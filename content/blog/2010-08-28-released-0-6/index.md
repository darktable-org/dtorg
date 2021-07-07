---
author: dt
comments: true
date: 2010-08-28 22:05:31+00:00
layout: post
link: /2010/08/released-0-6/
slug: released-0-6
title: "released 0.6"
wordpress_lede: watt.jpg
wordpress_id: 217
tags:
  - announcement
  - darktable release
---
finally a new release ... it has been so long that i hardly remember all the changes. let's try to list the most important ones:

* libraw 0.10.0-beta3
* tethered shooting mode
* import from camera via gphoto2
* new, improved modules: vignetting, velvia, grain, denoise (via bilateral filter), color transfer, channel mixer ...
* crop/rotate: straighten tool, perspective correction, guide lines (ported from digikam)
* lots of new input color matrices and base curves
* openexr export
* database format changed, which greatly improves speed (and cuts down used disk memory)
* film strip view in darkroom mode for quick image switching
* cool alternative demosaicing algorithms (ported from rawtherapee): dcb, amaze, vcd, c/a autocorrection
* customizable preset system for all darkroom modules with auto application to matching images, selected by exif
* reworked export system to modularly support export to picasa webalbum, email, or disk in jpg, png, 8/16-tiff, pfm, exr, or 16-ppm.
* lots of performance enhancements (modules denoise and local contrast are still slow)
* translations: de es fi fr gl nl ru sv

as always, the release comes with a warning: it will be outdated horribly in very short time (even now git master has some really cool new features over the release tarball ...). thanks to all contributors, translators, and everyone on #darktable!
