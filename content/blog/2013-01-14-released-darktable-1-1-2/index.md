---
author: smn
comments: true
date: 2013-01-14 23:24:16+00:00
layout: post
link: /2013/01/released-darktable-1-1-2/
slug: released-darktable-1-1-2
title: "Released darktable 1.1.2"
lede: flamingos.png
wordpress_id: 2671
tags:
  - announcement
  - darktable release
---
Dear all,

we just released darktable 1.1.2, a point release (so nothing too fancy) with a couple of bugfixes and better camera support. Additionally it comes with an updated usermanual which is available here:

[https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-usermanual-1.1.2.pdf/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-usermanual-1.1.2.pdf/download)

The tarball can be found here:

[https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.2.tar.gz/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.2.tar.gz/download)

and a new disk image for Mac users is provided as well:

[https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.2.dmg/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.2.dmg/download)

The various packages for your favourite distro are already on their way. The Ubuntu PPA should be updated already for example, and the opensuse package is available from [https://software.opensuse.org/package/darktable](https://software.opensuse.org/package/darktable) and will be included in the upcoming opensuse 12.3 thanks to Togan Muftuoglu.

## Changelog:

* Fix export resolution rounding issue (as in previous version it could be off-by-one)
* Correctly set output dimension in exif instead of passing the raw resolution verbatim
* Local average green eq. was fixed (it now works on high ISO images as well, and should no longer produce hot pixels)
* Use ordered arrays in XMP files
* Disable export parallelism for flickr/picasa export
* Don't enter tethering mode when there is no camera attached (this made darktable look as if it was hung, even though that wasn't the case)
* Bring back the pin for map thumbnails
* Improved TIFF support
* Vignetting now has a dithering option (to mitigate occasional banding)
* Read Nikon subject distance properly
* Assorted FreeBSD fixes
* Various OpenCL fixes
* Usermanual updates

## Support for the following camera's with either preliminarily added or updated:

* Canon EOS 6D
* Canon PowerShot s110
* Canon PowerShot g15
* Canon PowerShot sx50 hs
* Nikon 1 v2
* Nikon D600
* Nikon Coolpix P7700
* Olympus E Pl5
* Olympus E PM2
* Olympus XZ 2
* Panasonic DMC GH3
* Panasonic DMC LX7
* Pentax K5ii
* Samsung EX2f
* Sony RX1
* Sony NEX 6
* Sony SLT A99
* Sony NEX c3 blackpoint/greenshift fix

## White balance preset updates:

* Canon EOS 550D
* Canon EOS 5D Mark III
* Olympus XZ 1
* Sony NEX C3
* Sony SLT A57
* Sony nex 5N
* Panasonic DMC GH3

This stable release was mostly brought to you by Pascal says the hall-of-fame script:

* 30 Pascal de Bruijn
* 29 Ulrich Pegelow
* 13 parafin
* 6 Tobias Ellinghaus
* 5 johannes hanika
* 4 Pascal Obry
* 4 Jean-Sébastien Pédron
* 2 Roman Lebedev
* 2 Jose Carlos Garcia Sogo
* 1 tatica
* 1 Simon Spannagel
* 1 Roland Riegel
* 1 Richard Tollerton
* 1 Richard Levitte
* 1 Olivier Tribout
* 1 Michal Babej
* 1 Ger Siemerink
* 1 Chris Mason
* 1 Boucman

Enjoy!
