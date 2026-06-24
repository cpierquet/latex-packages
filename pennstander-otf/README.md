pennstander-otf fonts
=====================

## Description

`pennstander-otf` is a font family (based on v0.4.1 version) with math support  
Official site is https://github.com/juliusross1/Pennstander  
Inigial version of font is from https://etceteratype.co/pages/grandstander, by Tyler Finck  
Pennstander and PennstanderMath typeface are available under the SIL Open Font License 1.1 license

## Contents

* the `tex/`   directory holds the fontspec configuration files and the .sty file;
* the `doc/`   directory holds short documentation with samples;
* the `font/`...directory holds font files.

## Usage

lualatex/xelatex and fontspec are necessary in order to use pennstander fonts.

Several weights are given : Thin / ExtraLight / Light / Regular / Medium / SemiBold / Bold / ExtraBold / Black

## Installation

This package is meant to be installed automatically by TeXLive, MikTeX, etc.  
Otherwise, `pennstander-otf` can be installed under TEXMFHOME or TEXMFLOCAL, f.i.

+ sty file (`tex/*.sty`) in directory `texmf-local/tex/latex/pennstander-otf/`
+ fontspec files (`tex/*.fontspec`) in directory `texmf-local/tex/latex/pennstander-otf/`
+ documentation (from doc/ directory) in `texmf-local/doc/fonts/public/pennstander-otf/`
+ font files in `texmf-local/fonts/opentype/.../pennstander-otf/`

Don't forget to rebuild the file database (mktexlsr or so) if you install under TEXMFLOCAL.  
Finally, you may want to make the system font database aware of the `pennstander-otf` fonts (fontconfig under Linux).

## License

* Files are distributed under the terms of the LaTeX Project
Public License from CTAN archives in directory macros/latex/base/lppl.txt.  
Either version 1.3 or, at your option, any later version.  
Pennstander and PennstanderMath typeface are available under the SIL Open Font License 1.1 license.

## Changes
* v0.4.1 (based on 0.4.1 version)
* v0.4   (based on 0.4 version)
* v0.3a  (bugfixes)
* v0.3   (new version of otf + new fontfaces + variable ttf version)
* v0.1   (experimental).

---
Copyright 2025-2026 C. Pierquet
E-mail: cpierquet (at) outlook (dot) fr
