fantasquesansmono-otf fonts
===================

## Description

`fantasquesansmono-otf` is a font family with mono/code support (actual version v1.8.0).
Official site is https://github.com/belluzj/fantasque-sans.
FantasqueSansMono typeface family are available under the SIL Open Font License 1.1 license.

## Contents

* the `tex/`   directory holds the fontspec configuration files and the .sty file;
* the `doc/`   directory holds short documentation with samples;
* the `font/`...directory holds font files.

## Usage

lualatex/xelatex and fontspec are necessary in order to use FantasqueSansMono fonts.

Mono version or Code version (with ligatures) are available.

## Installation

This package is meant to be installed automatically by TeXLive, MikTeX, etc.  
Otherwise, `fantasquesansmono-otf` can be installed under TEXMFHOME or TEXMFLOCAL, f.i.

+ sty file (`tex/*.sty`) in directory `texmf-local/tex/latex/fantasquesansmono-otf/`
+ fontspec files (`tex/*.fontspec`) in directory `texmf-local/tex/latex/fantasquesansmono-otf/`
+ documentation (from doc/ directory) in `texmf-local/doc/fonts/.../fantasquesansmono-otf/`
+ font files in `texmf-local/fonts/.../fantasquesansmono-otf/`

Don't forget to rebuild the file database (mktexlsr or so) if you install under TEXMFLOCAL.  
Finally, you may want to make the system font database aware of the `fantasquesansmono-otf` fonts (fontconfig under Linux).

## License

* Files are distributed under the terms of the LaTeX Project
Public License from CTAN archives in directory macros/latex/base/lppl.txt.  
Either version 1.3 or, at your option, any later version.  
FantasqueSansMono family typeface are available under the SIL Open Font License 1.1 license.

## Changes
* v1.8.0 (experimental).

---
Copyright 2026 C. Pierquet
E-mail: cpierquet (at) outlook (dot) fr
