# nodepthtext

> A LaTeX package to modify small texts in order to remove the depth of letters — Un package LaTeX pour modifier de petits textes afin de supprimer la profondeur des lettres

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/nodepthtext) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `nodepthtext` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install nodepthtext
  ```

### Via TeX Live / tlmgr

```
tlmgr install nodepthtext
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/nodepthtext) (click *Code > Download ZIP*, or clone it).
2. Place `nodepthtext.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/nodepthtext/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\nodepthtext\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/nodepthtext/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{nodepthtext}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
