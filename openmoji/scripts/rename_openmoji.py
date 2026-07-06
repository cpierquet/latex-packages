#!/usr/bin/env python3
"""
rename_openmoji.py — reconstruit le pipeline de renommage OpenMoji perdu.

Principe : chaque ligne du CSV OpenMoji donne un hexcode exact (colonne
`hexcode`) qui correspond EXACTEMENT au nom de fichier source
(`<HEXCODE>.svg`). On ne fait JAMAIS de recherche par sous-chaîne sur le
hexcode (c'est ce qui causait les collisions du type 1F636 / 1F636-200D-...),
on utilise une correspondance exacte via un dict Python.

Le nom de fichier cible est dérivé de la colonne `annotation`, nettoyé pour
retrouver la convention historique du package (celle visible dans
openmoji.sty) :
    - "&"        -> "and"
    - “ / ”      -> "-"   (guillemets typographiques des boutons japonais)
    - '          -> "'"   (apostrophe typographique -> apostrophe simple)
    - ": "       -> "- "  (variantes de carnation, drapeaux, "person walking: ...")
    - "#"        -> "hashtag"
    - "*"        -> "-"
    - minuscules
    - suppression des accents/diacritiques (é -> e, ñ -> n, Å -> a, ü -> u, ...)

Usage :
    python3 rename_openmoji.py --csv openmoji.csv --svg-dir ./svg --out-dir ./svg-renamed
    python3 rename_openmoji.py --csv openmoji.csv --svg-dir ./svg --out-dir ./svg-renamed --mode copy
    python3 rename_openmoji.py --csv openmoji.csv --svg-dir ./svg --out-dir ./svg-renamed --dry-run

Options :
    --mode {copy,move,link}   copie (défaut), déplace, ou crée un lien symbolique
    --dry-run                 n'écrit rien, affiche juste ce qui serait fait
    --ext .svg                extension des fichiers source (défaut: .svg)
    --report report.csv       exporte un rapport détaillé (nom, hexcode, statut)
    --skip-proprietary        ignore les hexcodes propriétaires OpenMoji (E-codes)
                              en cas de doublon de nom avec un hexcode Unicode officiel
"""

import argparse
import csv
import shutil
import sys
import unicodedata
from pathlib import Path


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


# Correctifs ponctuels pour des données CSV corrompues (encodage perdu en amont)
MANUAL_FIXES = {
    "castile and le\ufffdn flag": "castile and leon flag",
}


def clean_name(annotation: str) -> str:
    s = annotation
    s = s.replace("&", "and")
    s = s.replace("\u201c", "-").replace("\u201d", "-")  # “ ”
    s = s.replace("\u2019", "'")  # ’
    s = s.replace(": ", "- ")
    s = s.replace("#", "hashtag")
    s = s.replace("*", "-")
    s = s.lower()
    s = strip_accents(s)
    if s in MANUAL_FIXES:
        s = MANUAL_FIXES[s]
    return s.strip()


def is_proprietary(hexcode: str) -> bool:
    """Les hexcodes propriétaires OpenMoji (hors Unicode officiel) commencent par E."""
    return hexcode.upper().startswith("E")


def sanitize_filename(name: str) -> str:
    """Rend le nom sûr comme nom de fichier (garde les espaces, vire les / et \\)."""
    return name.replace("/", "-").replace("\\", "-")


def load_rows(csv_path: Path):
    with csv_path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_mapping(rows, skip_proprietary: bool):
    """Construit le dict {nom_nettoye: [ (hexcode, row), ... ]} pour détecter les collisions."""
    mapping = {}
    for row in rows:
        name = clean_name(row["annotation"])
        mapping.setdefault(name, []).append(row)

    resolved = {}
    conflicts = []
    for name, group in mapping.items():
        if len(group) == 1:
            resolved[name] = group[0]
            continue
        # Doublon de nom (ex: "brain" en 1F9E0 et E319)
        if skip_proprietary:
            officials = [r for r in group if not is_proprietary(r["hexcode"])]
            if len(officials) == 1:
                resolved[name] = officials[0]
                conflicts.append((name, group, "resolu:officiel_garde"))
                continue
        # Non resolu automatiquement -> on suffixe pour ne rien perdre
        for i, r in enumerate(group, start=1):
            suffixed = name if i == 1 else f"{name} ({i})"
            resolved[suffixed] = r
        conflicts.append((name, group, "suffixe"))
    return resolved, conflicts


def main():
    ap = argparse.ArgumentParser(description="Renomme les SVG OpenMoji (hexcode -> nom nettoyé)")
    ap.add_argument("--csv", required=True, type=Path)
    ap.add_argument("--svg-dir", required=True, type=Path)
    ap.add_argument("--out-dir", required=True, type=Path)
    ap.add_argument("--ext", default=".svg")
    ap.add_argument("--mode", choices=["copy", "move", "link"], default="copy")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", type=Path, default=None)
    ap.add_argument("--skip-proprietary", action="store_true")
    args = ap.parse_args()

    rows = load_rows(args.csv)
    resolved, conflicts = build_mapping(rows, args.skip_proprietary)

    if conflicts:
        print(f"[!] {len(conflicts)} collision(s) de nom détectée(s) :", file=sys.stderr)
        for name, group, action in conflicts:
            codes = ", ".join(r["hexcode"] for r in group)
            print(f"    - {name!r} : {codes}  -> {action}", file=sys.stderr)

    if not args.dry_run:
        args.out_dir.mkdir(parents=True, exist_ok=True)

    report_rows = []
    n_ok, n_missing = 0, 0
    for target_name, row in resolved.items():
        hexcode = row["hexcode"]
        src = args.svg_dir / f"{hexcode}{args.ext}"
        dst_name = sanitize_filename(target_name) + args.ext
        dst = args.out_dir / dst_name

        if not src.exists():
            n_missing += 1
            report_rows.append([target_name, hexcode, "MANQUANT", str(src)])
            continue

        n_ok += 1
        report_rows.append([target_name, hexcode, "OK", str(dst)])
        if args.dry_run:
            continue
        if args.mode == "copy":
            shutil.copy2(src, dst)
        elif args.mode == "move":
            shutil.move(str(src), str(dst))
        elif args.mode == "link":
            if dst.exists():
                dst.unlink()
            dst.symlink_to(src.resolve())

    print(f"\nTotal lignes CSV     : {len(rows)}")
    print(f"Noms uniques résolus : {len(resolved)}")
    print(f"Fichiers traités     : {n_ok}")
    print(f"Fichiers manquants   : {n_missing}")

    if args.report:
        with args.report.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["nom_cible", "hexcode", "statut", "chemin"])
            w.writerows(report_rows)
        print(f"Rapport écrit : {args.report}")


if __name__ == "__main__":
    main()
