# openmoji

> A LaTeX package to use OpenMoji icons (v17.0.0) with support for color or black and white — Un package LaTeX pour utiliser les icônes OpenMoji (v17.0.0) en couleur ou en noir et blanc.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/openmoji) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `openmoji` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install openmoji
  ```

### Via TeX Live / tlmgr

```
tlmgr install openmoji
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/openmoji) (click *Code > Download ZIP*, or clone it).
2. Place `openmoji.sty` and `openmoji-*-all.pdf` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/openmoji/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\openmoji\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/openmoji/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{openmoji}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **Source** | https://openmoji.org (v17.0.0) CC-BY-SA-4.0 |