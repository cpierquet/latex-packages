# tablericons

> This package aims to provide "tabler Icons" for LaTeX like fontawesome or simpleicons.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/tablericons) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `tablericons` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install tablericons
  ```

### Via TeX Live / tlmgr

```
tlmgr install tablericons
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/tablericons) (click *Code > Download ZIP*, or clone it).
2. Place `tablericons.sty` and `tablericons-*-all.pdf` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/tablericons/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\tablericons\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/tablericons/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{tablericons}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **Source** | https://tabler.io/icons (v3.44) MIT License |