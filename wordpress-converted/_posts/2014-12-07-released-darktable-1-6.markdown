---
author: jcsogo
comments: true
date: 2014-12-07 21:58:59+00:00
layout: post
link: http://www.darktable.org/2014/12/released-darktable-1-6/
slug: released-darktable-1-6
title: Released darktable 1.6
wordpress_id: 3445
categories:
- announcement
- darktable release
- news
tags:
- '1.6'
- announcement
- darktable
- release
---

We are happy to announce that almost after one year darktable 1.6 has just been released.

The release notes and relevant downloads can be found attached to this git tag:
[https://github.com/darktable-org/darktable/releases/tag/release-1.6.0](https://github.com/darktable-org/darktable/releases/tag/release-1.6.0)
Please only use our provided packages (green buttons tar.xz and dmg) not the auto-created tarballs from github (grey buttons, zip and tar.gz). The latter are just git snapshots and will not work! Here's the direct link to tar.xz:
[https://github.com/darktable-org/darktable/releases/download/release-1.6.0/darktable-1.6.0.tar.xz](https://github.com/darktable-org/darktable/releases/download/release-1.6.0/darktable-1.6.0.tar.xz)

If you are using any distribution's packages, please be patient for the packager to catch up and provide the relevant updates.

Thanks to our great community and all the contributors for making this possible!
See the development visualised: [https://www.youtube.com/watch?v=N-ST2PDcDUg](https://www.youtube.com/watch?v=N-ST2PDcDUg)

Enjoy the release!


## **New features:**




### **general/misc:**





	
  * high DPI monitor support

	
  * signed OSX packages

	
  * map view now allows to only show images from the current collection on the map

	
  * slideshow

	
  * darktable-cli now works without a running X server for use on headless systems

	
  * support for audio notes playback

	
  * sticky preview

	
  * added the option to overwrite files when exporting to disk

	
  * crawler that syncs all xmp files on start

	
  * support huge images (> 32 bit pixel index). darktable can open 26770x13385 TIFFs and should in theory be able to process arbitrary sized images. don't try this on a 32 bit system though!

	
  * lens iop presets are copy/pastable between different images




### **output:**





	
  * tiff read/write rewritten, works on 32-bit float now, supports compression

	
  * allow setting PPI for exported JPEGs, defaulting to 300

	
  * pwstorage libsecret

	
  * use HTTPS when exporting to flickr




### **darkroom:**





	
  * new defringe image operation

	
  * automatic mode for levels module

	
  * allow to disable white balance

	
  * new colour reconstruction mode for highlight recovery that tries to add both colour and structure to clipped areas. thanks to a1ex from magic lantern!

	
  * better basecurve tool to create basecurves from raw/jpg pairs

	
  * soft boundaries in sliders (right click and type 8 in exposure compensation for example)

	
  * input colour gamut mapping to avoid problems with saturated blues causing purple artefacts




### **colour:**





	
  * color conversion speedup (openmp for lcms2 case)

	
  * add linear Rec2020 as a build-in profile

	
  * embedded icc profile support for png/tiff (read/write)




### **lua scripting:**





	
  * copy, move, reset and delete images via lua

	
  * handle progress bars via lua

	
  * limited manipulation of libs an views UI via lua

	
  * import and export styles via lua

	
  * trigger lua when the grouping mode changes

	
  * trigger lua when the overlay mode changes

	
  * trigger lua when the active view changes

	
  * manipulate snapshots via lua

	
  * handle more types of preferences, including enums, directories and file names

	
  * lua API is now versioned: use darktable.configuration.check_version to check

	
  * lua API incompatibilities: darktable.modules has been removed, use darktable.new_format and darktable.new_storage to access the constructors




### **performance improvements:**





	
  * many speed improvements by adding sse code for image operations

	
  * make white balance work faster

	
  * make invert work faster

	
  * much faster exr export with optional compression (multicore support)

	
  * speedup of pfm writing

	
  * speedup of amaze. it is still slow but not as bad as it used to be




### **internal improvements:**





	
  * module parameter introspection

	
  * clang/address-sanitizer/etc compiler warnings fixed

	
  * flip iop used for raw auto-orientation (simplifies code)

	
  * complete rawspeed migration for raw loading




### **bug fixes:**





	
  * hdr bracketing fixes

	
  * masks cleanup and bugfixes

	
  * correct lens detection for compact cameras

	
  * avoid clipping in vignette, lowpass, shadows & highlights, a/b channels of colorcontrast and tonecurve




### **new cameras supported!**





	
  * initial support for x-trans sensors

	
  * new demosaicing algorithms: markesteijn for x-trans and vng for x-trans and regular bayer raws

	
  * There is support for several dozens of new cameras, and loads of new noise profiles for denoising have been added. Check out the full list in the release notes on github.




### **and of course also:**





	
  * updated usermanual

	
  * lots of small performance improvements and code cleanup


