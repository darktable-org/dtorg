author: houz
comments: true
date: 2015-03-04 10:38:35+00:00
layout: post
link: http://www.darktable.org/2015/03/released-darktable-1-6-3/
slug: released-darktable-1-6-3
title: released darktable 1.6.3
lede: speicherstadt_wide.jpg
wordpress_id: 3570
tags: announcement, darktable release

We are happy to announce that darktable 1.6.3 has been released.

The release notes and relevant downloads can be found attached to this git tag:

[https://github.com/darktable-org/darktable/releases/tag/release-1.6.3](https://github.com/darktable-org/darktable/releases/tag/release-1.6.3)

Please only use our provided packages ("darktable-1.6.3.*" tar.xz and dmg) not the auto-created tarballs from github ("Source code", zip and tar.gz). The latter are just git snapshots and will not work! Here's the direct link to tar.xz:

[https://github.com/darktable-org/darktable/releases/download/release-1.6.3/darktable-1.6.3.tar.xz](https://github.com/darktable-org/darktable/releases/download/release-1.6.3/darktable-1.6.3.tar.xz)

and the DMG:

[https://github.com/darktable-org/darktable/releases/download/release-1.6.3/darktable-1.6.3.dmg](https://github.com/darktable-org/darktable/releases/download/release-1.6.3/darktable-1.6.3.dmg)

this is another point release in the stable 1.6.x series.

    sha256sum darktable-1.6.3.tar.xz
    852bb3d307b0e2b579d14cc162b347ba1193f7bc9809bb283f0485dfd22ff28d

    sha256sum darktable-1.6.3.dmg
    be568ad20bfb75aed703e2e4d0287b27464dfed1e70ef2c17418de7cc631510f

## Changes

* Make camera import window transient
* Allow soft limits on radius
* Fix soft boundaries for black in exposure
* Change order of the profile/intent combo in export dialog
* Support read/write of chromaticities in EXR
* Allow to default to :memory: db in config
* Add mime handler for non-raw image file formats
* Improved lens model name detection for Sony SAL lenses

## Bug fixes

* Fix buffer overrun in SSE clipping loop for highlight handling
* Prevent exporting when an invalid export/storage is selected
* Hopefully last fix for aspect ratios in crop and rotate ([#9942](https://darktable.org/redmine/issues/9942))
* No tooltip when dragging in monochrome ([#10319](https://darktable.org/redmine/issues/10319))

## Raw support

* Panasonic LX100 (missing non-standard aspect ratio modes)
* Panasonic TZ60
* Panasonic FZ1000
* KODAK EASYSHARE Z1015 IS
* Canon 1DX (missing sRAW modes)
* Canon A630 and SX110IS (CHDK raw)

## white balance presets

* Panasonic FZ1000
* Panasonic TZ60
* Panasonic LX100

## standard matrix

* Canon Rebel T3 (non-european 1100D)

## enhanced matrix

* nikon d750

## noise profiles

* Canon EOS 1DX
