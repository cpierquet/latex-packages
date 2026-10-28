#!/usr/bin/env python3
"""
svg2pdf.py — convertit les SVG des dossiers de SVG/ en PDF recolorisables.

    SVG/animaux/chat.svg   ->   PDF/animaux/chat.pdf

Usage :  python3 svg2pdf.py            (dossiers SVG/ -> PDF/)
         python3 svg2pdf.py SVG PDF    (autres noms de dossiers)

Les couleurs sont retirées (SVG remis en noir, puis opérateurs de couleur
supprimés dans le PDF) pour que \\textcolor{...}{\\includegraphics{...}} fonctionne.
Le blanc pur est conservé.

Dépendances : rsvg-convert (ou inkscape, ou cairosvg), lxml, pikepdf
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pikepdf
from lxml import etree

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "SVG")
DST = Path(sys.argv[2] if len(sys.argv) > 2 else "PDF")

# Canevas carré commun : chaque icône est centrée, SANS changement d'échelle, dans un
# carré CANVAS x CANVAS (None = plus grande dimension rencontrée dans tous les SVG).
# Les SVG sont rognés au plus près du dessin (ex. 105x19 pour "menu-2") : sans cela,
# \includegraphics[height=...] agrandirait chaque icône différemment.
SQUARE = True
CANVAS = None

PROPS = ("fill", "stroke", "stop-color", "flood-color", "lighting-color", "color")
KEEP = {"none", "transparent", "inherit", "initial", "unset"}
CSS = re.compile(r"(?P<p>" + "|".join(PROPS) + r")\s*:\s*(?P<v>[^;}]+)", re.I)


def new_value(v):
    low = re.sub(r"\s+", "", v.strip().lower())
    if low.startswith("url("):
        return "#000000"
    if low in KEEP or low in {"#fff", "#ffffff", "white", "rgb(255,255,255)"}:
        return None
    return "#000000"


def css(text):
    return CSS.sub(lambda m: m.group(0) if new_value(m["v"]) is None else f"{m['p']}:#000000", text)


def box(root):
    """(x, y, largeur, hauteur) du SVG, d'après viewBox ou width/height."""
    vb = root.get("viewBox")
    if vb:
        try:
            x, y, w, h = (float(v) for v in re.split(r"[\s,]+", vb.strip()))
            return x, y, w, h
        except ValueError:
            pass

    def num(a):
        m = re.match(r"\s*([\d.]+)\s*(px)?\s*$", root.get(a, ""))
        return float(m.group(1)) if m else None

    w, h = num("width"), num("height")
    return (0.0, 0.0, w, h) if w and h else None


def neutralize(svg, canvas=None):
    tree = etree.parse(str(svg), etree.XMLParser(remove_comments=True, huge_tree=True))
    if canvas:
        b = box(tree.getroot())
        if b:
            x, y, w, h = b
            tree.getroot().set(
                "viewBox", f"{x - (canvas - w) / 2:.4f} {y - (canvas - h) / 2:.4f} {canvas:.4f} {canvas:.4f}"
            )
            tree.getroot().set("width", f"{canvas:g}")
            tree.getroot().set("height", f"{canvas:g}")
        else:
            print(f"[AVERTISSEMENT] {svg} : taille introuvable, canevas non appliqué", file=sys.stderr)
    for el in tree.getroot().iter():
        if not isinstance(el.tag, str):
            continue
        for p in PROPS:
            if el.get(p) is not None and new_value(el.get(p)):
                el.set(p, "#000000")
        if el.get("style"):
            el.set("style", css(el.get("style")))
        if el.tag.endswith("style") and el.text:
            el.text = css(el.text)
    return etree.tostring(tree, xml_declaration=True, encoding="utf-8")


def convert(svg, pdf):
    if shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-f", "pdf", "-o", str(pdf), str(svg)], check=True)
    elif shutil.which("inkscape"):
        subprocess.run(["inkscape", str(svg), "--export-type=pdf", f"--export-filename={pdf}"],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        import cairosvg
        cairosvg.svg2pdf(url=str(svg), write_to=str(pdf))


def strip_colors(pdf):
    ops = {"rg", "RG", "g", "G", "k", "K", "sc", "SC", "scn", "SCN", "cs", "CS"}
    with pikepdf.open(str(pdf), allow_overwriting_input=True) as doc:
        for page in doc.pages:
            kept = []
            for ins in pikepdf.parse_content_stream(page):
                op = str(ins.operator)
                if op in ops:
                    vals = [float(x) for x in ins.operands]
                    white = op in {"rg", "RG", "g", "G"} and vals and all(v >= 0.999 for v in vals)
                    if not white:
                        continue
                kept.append(ins)
            page.Contents = doc.make_stream(pikepdf.unparse_content_stream(kept))
        doc.save(str(pdf))


def main():
    files = sorted(SRC.rglob("*.svg"))
    if not files:
        sys.exit(f"Aucun SVG trouvé dans {SRC}/")
    canvas = None
    if SQUARE:
        canvas = CANVAS
        if canvas is None:
            sizes = [b for b in (box(etree.parse(str(f)).getroot()) for f in files) if b]
            canvas = max(max(b[2], b[3]) for b in sizes)
        print(f"Canevas carré commun : {canvas:g} x {canvas:g}")
    ok = 0
    with tempfile.TemporaryDirectory() as tmp:
        tmp_svg = Path(tmp) / "in.svg"
        for svg in files:
            pdf = DST / svg.relative_to(SRC).with_suffix(".pdf")
            pdf.parent.mkdir(parents=True, exist_ok=True)
            try:
                tmp_svg.write_bytes(neutralize(svg, canvas))
                convert(tmp_svg, pdf)
                strip_colors(pdf)
                ok += 1
            except Exception as e:
                print(f"[ERREUR] {svg} : {e}", file=sys.stderr)
    print(f"{ok}/{len(files)} PDF écrits dans {DST}/")


main()
