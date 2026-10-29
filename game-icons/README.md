# game-icons

> A LaTeX package to use Game-icons.net icons (4133 icons) — Un package LaTeX pour utiliser les icônes Game-icons.net (4133 icônes)

---

## Installation

### Manual installation

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/game-icons) (click *Code > Download ZIP*, or clone it).
2. Place `game-icons.sty`, `gameicons-all.pdf` and `gameicons-badges-all.pdf` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/game-icons/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\game-icons\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/game-icons/`
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
\usepackage{game-icons}
```

```latex
Inline \gameicons{meeple} version, and colored \textcolor{red}{\gameicons{meeple}}.
```

The icons are black by default and take the current color, so `\textcolor`, `\color`, etc. work as expected.
The size can be set with the `height` key, for example `\gameicons[height=2em]{meeple}`.
All the icon names (and their page in `gameicons-all.pdf`) are listed in the documentation.

A badge (59 available) can be added to an icon, and recolored independently:

```latex
\gameicons[badge=bolt]{wizard-staff}
\gameicons[badge=skull,badgepos=tl,badgecolor=red,badgescale=0.5]{anvil}
```

Keys: `badge` (name), `badgepos` (`br` by default, `bl`, `tr`, `tl`, or `c` for the center), `badgescale` (`0.4` by default), `badgecolor` (needs `xcolor`). A badge alone: `\gameiconsbadge{bolt}`.

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License (package)** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **License (icons)** | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) — attribution required |
| **Source** | Icons by Lorc, Delapouite & contributors — https://game-icons.net |

> Attribution example: *"Icons made by Lorc, Delapouite & contributors. Available on https://game-icons.net"*
