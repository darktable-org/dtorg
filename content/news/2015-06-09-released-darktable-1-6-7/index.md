---
author: houz
comments: false
date: 2015-06-09 11:54:22+00:00
layout: post
link: /2015/06/released-darktable-1-6-7/
slug: released-darktable-1-6-7
title: released darktable 1.6.7
lede: town_hall_wide.jpg
lede_author: <a href="https://houz.org/">houz</a>
wordpress_id: 3697
tags:
  - announcement
  - darktable release
---
We are happy to announce that darktable 1.6.7 has been released.

The release notes and relevant downloads can be found attached to this git tag:
[ https://github.com/darktable-org/darktable/releases/tag/release-1.6.7](https://github.com/darktable-org/darktable/releases/tag/release-1.6.7)
Please only use our provided packages ("darktable-1.6.7.*" tar.xz and dmg) not the auto-created tarballs from github ("Source code", zip and tar.gz). The latter are just git snapshots and will not work! Here are the direct links to tar.xz and dmg:
[ https://github.com/darktable-org/darktable/releases/download/release-1.6.7/darktable-1.6.7.tar.xz](https://github.com/darktable-org/darktable/releases/download/release-1.6.7/darktable-1.6.7.tar.xz)
[https://github.com/darktable-org/darktable/releases/download/release-1.6.7/darktable-1.6.7.dmg](https://github.com/darktable-org/darktable/releases/download/release-1.6.7/darktable-1.6.7.dmg)

this is another point release in the stable 1.6.x series.

    sha256sum darktable-1.6.7.tar.xz
    a75073b49df0a30cd2686624feeb6210bc083bc37112ae6e045f8523db4c4c98
    sha256sum darktable-1.6.7.dmg
    6630230049e6d2c4cdfd39585f95fbd1ee439a8dad107f7332aefeb1dd75b831

## security

* libraw [CVE-2015-3885](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3885): fix integer overflow in ljpeg_start()

## miscellaneous

* improvements to facebook export
* interpolation fixups
* demosaic code cleanups
* slideshow should handle very small images better
* improve Olympus lens detection
* various minor memory leak fixes
* various other fixes
* Pentax (K-x) DNG old embedded preview left over is now removed
* modern OSX display profile handling

## camera support

* Nikon D7200 (both 12bit and 14bit compressed NEFs)
* Nikon Coolpix P340
* Canon EOS 750D
* Canon EOS 760D
* Canon EOS M2
* Panasonic DMC-CM1
* Panasonic DMC-GF7 (4:3 only)
* Olympus XZ-10
* Olympus SP570UZ
* Samsung NX500
* Fuji F600EXR

## aspect ratios

* Pansonic DMC-G5
* Panasonic DMC-GM5
* Panasonic FZ200

## white balance presets

* Nikon D7200
* Nikon Coolpix P340
* Panasonic DMC-GM1
* Panasonic DMC-GM5
* Olympus E-M10 (updated)
* Olympus E-PL7
* Olympus XZ-10

## noise profiles

* Canon Powershot G9
* Sony A350

## basecurves

* Nikon D7200
* Nikon D7000
* Nikon D750
* Nikon D90

## translations

* Catalan
* German
* Spanish
* Swedish
