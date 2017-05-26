---
author: smn
comments: true
date: 2014-11-16 20:35:36+00:00
layout: post
link: http://www.darktable.org/2014/11/release-candidate-for-darktable-1-6/
slug: release-candidate-for-darktable-1-6
title: Release Candidate for darktable 1.6
wordpress_id: 3421
categories:
- announcement
- darktable release
- news
---

We are happy to announce the first release candidate for the upcoming darktable 1.6.

In case you are wondering about the versioning scheme: we use odd numbers as development versions and even numbers for stable releases. This means the release candidate, tagged as "darktable-1.5.1", is an unstable development version – the final stable version will bear the tag "darktable-1.6.0".

Grab the tarball and OS X package from the github release page:
[https://github.com/darktable-org/darktable/releases/tag/release-1.5.1](https://github.com/darktable-org/darktable/releases/tag/release-1.5.1)

Concerning Pascal's Unstable PPA: only Ubuntu 14.04 (LTS) is supported, and there will be no support for future non-LTS releases. Of course the stable PPA will still serve all active Ubuntu versions starting at the most recent LTS.

And here are the preliminary release candidate release notes:


## New features:





	
  * initial support for x-trans sensors

	
  * input colour gamut mapping

	
  * slideshow

	
  * better basecurve tool to create basecurves from raw/jpg pairs

	
  * soft boundaries in sliders (right click and type 8 in exposure compensation for example)

	
  * support huge images (> 32 bit pixel index)

	
  * pwstorage libsecret

	
  * new defringe image operation

	
  * automatic levels

	
  * big exr export speedup (multicore support)

	
  * color conversion speedup (openmp for lcms2 case)

	
  * tiff read/write rewritten, works on 32-bit float now

	
  * embedded icc profile support for png/tiff (read/write)




## Internal improvements:





	
  * module parameter introspection

	
  * clang/address-sanitizer/etc compiler warnings fixed

	
  * flip iop used for raw auto-orientation (simplifies code)

	
  * libraw not used any more for a lot of file formats (faster loading via rawspeed now)




## Bug fixes:





	
  * hdr bracketing fixes

	
  * masks cleanup and bugfixes

	
  * lens iop presets are working

	
  * correct lens detection for compact cameras

	
  * updated usermanual

	
  * lots of performance improvements and code cleanup




## New camera support / new noise profiles


There is support for several dozens of new cameras, and loads of new noise profiles for denoising have been added. Check out the full list in the release notes on github.

We are still looking for aspect ratio mode samples for the following camera models:



	
  * Panasonic DMC-G1 [#10149](http://darktable.org/redmine/issues/10149)

	
  * Panasonic DMC-G3 [#10150](http://darktable.org/redmine/issues/10150)

	
  * Panasonic DMC-G5 [#10151](http://darktable.org/redmine/issues/10151)

	
  * Panasonic DMC-G10 [#10152](http://darktable.org/redmine/issues/10152)

	
  * Panasonic DMC-GF5 [#10154](http://darktable.org/redmine/issues/10154)

	
  * Panasonic DMC-GF6 [#10155](http://darktable.org/redmine/issues/10155)

	
  * Panasonic DMC-L1 [#10156](http://darktable.org/redmine/issues/10156)

	
  * Panasonic DMC-L10 [#10157](http://darktable.org/redmine/issues/10157)

	
  * Panasonic DMC-LF1 [#10158](http://darktable.org/redmine/issues/10158)

	
  * Panasonic DMC-LX2 [#10159](http://darktable.org/redmine/issues/10159)

	
  * Panasonic DMC-LX3 [#10160](http://darktable.org/redmine/issues/10160)

	
  * Panasonic DMC-LX5 [#10161](http://darktable.org/redmine/issues/10161)


Please give this some testing and let us know on FreeNode in #darktable or on the darktable-devel mailing list if there are remaining issues with it.

And as always, thanks to our great community and all the contributors for making this possible! enjoy the release!
