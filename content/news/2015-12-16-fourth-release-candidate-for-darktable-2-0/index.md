---
author: houz
comments: true
date: 2015-12-16 18:26:23+00:00
layout: post
link: /2015/12/fourth-release-candidate-for-darktable-2-0/
slug: fourth-release-candidate-for-darktable-2-0
title: fourth release candidate for darktable 2.0
lede: sail_wide.jpg
lede_author: <a href="https://houz.org/">houz</a>
wordpress_id: 3903
tags:
  - announcement
  - darktable release
---
we're proud to announce the fourth and hopefully last release candidate in the new feature release of darktable, 2.0~rc4.

the release notes and relevant downloads can be found attached to this git tag:
[https://github.com/darktable-org/darktable/releases/tag/release-2.0rc4](https://github.com/darktable-org/darktable/releases/tag/release-2.0rc4)
please only use our provided packages ("darktable-2.0.rc4.*" tar.xz and dmg) not the auto-created tarballs from github ("Source code", zip and tar.gz). the latter are just git snapshots and will not work! here are the direct links to tar.xz and dmg:
[https://github.com/darktable-org/darktable/releases/download/release-2.0rc4/darktable-2.0.rc4.tar.xz](https://github.com/darktable-org/darktable/releases/download/release-2.0rc4/darktable-2.0.rc4.tar.xz)
[https://github.com/darktable-org/darktable/releases/download/release-2.0rc4/darktable-2.0.rc4.dmg](https://github.com/darktable-org/darktable/releases/download/release-2.0rc4/darktable-2.0.rc4.dmg)

the checksums are:

    $ sha256sum darktable-2.0~rc4.tar.xz
    79446397a837bc9c262706d91b99ee0cb3339e93e36ebcbc3a23a0af80d77509
    darktable-2.0~rc4.tar.xz
    $ sha256sum darktable-2.0~rc4.dmg
    14422e1569f94deb093e198895636b6e63982b9e9812c57e262fc42281d90bf5
    darktable-2.0~rc4.dmg

packages for individual platforms and distros will follow shortly.

the changes from rc3 include minor bugfixes, such as:

* translation updates
* an OpenCL bug fixed
* fixed a rare crash when leaving darkroom
* fixed a bug in gamut checking
* fixed a possible crash in lua garbage collection
* fixed a bug in rawspeed's sraw handling
* fixed a bug in circle masks
* allow toggling tethering zoom with 'z'
* don't make some modules too wide in some languages
* fixed high CPU load when hovering filmstrip
* fixed lighttable prefetching
* fixed thumbnail color management
* make tethered focusing for Canon cameras more robust wrt. libgphoto2 version
* some styling fixes
* fixed filmstrip width when duplicating images in darkroom
* scroll sidepanels when mouse is next to the window border
* speed up thumbnail color management using OpenMP
* fixed a few small memleaks
* fixed PDF exporter when compiled without Lua
* camera support improvements:

    * noiseprofiles:

        * add Olympus E-M5 Mark II
        * add Canon M3
        * add Fuji X30
        * add Sony RX10M2
        * add Panasonic GX8
        * add Sony A7RII

    * whitebalance:

        * Canon S110
        * Canon S100
        * Canon G1 X Mark II
        * Canon PowerShot G3 X
        * Canon PowerShot G16
        * Canon PowerShot G15
        * Canon PowerShot G1 X
        * Canon 1D Mark III
        * Canon 1Ds Mark III
        * Canon EOS M3
        * Panasonic GX8
        * Pentax *ist DL2
        * Sony NEX-F3
        * Sony SLT-A33
        * Sony NEX-5T
        * Sony NEX-3N
        * Sony A3000
        * Sony A5000
        * Sony A5100
        * Sony A500
        * Sony RX1R
        * Sony RX1
        * Sony DSLR-A580
        * Sony ILCE-6000
        * Sony ILCE-7S
        * Sony ILCE-7SM2
        * Sony SLT-A35

    * rawspeed fixes:

        * support all Panasonic GF7 crops
        * support all Panasonic FZ70/FZ72 crops
        * support FZ150 3:2 and fix 4:3 blackpoint
        * fixed whitebalance for Canon G3 X
        * whitebalance support for the Leaf Credo line
        * fixed Nikon D1 whitebalance
        * whitebalance support for Canon Pro1/G6/S60/S70
        * add another whitebalance mode for Canon D30
        * fixed whitebalance for Canon G3/G5/S45/S50
        * fixed whitebalance for Canon S90
        * support another Canon 350D alias
