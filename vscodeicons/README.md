# vscodeicons

> This package aims to provide "vscode icons" for LaTeX like fontawesome or simpleicons.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/vscodeicons) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `vscodeicons` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install vscodeicons
  ```

### Via TeX Live / tlmgr

```
tlmgr install vscodeicons
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/vscodeicons) (click *Code > Download ZIP*, or clone it).
2. Place `vscodeicons.sty` and `vscodeicons-*-all.pdf` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/vscodeicons/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\vscodeicons\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/vscodeicons/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{vscodeicons}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **Source** | https://github.com/vscode-icons/vscode-icons (v12.19.0) MIT License
| | Icons are licensed under the Creative Commons - ShareAlike (CC BY-SA) license. |
| | Branded icons are licensed under their copyright license. |