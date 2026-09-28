# mathador

> A LaTeX package providing commands for the French game "Mathador" — Un package LaTeX proposant des commandes pour le jeu français « Mathador »

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/mathador) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `mathador` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install mathador
  ```

### Via TeX Live / tlmgr

```
tlmgr install mathador
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/mathador) (click *Code > Download ZIP*, or clone it).
2. Place `mathador.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/mathador/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\mathador\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/mathador/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{mathador}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later · other-free (game content by Éric Trouillet and CANOPÉ) |
| **Credits** | https://www.mathador.fr (author : Éric Trouillot -- editor : CANOPÉ) |
| | Mathador est une marque protégée de Monsieur Eric Trouillot et de Réseau Canopé. |