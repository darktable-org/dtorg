---
author: smn
comments: true
date: 2013-09-13 12:19:52+00:00
layout: post
link: http://www.darktable.org/2013/09/released-darktable-1-2-3/
slug: released-darktable-1-2-3
title: released darktable 1.2.3
wordpress_id: 3014
categories:
- darktable release
- news
---

Dear all,

we just released another patch version for the stable branch 1.2. As usual you can find the source tarball here:



	
  * [source tarball](https://sourceforge.net/projects/darktable/files/darktable/1.2/darktable-1.2.3.tar.xz/download)

	
  * The [Ubuntu PPA](https://launchpad.net/~pmjdebruijn/+archive/darktable-release) has already been updated by Pascal (thanks!),

	
  * [OS X disk image](https://sourceforge.net/projects/darktable/files/darktable/1.2/darktable-1.2.3.dmg/download)

	
  * builds for other distributions will hit the respective repositories soon



We collected the following goodies for you:

	
  * Update to RawSpeed r570

	
  * Canon 70D (preliminary)

	
  * Olympus E-P5 (incl. preliminary Adobe Coeff.)

	
  * Samsung NX2000

	
  * Sony RX100m2

	
  * Sony SLT-A58 (updated)


White Balance Presets:

	
  * Sony NEX-5R

	
  * Sony SLT-A58

	
  * Nikon D3200 (updated)

	
  * Pentax K20D


Enhanced Color Matrix:

	
  * Pentax K20D


Noise Profiles:

	
  * Canon EOS 1100D == Canon EOS Rebel T3

	
  * Canon PowerShot S95

	
  * Canon PowerShot G11

	
  * Nikon Coolpix P330

	
  * Sony A580

	
  * Fuji X10

	
  * Pentax K20D


Fixes and improvements:

	
  * Increased maximum cache size to 8GB

	
  * OS X: fix Facebook uploads

	
  * Adjustments to default lowpass blur settings

	
  * Adjustments to dithering slider ranges

	
  * Metadata viewer: fix display of focal length: indicate unit and hide if invalid.

	
  * Chromatic Aberrations: fix segfault for small buffers

	
  * Color pickers: fix various issues, e.g. #9482

	
  * More guides for Crop & Rotate

	
  * Improve light table usability: when viewing images in fullscreen wrap around at line end when pressing right arrow key

	
  * Soften: massive speed improvements by using SSE and OpenMP

	
  * Deleting images from camera is not supported anymore for safety.

	
  * Exposure module now supports multiple instances

	
  * Support for custom meta data burn in (see commit 6ac7ba055440aa27f79f0a67ac112799a0e7785e)

	
  * OpenCL support for nVidia GeForce GT330

	
  * PFM: load timestamp as date & time taken.

	
  * Fix bug prohibiting image rating by mouse

	
  * Update Picasa uploader: references Google+ now

	
  * Some fixes for memory leaks, deadlocks, background jobs

	
  * Fixes of on-screen handles for Crop&Rotate; and GND modules

	
  * 0 bytes files will no longer be imported but ignored



As usual: enjoy the release!
(and: [give feedback](http://www.darktable.org/contact/), [report bugs](http://darktable.org/redmine/projects/darktable/issues), [read our blog](http://www.darktable.org/category/blog/), try the [development branch](https://github.com/darktable-org/darktable/commits/master), go out and take photos...)

This might be the last point release of the darktable 1.2 stable branch. Prepare yourselves for some major improvements and new features...
