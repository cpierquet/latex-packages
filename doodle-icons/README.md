# doodle-icons

> A LaTeX package to use Doodle Icons (439 icons) — Un package LaTeX pour utiliser les icônes Doodle Icons (439 icônes)

---

## Installation

### Manual installation

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/doodle-icons) (click *Code > Download ZIP*, or clone it).
2. Place `doodle-icons.sty` and `doodleicons-all.pdf` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/doodle-icons/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\doodle-icons\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/doodle-icons/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

### Requirements

- Only the `graphicx` package is loaded (the key handling relies on `expl3`, part of the LaTeX kernel).
- A LaTeX kernel from October 2020 or later (TeX Live 2021 or later).
- Works with pdfLaTeX, LuaLaTeX and XeLaTeX.

---

## Quick start

```latex
\usepackage{doodle-icons}
```

```latex
Inline \doodleicon{bottle} version, and colored \textcolor{red}{\doodleicon{bottle}}.
```

The icons are black by default and take the current color, so `\textcolor`, `\color`, etc. work as expected.
The size can be set with the `height` key, for example `\doodleicon[height=2em]{bottle}`.
All the icon names (and their page in `doodleicons-all.pdf`) are listed in the documentation.

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License (package)** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **License (icons)** | [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |
| **Source** | Doodle Icons by Khushmeen Sidhu — https://khushmeen.gumroad.com/l/doodleicons (CC0 license) |