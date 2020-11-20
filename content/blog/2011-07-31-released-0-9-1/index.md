---
author: dt
comments: true
date: 2011-07-31 22:09:17+00:00
layout: post
link: /2011/07/released-0-9-1/
slug: released-0-9-1
title: "released 0.9.1"
wordpress_lede: leaves.jpg
wordpress_id: 231
tags:
  - announcement
  - darktable release
---
we [released version 0.9.1](https://sourceforge.net/projects/darktable/files/darktable/0.9/darktable-0.9.1.tar.gz/download), with a few bugfixes on top of release 0.9. and 184 patches, among them

* new rawspeed, dcraw, libraw
* fixed various segfaults and deadlocks
* the pipeline is now more real HDR (unbounded color management, no more gamut clipping in between)
* fixed a nasty bug which could cause complete loss of history for an image
* darktable-faster now plays nicely with darktablerc (non-gconf)
* lots of opencl improvements
* updated translations
* second part of our GSoC: customizable keyboard shortcuts!

check the [installation instructions](/install/) for more infos!

as always, thanks to our awesome community! you all make this possible, especially when our core devs have little time. this is one of a couple of stable releases we plan to do before publishing cool new features in our unstable development branches, so there is more to come soon.

enjoy, and let us know if you run into any issues!
