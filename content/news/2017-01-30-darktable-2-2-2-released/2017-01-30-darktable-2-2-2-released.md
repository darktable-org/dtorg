author: houz
comments: true
date: 2017-01-30 09:49:52+00:00
layout: post
link: http://www.darktable.org/2017/01/darktable-2-2-2-released/
slug: darktable-2-2-2-released
title: darktable 2.2.2 released
lede: pygmy_chameleon_wide.jpg
lede_author: <a href="https://www.flickr.com/photos/andabata">Kees Guequierre</a>
wordpress_id: 4727
tags: announcement, darktable release

we're proud to announce the second bugfix release for the 2.2 series of darktable, 2.2.2!

the github release is here: [https://github.com/darktable-org/darktable/releases/tag/release-2.2.2](https://github.com/darktable-org/darktable/releases/tag/release-2.2.2).

as always, please don't use the autogenerated tarball provided by github, but only our tar.xz. the checksum is:

    766d7d734e7bd5a33f6a6932a43b15cc88435c64ad9a0b20410ba5b4706941c2 darktable-2.2.2.tar.xz
    52fd0e9a8bb74c82abdc9a88d4c369ef181ef7fe2b946723c5706d7278ff2dfb darktable-2.2.2.dmg

**Important note: to make sure that darktable can keep on supporting the raw file format for your camera, please help us by visiting [https://raw.pixls.us/](https://raw.pixls.us/) and making sure that we have the full raw sample set for your camera under CC0 license!**

and the changelog as compared to 2.2.1 can be found below.

## New features:

* color look up table module: include preset for helmholtz/kohlrausch monochrome
* Lens module: re-enable tiling
* Darkroom: fix some artefacts in the preview image (not the main view!)
* DNG decoder: support reading one more white balance encoding method
* Mac: display an error when too old OS version is detected
* Some documentation and tooltips updates

## Bugfixes:

* Main view no longer grabs focus when mouse enters it. Prevents accidental catastrophic image rating loss.
* OSX: fix bauhaus slider popup keyboard input
* Don't write all XMP when detaching tag
* OSX: don't do PPD autodetection, gtk did their thing again.
* Don't show database lock popup when DBUS is used to start darktable
* Actually delete duplicate's XMP when deleting duplicated image
* Ignore UTF-8 BOM in GPX files
* Fix import of LR custom tone-curve
* Overwrite Xmp rating from raw when exporting
* Some memory leak fixes
* Lua: sync XMPs after some tag manipulations
* Explicitly link against math library

## Base Support:

* Canon PowerShot SX40 HS (dng)
* Fujifilm X-E2S
* Leica D-LUX (Typ 109) (4:3, 3:2, 16:9, 1:1)
* Leica X2 (dng)
* Nikon LS-5000 (dng)
* Nokia Lumia 1020 (dng)
* Panasonic DMC-GF6 (16:9, 3:2, 1:1)
* Pentax K-5 (dng)
* Pentax K-r (dng)
* Pentax K10D (dng)
* Sony ILCE-6500

## Noise Profiles:

* Fujifilm X-M1
* Leica X2
* Nikon Coolpix A
* Panasonic DMC-G8
* Panasonic DMC-G80
* Panasonic DMC-G81
* Panasonic DMC-G85