# WriteOnGrid

> A LaTeX package providing an environment to create grids (5×5, Seyes, Ruled) and commands to write text on the lines — Un package LaTeX proposant un environnement pour créer des grilles (5×5, Séyès, lignées) et des commandes pour écrire sur les lignes

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/writeongrid) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `WriteOnGrid` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install WriteOnGrid
  ```

### Via TeX Live / tlmgr

```
tlmgr install WriteOnGrid
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/writeongrid) (click *Code > Download ZIP*, or clone it).
2. Place `WriteOnGrid.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/WriteOnGrid/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\WriteOnGrid\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/WriteOnGrid/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{WriteOnGrid}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
