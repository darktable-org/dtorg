author: jo
comments: true
date: 2014-02-15 15:56:16+00:00
layout: post
link: http://www.darktable.org/2014/02/released-darktable-1-4-1/
slug: released-darktable-1-4-1
title: released darktable 1.4.1
wordpress_lede: paua.jpg.jpg
wordpress_id: 3250
tags: announcement, darktable

hi all,

as most of you probably noticed already, we published a point release, 1.4.1. the tarball is here:

[https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.1.tar.xz/download](https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.1.tar.xz/download)

make sure you check the signature:

[https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.1.tar.xz.asc/download](https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.1.tar.xz.asc/download)

the macintosh computer disk image with signature here:

[https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.1.dmg/download](https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.1.dmg/download)
[ https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.1.dmg.asc/download]( https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.1.dmg.asc/download)

this is just a point release, so not really any new features. detailed release notes are as follows:



	
  * export: consistent names for output formats

	
  * export to disk: overwrite file option

	
  * grain plugin now allows smaller coarseness and will display coarseness values half of what they used to be, this is merely a cosmetic change, your images are unaffected.

	
  * some masks related fixes

	
  * some lua related fixes

	
  * tiff writer (32bit float, little endian output, configurable compression)

	
  * tiff reader

	
  * subtly nicer scrollbar behavior

	
  * theme loading cornercase fixups

	
  * shadow & highlight module improvements (should be less prone to artifacts when used on new images)

	
  * allow importing more than 1 style at a time

	
  * regression was fixed when building darktable against bleeding edge glibc

	
  * Sony A77V enhanced color matrix

	
  * Nikon D5100 updated white balance presets

	
  * Nikon 1 V2 noise profile (and by extension J3/AW1)

	
  * Nikon 1 J1 noise profile (and by extension V1/J2/S1)

	
  * Pentax K3 noise profile

	
  * experimental support for Panasonic DMC-LF1 (we still need samples for the nonstandard aspect ratios)

	
  * experimental support for SONY DSC-RX100M2

	
  * experimental support for SONY NEX-3N

	
  * still no Nikon D5300/D3300 support, we're still looking into that.


the darktable release plus ppa is being phased out:
https://launchpad.net/~pmjdebruijn/+archive/darktable-release-plus

please switch to our regular darktable release ppa:
https://launchpad.net/~pmjdebruijn/+archive/darktable-release

enjoy!
