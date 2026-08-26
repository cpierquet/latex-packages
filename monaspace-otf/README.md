monaspace-otf fonts
===================

## Description

`monaspace-otf` is a font family with mono/code support (actual version v1.400).
Official site is https://monaspace.githubnext.com.
Monaspace typeface family are available under the SIL Open Font License 1.1 license.

## Contents

* the `tex/`   directory holds the fontspec configuration files and the .sty file;
* the `doc/`   directory holds short documentation with samples;
* the `font/`...directory holds font files.

## Usage

lualatex/xelatex and fontspec are necessary in order to use monaspace fonts.

Several weights are given : ExtraLight / Light / Regular / Medium / SemiBold

Several styles are given : Argon / Krypton / Neon / Radon / Xenon

## Installation

This package is meant to be installed automatically by TeXLive, MikTeX, etc.  
Otherwise, `monaspace-otf` can be installed under TEXMFHOME or TEXMFLOCAL, f.i.

+ sty file (`tex/*.sty`) in directory `texmf-local/tex/latex/monaspace-otf/`
+ fontspec files (`tex/*.fontspec`) in directory `texmf-local/tex/latex/monaspace-otf/`
+ documentation (from doc/ directory) in `texmf-local/doc/fonts/.../monaspace-otf/`
+ font files in `texmf-local/fonts/.../monaspace-otf/`

Don't forget to rebuild the file database (mktexlsr or so) if you install under TEXMFLOCAL.  
Finally, you may want to make the system font database aware of the `monaspace-otf` fonts (fontconfig under Linux).

## License

* Files are distributed under the terms of the LaTeX Project
Public License from CTAN archives in directory macros/latex/base/lppl.txt.  
Either version 1.3 or, at your option, any later version.  
Monaspace family typeface are available under the SIL Open Font License 1.1 license.

## Changes
* v1.400 (experimental).
* v0.1 (experimental).

---
Copyright 2025 C. Pierquet
E-mail: cpierquet (at) outlook (dot) fr
