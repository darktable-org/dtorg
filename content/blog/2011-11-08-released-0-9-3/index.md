---
author: jo
comments: true
date: 2011-11-08 09:30:29+00:00
layout: post
link: /2011/11/released-0-9-3/
slug: released-0-9-3
title: "Released 0.9.3"
wordpress_lede: img_0001_23.jpg
wordpress_id: 941
tags:
  - darktable release
  - bugfixes
  - darktable
  - release
---
As most of you probably noticed by now, we released 0.9.3. The tar file can be found here:
[https://sourceforge.net/projects/darktable/files/darktable/0.9/darktable-0.9.3.tar.gz/download](https://sourceforge.net/projects/darktable/files/darktable/0.9/darktable-0.9.3.tar.gz/download)

Pascal updated his ppa for ubuntu here:
[https://launchpad.net/~pmjdebruijn/+archive/darktable-release](https://launchpad.net/~pmjdebruijn/+archive/darktable-release) or
[https://launchpad.net/~pmjdebruijn/+archive/darktable-release-plus](https://launchpad.net/~pmjdebruijn/+archive/darktable-release-plus) (with Exiv2 0.22, and Lensfun 0.2.5 + lens data from svn).

and made great new screencasts explaining a couple of features and differences to 0.9.2. You can find them on our [resources page](/resources/resources/) or [Pascal's website](https://encrypted.pcode.nl/blog/2011/11/05/darktable-0-9-screencast-library-addition/)

It is a comparatively minor update to our stable 0.9.x series. It does not contain many very cool new features and big changes we have in git, because we don't consider them stable enough yet. Nontheless, it contains 272 commits over the previous release 0.9.2, mainly containing:

## sse optimizations

* non-local means
* graduated density
* velvia
* color management
* equalizer
* zone system

## updated translations

* ru,fr,es,ja,it,sq,pl,nl,de

## more presets

* split toning
* tone curve
* equalizer
* color zones

## lots of bugfixes

* tiling code (low mem/opencl)
* gcc 4.6 compat
* ...

## updates

* libraw 0.13.8
* rawspeed r379

As well as more basecurves and color matrices.

I'd also like to take the opportunity to point out we have now an awesome new webpage:

[https://www.darktable.org](https://www.darktable.org/)

and thank _smn and PolarFox for that!

As always, cheers to everyone who helped make this possible. dt has become huge! this would never be possible for three or five people alone.
