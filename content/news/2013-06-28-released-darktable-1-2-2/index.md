---
author: smn
comments: true
date: 2013-06-28 07:24:49+00:00
layout: post
link: /2013/06/released-darktable-1-2-2/
slug: released-darktable-1-2-2
title: released darktable 1.2.2
lede: 3.jpg
wordpress_id: 2955
tags:
  - announcement
  - darktable release
---
Dear all,

we just released another patch version for the stable branch 1.2. As usual you can find the source tarball here:

* [source tarball](https://sourceforge.net/projects/darktable/files/darktable/1.2/darktable-1.2.2.tar.xz/download)
* The [Ubuntu PPA](https://launchpad.net/~pmjdebruijn/+archive/darktable-release) has already been updated by Pascal (thanks!),
* [OS X disk image](https://sourceforge.net/projects/darktable/files/darktable/1.2/darktable-1.2.2.dmg/download)
* other builds will follow soon

We don't have too many commits to report but since quite some of those we picked concern support of new hardware we decided to release this version comparatively early making it more or less a "hardware release":

* updated rawspeed r553. Support for
* Canon EOS 700D
* Nikon Coolpix P330
* New Olymbus base curve
* Updated Adobe Coeffs

## Enhanced color matrices:

* Canon 700D (from Canon 650D)
* Canon 100D (from Canon 650D)
* Sony NEX-7

## White balance presets:

* Some updates from UFRaw
* Canon 100D
* Canon 700D
* Sony SLT-A37
* Nikon Coolpix P330

## Noise profiles:

* Canon EOS-M
* Olympus E-600 (from: Olympus E-30)
* Olympus E-620 (from: Olympus E-30)
* Samsung WB2000
* Sony A99v
* Panasonic DMC-G10 iso 100
* Nikon D60

## Bug fixes:

* 0 star rating working again
* LT: ctrl+d duplicates per default now
* Some fixes concerning locale handling
* double click on film strip jumps to image
* remember position in collections
* ctrl+k jumps to previous collection
* Blending parameters are preserved when module is deactivated
* In full-preview (alt-1) ratings and labels are only applied to image shown
* Various OpenCL fixes, e.g. compilation on Mac OS X
* libsquish compilation now optional
* dr: deactivate interpolation at 200% zoom

Enjoy the release!

(and as usual: [give feedback](/contact/), [report bugs](https://darktable.org/redmine/projects/darktable/issues), [read our blog](/blog/), try the [development branch](https://github.com/darktable-org/darktable/commits/master), go out and take photos...)
