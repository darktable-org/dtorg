---
author: dt
comments: true
date: 2009-07-06 22:00:19+00:00
layout: post
link: /2009/07/0-2-beta-is-out/
slug: 0-2-beta-is-out
title: "0.2 beta is out!"
lede: release_0.2.jpg
wordpress_id: 200
tags:
  - darktable release
---
there have been some major changes in the last months. first, the processing backend has been replaced completely, based on an interface which is able to use libgegl (but currently doesn't, until gegl is fast enough). all operations are encapsulated in run-time loaded plug-ins. raw reading is now based on libraw-0.8. the lighttable got a slightly different look, and more image operations have been implemented (e.g. luma/chroma denoising).
this release is still marked _beta_, which should indicate that not all features are yet in (especially some lighttable related tasks such as filtering, sorting etc.), and not everything will work bug-free and stable yet.
