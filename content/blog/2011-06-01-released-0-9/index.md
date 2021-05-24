---
author: dt
comments: true
date: 2011-06-01 22:08:28+00:00
layout: post
link: /2011/06/released-0-9/
slug: released-0-9
title: "released 0.9"
lede: bay.jpg
wordpress_id: 227
tags:
  - announcement
  - darktable release
---
we [released version 0.9](https://sourceforge.net/projects/darktable/files/darktable/0.9/darktable-0.9.tar.gz/download), with many new features:

* run-time switchable opencl to exploit all the power of your GPU whenever you decide to install the driver
* many new modules, including a spot removal tool, better denoising (on raw pixels and non-local means) and many more
* blend operations, overlay your module only 20 percent if you want
* spot removal tool
* low light vision tool
* non-local-means denoising (relatively fast for nlmeans, but still slow)
* first part of the google summer of code project already merged
* framing module (adds postcard borders to match given aspect ratio)
* tonemapping a lot faster now (probably the fastest high-dimensional bilateral filter available today)
* changed images come with the darktable|changed tag

more updates to the page/install instructions to come, but you should be good by just extracting the tarball and typing `./build.sh`. enjoy! and thanks to all our many contributors!
