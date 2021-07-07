---
author: jo
comments: true
date: 2013-04-07 08:18:42+00:00
layout: post
link: /2013/04/released-1-2/
slug: released-1-2
title: "released 1.2"
lede: rimutaka.jpg
wordpress_id: 2839
tags:
  - announcement
  - darktable release
---
we released the next feature release (1.2):

[source tarball](https://sourceforge.net/projects/darktable/files/darktable/1.2/darktable-1.2.tar.xz/download)

[user manual](https://sourceforge.net/projects/darktable/files/darktable/1.2/darktable-usermanual.pdf/download)

[macintosh disk image](https://sourceforge.net/projects/darktable/files/darktable/1.2/darktable-1.2.dmg/download)

as a feature release, it comes with a lot of new goodies:

* [profiled denoising:](/blog/2012-12-11-profiling-sensor-and-photon-noise/2012-12-11-profiling-sensor-and-photon-noise.md) adapt to the properties of your camera's sensor (72 cameras already profiled for you).
* [lightroom import:](/blog/2013-02-02-importing-lightroom-development/2013-02-02-importing-lightroom-development.md) convert some basic edits from your lightroom collection to darktable operations.
* [multi instance support:](/blog/2013-02-15-multi-instances/2013-02-15-multi-instances.md) duplicate your modules and apply them more than one time with different settings.
* improved usability for distorting modules (streamline spot removal in the presence of crop/rotate for example).
* selective copy/paste of image processing.
* new more intuitive keystone correction tool.
* jpeg2000 support.
* graphics magick import (support virtually all input image formats).
* much faster thumbnail loading (if you can live with crappy embedded thumbnails).
* incredibly lengthy list of small bug fixes, performance enhancements, and usability improvements.
* new camera support (decode and color matrices).
* dithering against banding.
* sharper thumbnails in lighttable mode.
* new oauth2 based picasa uploader.
* updated translations.
* and a thoroughly overhauled user manual, proof read by natives (thanks heaps guys!).

this is the list of cameras supported for profiled denoising in this tarball:

* canon eos-1d mark iv
* canon eos-1ds mark ii
* canon eos 20d
* canon eos 30d
* canon eos 350d
* canon eos 400d
* canon eos 40d
* canon eos 450d
* canon eos 50d
* canon eos 550d
* canon eos 5d
* canon eos 5d mark ii
* canon eos 5d mark iii
* canon eos 600d
* canon eos 60d
* canon eos 650d
* canon eos 6d
* canon eos 7d
* canon eos rebel t1i
* canon eos rebel t3i
* canon eos rebel t4i
* canon powershot g10
* canon powershot g12
* canon powershot s90
* konica minolta dynax 5d
* nikon d200
* nikon d300
* nikon d300s
* nikon d3100
* nikon d5000
* nikon d5100
* nikon d600
* nikon d700
* nikon d7000
* nikon d80
* nikon d800
* nikon d800e
* nikon d90
* olympus e-30
* olympus e-400
* olympus e-420
* olympus e-m5
* olympus e-pl1
* olympus e-pl5
* olympus xz-1
* olympus xz-2
* panasonic dmc-fz18
* panasonic dmc-g2
* panasonic dmc-g3
* panasonic dmc-g5
* panasonic dmc-gf1
* panasonic dmc-gh2
* panasonic dmc-gx1
* pentax k100d
* pentax k10d
* pentax k200d
* pentax k-5
* pentax k-5 ii s
* pentax k-7
* pentax k-m
* pentax k-r
* pentax k-x
* samsung nx100
* sony dsc-rx100
* sony dslr-a200
* sony dslr-a230
* sony dslr-a550
* sony dslr-a700
* sony nex-3
* sony nex-5n
* sony nex-6
* sony nex-7
* sony nex-c3
* sony slt-a55v
* sony slt-a65v
* sony slt-a77v

these are all community contributed noise profiles, we're quite happy about this great response!

so string freeze is over! that means we'll have cool new stuff in git for you to check out soon :)

as always, thanks to everybody who made this possible. all the developers, translators, proof readers, battle testers and the guys who maintain the great libraries we depend on. you know who you are!
