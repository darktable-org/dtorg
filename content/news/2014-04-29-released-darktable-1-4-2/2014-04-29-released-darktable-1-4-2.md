author: houz
comments: true
date: 2014-04-29 11:54:47+00:00
layout: post
link: http://www.darktable.org/2014/04/released-darktable-1-4-2/
slug: released-darktable-1-4-2
title: released darktable 1.4.2
lede: dt_shirt_text_wide.jpg
wordpress_id: 3278
tags: announcement, darktable release

Hello everyone,

we released darktable 1.4.2, a point release which consists mostly of bugfixes and newly added camera support.

You can find the source tarball here:

[http://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.2.tar.xz/download](http://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.2.tar.xz/download)

The PGP signature:

[http://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.2.tar.xz.asc/download](http://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.2.tar.xz.asc/download)

The disk image for Mac users:

[http://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.2.dmg/download](http://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.2.dmg/download)

And this one is also signed:

[http://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.2.dmg.asc/download](http://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.2.dmg.asc/download)

The key can be obtained from the usual key servers, fingerprint being 4BFF7EAD.

The release notes are as follows:

========================



## darktable 1.4.2 Release Notes







  * A lot of cleanup was done to allow larger images to be handled by darktable
without crashing as often


  * A significant effort has been made to cleanup some of our code, fixing a lot of
minor memory leaks and some corner case bugs in the process


  * A bunch of masks corner cases fixed


  * Tonecurve no longer clamps the gamut


  * Assorted TIFF reader/writer fixes


  * Map view: only connect to the map server when active


  * Use filesystem timestamp for images lacking EXIF


  * Sync AMAZE code from RawTherapee, now with SSE2 optimization, so it's less
slow


  * Olympus: lens detection for some Olympus cameras should work better now
(requires images to be re-imported)


  * Olympus: focus distance should now be properly displayed for some Olympus
cameras (requires images to be re-imported)


  * SONY ILCE-7(R) garbage pixels are now cut off


  * Experimental support for Nikon D5300


  * Experimental support for Nikon D3300


  * Experimental support for Samsung NX1100


  * Experimental support for Samsung NX30


  * Very experimental support for Olympus E-M10 (color rendering is still
subject to future change, and may retroactively affect your image library for
this camera)


  * New white balance presets for:


    * Nikon D610


    * Olympus E-PL5


    * Olympus E-PM2





For Ubuntu users

Users who are using our darktable-release-plus PPA (which has been deprecated
since the previous release) should switch to our darktable-release PPA:
[https://launchpad.net/~pmjdebruijn/+archive/darktable-release](https://launchpad.net/~pmjdebruijn/+archive/darktable-release)

1.4.2 is the last release that will be supported for older Ubuntu versions.
All future versions of darktable will only be supported for 14.04 “Trusty”
(the new Long Term Support release) and onward

========================

Enjoy and take a lot of photos!
