# lucide-icons

> A LaTeX package to use Lucide icons (v0.475) — Un package LaTeX pour utiliser les icônes Lucide (v1.23.0)

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/lucide-icons) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `lucide-icons` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install lucide-icons
  ```

### Via TeX Live / tlmgr

```
tlmgr install lucide-icons
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/lucide-icons) (click *Code > Download ZIP*, or clone it).
2. Place `lucide-icons.sty` and `lucide-icons-all.pdf` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/lucide-icons/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\lucide-icons\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/lucide-icons/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{lucide-icons}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **Source** | https://lucide.dev (v1.23.0) ISC License |