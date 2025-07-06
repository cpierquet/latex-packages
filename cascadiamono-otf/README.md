cascadiamono-otf fonts
======================

## Description

`cascadiamono-otf` is the version of cascadiacode-otf without ligatures.  
Official repo is https://github.com/microsoft/cascadia-code  
CascadiaCode is already present, it's just a fontspec file (or a fontfamily) for using CascadiaMono version :-)

## Contents

* the `tex/`   directory holds the fontspec configuration files and the .sty file;
* the `doc/`   directory holds short documentation with samples.

## Usage

lualatex/xelatex and fontspec are necessary in order to use cascadiamono fonts.

* 'Normal' version of the font is available with global `\setmonofont{CascadiaMono}[options]` or locally with `\cascadiamono`.
* 'SemiLight' version of the font is available with global `\setmonofont{CascadiaMono-SemiLight}[options]` or locally with `\cascadiamonosemilight`.
* 'Light' version of the font is available with global `\setmonofont{CascadiaMono-Light}[options]` or locally with `\cascadiamonolight`.
* 'ExtraLight' version of the font is available with global `\setmonofont{CascadiaMono-ExtraLight}[options]` or locally with `\cascadiamonoextralight`.

## Installation

This package is meant to be installed automatically by TeXLive, MikTeX, etc.  
Otherwise, `cascadiamono-otf` can be installed under TEXMFHOME or TEXMFLOCAL, f.i.

+ sty file (`tex/cascadiamono-otf.sty`) in directory `texmf-local/tex/latex/cascadiamono-otf/`
+ fontspec files (`tex/*.fontspec`) in directory `texmf-local/tex/latex/cascadiamono-otf/`
+ documentation (from doc/ directory) in `texmf-local/doc/fonts/public/cascadiamono-otf/`

Don't forget to rebuild the file database (mktexlsr or so) if you install under TEXMFLOCAL.  
Finally, you may want to make the system font database aware of the `cascadiamono-otf` fonts (fontconfig under Linux).

## License

* Files are distributed under the terms of the LaTeX Project
* Public License from CTAN archives in directory macros/latex/base/lppl.txt.
* Either version 1.3 or, at your option, any later version.

## Changes
* v0.3 (sty file with fontfamily & code version)
* v0.2 (new alt weights)
* v0.1 (experimental).

---
Copyright 2024--2025 C. Pierquet (with help from D. Flipo)  
E-mail: cpierquet (at) outlook (dot) fr
