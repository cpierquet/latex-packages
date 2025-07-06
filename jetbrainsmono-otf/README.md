jetbrainsmono-otf fonts
=======================

## Description

`jetbrainsmono-otf` is the version of jetbrainsmono with or without ligatures.  
Official site is https://www.jetbrains.com/lp/mono/  
JetBrains Mono typeface is available under the SIL Open Font License 1.1 license

## Contents

* the `tex/`   directory holds the fontspec configuration files and the .sty file;
* the `doc/`   directory holds short documentation with samples;
* the `font/`...directory holds font files.

## Usage

lualatex/xelatex and fontspec are necessary in order to use cascadiamono fonts.  
`mono` version (w/o ligatures) and `code` version (w ligatures) are available.

* 'Normal' version of the font is available with `\setmonofont{jetbrainsmono/code}[options]` or with `\jetbrainsmono`.
* 'Medium' version of the font is available with `\setmonofont{jetbrainsmono/code-medium}[options]` or with `\jetbrainsmonomedium`.
* 'Light' version of the font is available with `\setmonofont{jetbrainsmono/code-light}[options]` or with `\jetbrainsmonolight`.
* 'ExtraLight' version of the font is available with `\setmonofont{jetbrainsmono/code-extralight}[options]` or with `\jetbrainsmonoextralight`.
* 'Thin' version of the font is available with `\setmonofont{jetbrainsmono-thin}[options]` or with `\jetbrainsmonothin`.

## Installation

This package is meant to be installed automatically by TeXLive, MikTeX, etc.  
Otherwise, `jetbrainsmono-otf` can be installed under TEXMFHOME or TEXMFLOCAL, f.i.

+ sty file (`tex/*.sty`) in directory `texmf-local/tex/latex/jetbrainsmono-otf/`
+ fontspec files (`tex/*.fontspec`) in directory `texmf-local/tex/latex/jetbrainsmono-otf/`
+ documentation (from doc/ directory) in `texmf-local/doc/fonts/public/jetbrainsmono-otf/`
+ font files in `texmf-local/fonts/opentype/SIL/jetbrainsmono/`

Don't forget to rebuild the file database (mktexlsr or so) if you install under TEXMFLOCAL.  
Finally, you may want to make the system font database aware of the `jetbrainsmono-otf` fonts (fontconfig under Linux).

## License

* Files are distributed under the terms of the LaTeX Project
Public License from CTAN archives in directory macros/latex/base/lppl.txt.  
Either version 1.3 or, at your option, any later version.  
JetBrains Mono typeface is available under the SIL Open Font License 1.1 license.

## Changes
* v0.1 (experimental).

---
Copyright 2025 C. Pierquet (with help from D. Flipo)  
E-mail: cpierquet (at) outlook (dot) fr
