# tikz-decofonts

> A LaTeX package providing simple decoration fonts made with TikZ for short texts (paint brush, ink brush, pixelart brush…) — Un package LaTeX proposant des polices de décoration simples faites avec TikZ pour de courts textes (pinceau, encre, pixelart…)

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/tikz-decofonts) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `tikz-decofonts` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install tikz-decofonts
  ```

### Via TeX Live / tlmgr

```
tlmgr install tikz-decofonts
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/tikz-decofonts) (click *Code > Download ZIP*, or clone it).
2. Place `tikz-decofonts.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/tikz-decofonts/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\tikz-decofonts\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/tikz-decofonts/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{tikz-decofonts}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later · CC BY-SA 4.0 |
| | CC BY-SA 4.0 (https://tex.stackexchange.com/questions/475141/simulating-paintbrush-strokes-in-tikz from user121799) |
| | CC BY-SA 4.0 (https://tex.stackexchange.com/questions/460836/custom-line-cap-to-simulate-inked-line-in-tikz/460842#460842 from user121799) |
| | LPPL 1.3c (https://github.com/meyvenil0844-byte/-multicancel from meyvenil0844-byte) |