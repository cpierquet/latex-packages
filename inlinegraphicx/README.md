# inlinegraphicx

> A LaTeX package to insert inline images with automatic size and positioning — Un package LaTeX pour insérer des images en ligne avec taille et positionnement automatiques

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/inlinegraphicx) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `inlinegraphicx` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install inlinegraphicx
  ```

### Via TeX Live / tlmgr

```
tlmgr install inlinegraphicx
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/inlinegraphicx) (click *Code > Download ZIP*, or clone it).
2. Place `inlinegraphicx.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/inlinegraphicx/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\inlinegraphicx\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/inlinegraphicx/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{inlinegraphicx}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
