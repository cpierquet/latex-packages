# skill-icons

> A LaTeX package to use the Skill Icons (837 icons, dark and light themes) — Un package LaTeX pour utiliser les icônes Skill Icons (837 icônes, thèmes sombre et clair)

---

## Installation

### Manual installation

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/skill-icons) (click *Code > Download ZIP*, or clone it).
2. Place `skill-icons.sty`, `skill-icons-dark-all.pdf` and `skill-icons-light-all.pdf` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/skill-icons/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\skill-icons\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/skill-icons/`
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
\usepackage{skill-icons}
```

```latex
Inline \skillicons{python} version, and light \skillicons[theme=light]{python} version.
```

The icons are colored (logos with their own background). The size can be set with the `height` key, for example `\skillicons[height=2em]{python}`.
All the icon names (and their page in the PDF files) are listed in the documentation.

Two themes are available, `dark` (by default) and `light`. The theme can be chosen for one icon with the key `theme`, or for the whole document:

```latex
\usepackage[light]{skill-icons}      % package option
\skilliconssetup{theme=dark}         % at any time (global)
\skillicons[theme=light]{github}     % for one icon
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License (package)** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **License (icons)** | [MIT](https://github.com/LelouchFR/skill-icons/blob/main/LICENSE) — © 2022 tandpfun, © 2024 Baptiste Zahnow |
| **Source** | https://github.com/LelouchFR/skill-icons (fork of https://github.com/tandpfun/skill-icons) |

> The logos remain the property of their respective owners.
