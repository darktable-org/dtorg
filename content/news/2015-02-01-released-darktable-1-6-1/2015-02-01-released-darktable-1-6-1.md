author: houz
comments: true
date: 2015-02-01 16:17:33+00:00
layout: post
link: http://www.darktable.org/2015/02/released-darktable-1-6-1/
slug: released-darktable-1-6-1
title: released darktable 1.6.1
lede: fireworks_wide.jpg
wordpress_id: 3530
tags: announcement, darktable release

We are happy to announce that darktable 1.6.1 has been released. Due to an oversight on our side we forgot to do this announcement back when the actual release was done, so this is mostly for historical reasons.

The release notes and relevant downloads can be found attached to this git tag:
[https://github.com/darktable-org/darktable/releases/tag/release-1.6.1](https://github.com/darktable-org/darktable/releases/tag/release-1.6.1)
Please only use our provided packages (green buttons tar.xz and dmg) not the auto-created tarballs from github (grey buttons, zip and tar.gz). The latter are just git snapshots and will not work! Here's the direct link to tar.xz:
[https://github.com/darktable-org/darktable/releases/download/release-1.6.1/darktable-1.6.1.tar.xz](https://github.com/darktable-org/darktable/releases/download/release-1.6.1/darktable-1.6.1.tar.xz)
and the DMG:
[https://github.com/darktable-org/darktable/releases/download/release-1.6.1/darktable-1.6.1.dmg](https://github.com/darktable-org/darktable/releases/download/release-1.6.1/darktable-1.6.1.dmg)

this is a point release which fixes a couple of minor issues in the recent feature release 1.6.0 (such as a crash with images greater than 134 megapixels).

happy holidays everyone :)

sha1sums:
e3e0014361081364b56b6c02e886ba2fba6c6887 darktable-1.6.1.tar.xz
7173938cad7cd4c4a86de9438517c17166008f3c darktable-1.6.1.dmg


## General improvements:






  * Hide mouse in slideshow mode


  * Show option for txt overlay in the preferences Bugfixes:


  * ImageIO format TIFF: use scanline-based I/O. Fixes bug #10230


  * exif: always try to use Exiv2's lens detection for Olympus


  * demosaic: fix assertion


  * Do not deadlock in input color profile on unsupported input profiles


  * ensure that quick access preset menu is displayed correctly


  * Properly disconnect from the mipmap signal when leaving tethering mode


  * Avoid integer overflow on big images


  * OSX HiDPI fixes


  * Lua fixes




## Modules:






  * masks: enhance mouse hover detection


  * masks: allow smaller radius for circle and ellipse


  * spots: fix icon states bug #10216


  * spots: rounded correction. Fix bug #10045


  * spots: legacy_params(): adapt for latest mask changes


  * flip: fix legacy presets update


  * exposure: enable soft boundaries for black


  * zonesystem: remove stale button_release() callback


  * graduatednd: avoid rounding issues for rotation after moving whole line. Fixes bug #10241




## Camera support:






  * Pentax *istDL


  * 7D Mark II sRAW/mRAW


  * Samsung NX1




## White balance presets:






  * 7D Mark II


  * Panasonic DMC-LX7


