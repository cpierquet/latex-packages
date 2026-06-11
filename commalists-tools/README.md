# commalists-tools

> A LaTeX package providing macros for basic manipulation of comma-separated lists — Un package LaTeX proposant des macros pour la manipulation de listes séparées par des virgules.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/commalists-tools) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `commalists-tools` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install commalists-tools
  ```

### Via TeX Live / tlmgr

```
tlmgr install commalists-tools
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/commalists-tools) (click *Code > Download ZIP*, or clone it).
2. Place `commalists-tools(-l3).sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/commalists-tools/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\commalists-tools\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/commalists-tools/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{commalists-tools}
%or
\usepackage{commalists-tools-l3}
```

---

## Author & License & 

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Credits** | Valentin Dao, aka ankaa3908 |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
