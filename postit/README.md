# postit

> A LaTeX package providing commands to create Post-it-like boxes with tcolorbox — Un package LaTeX proposant des commandes pour créer des boîtes style Post-it avec tcolorbox

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/postit) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `postit` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install postit
  ```

### Via TeX Live / tlmgr

```
tlmgr install postit
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/postit) (click *Code > Download ZIP*, or clone it).
2. Place `postit.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/postit/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\postit\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/postit/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{postit}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
