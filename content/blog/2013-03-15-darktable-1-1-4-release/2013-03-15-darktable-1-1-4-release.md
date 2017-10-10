author: pmjdebruijn
comments: true
date: 2013-03-15 18:02:27+00:00
layout: post
link: http://www.darktable.org/2013/03/darktable-1-1-4-release/
slug: darktable-1-1-4-release
title: darktable 1.1.4 release
wordpress_id: 2793
tags: announcement, darktable release

Hi,

there is a new point release with a couple of smaller updates. The source tarball and OSX image can be found here:

[https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.4.tar.xz/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.4.tar.xz/download)

[https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.4.dmg/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.4.dmg/download)

And the usermanual is still the same.

## Fixes:

* keep the styles plugin usable after applying a style
* darktable should now be better able to import some of the data from .xmp's from other applications
* better redraw logic in darkroom mode
* it should be less likely to get blurry thumbnails in lighttable mode now
* on low end system use lower quality thumbnails
* work around some malformed icc profiles
* add a mandatory cprt tag to our embedded icc profiles
* prevent adobe rgb related trademark issue
* some fixes with regard to the colorpicker
* tooltips should now be more easily distinguisable
* fix build with new glib versions
* more assorted small fixes

## Added preliminary camera support:

* Nikon coolpix p7100 blackpoint fix
* Leica basecurve should apply to more camera models now
* Pentax k-5 ii (s)
* Nikon 1 j3
* Nikon 1 s1
* Improved panasonic dmc-g5 support
* Improved panasonic dmc-lx7 support

## Improved color rendition:

* Olympus e-m5 enhanced color matrix (frederic crozat)

## New white balance presets:

* Panasonic dmc-g5 (thouks)
* pentax k-5 ii (s) (jack bowling)
* sony slt-a77v
* nikon d3200
* nikon d800 update (wolfgang goetz)

darktable wouldn't be where it is now if we weren't able to depend on the great work of others, in particular we'd like to thank:

klaus post (rawspeed), dave coffin (dcraw), andreas hugel (exiv2), andrew zabolotny (lensfun), marti maria (lcms), niels kristian bech jensen (ufraw).
