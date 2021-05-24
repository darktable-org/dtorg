---
author: smn
comments: true
date: 2015-04-08 16:06:26+00:00
layout: post
link: /2015/04/released-darktable-1-6-4/
slug: released-darktable-1-6-4
title: released darktable 1.6.4
lede: thumb.jpg
wordpress_id: 3644
tags:
  - darktable release
---
We are happy to announce that darktable 1.6.4 has been released.

The release notes and relevant downloads can be found attached to this git tag:
[https://github.com/darktable-org/darktable/releases/tag/release-1.6.4](https://github.com/darktable-org/darktable/releases/tag/release-1.6.4)
Please only use our provided packages ("darktable-1.6.4.*" tar.xz and dmg) not the auto-created tarballs from github ("Source code", zip and tar.gz). The latter are just git snapshots and will not work! Here's the direct link to tar.xz and dmg:
[https://github.com/darktable-org/darktable/releases/download/release-1.6.4/darktable-1.6.4.tar.xz](https://github.com/darktable-org/darktable/releases/download/release-1.6.4/darktable-1.6.4.tar.xz)
[https://github.com/darktable-org/darktable/releases/download/release-1.6.4/darktable-1.6.4.dmg](https://github.com/darktable-org/darktable/releases/download/release-1.6.4/darktable-1.6.4.dmg)

this is another point release in the stable 1.6.x series.

    sha256sum darktable-1.6.4.tar.xz
     c5f705e8164c014acf0dac2ffc5b730362068c2864622121ca6fa9f330368d2a
    sha256sum darktable-1.6.4.dmg
     e5bbf00fefcf116aec0e66d1d0cf2e2396cb0b19107402d2ef70d1fa0ab375f6

## General improvements:

* major rawspeed update
* facebook exporter update (first authentication usability should be much better now)
* first run opencl benchmark to prevent opencl auto-activation if GPU is obviously slower than CPU
* lensfun cornercase fixes
* some mask cornercase fixes
* zonesystem now updates it's gui when number of zones changes
* spots iop updates
* ui_last/gui_language should work more reliably now
* internal lua updated from 5.2.3 to 5.2.4 (distro typically use their own version of lua)
* gcc 5 should build now

## Camera support:

* Canon Digital Rebel (non-european 300D)
* Nikon D5500 (experimental)
* Olympus E-M5 Mark II (experimental)
* Samsung NX500 (experimental)

## White balance presets:

* Sony A77 II
* Fujifilm X-E2
* Olympus E-M5 Mark II

## Noise profiles:

* Canon 7D Mark II

## updated translations:

* German
* French
* Russian
* Danish
* Catalan
* Japanese
* Dutch


