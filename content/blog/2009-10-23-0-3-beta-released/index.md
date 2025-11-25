---
author: dt
comments: true
date: 2009-10-23 22:02:30+00:00
layout: post
link: /2009/10/0-3-beta-released/
slug: 0-3-beta-released
title: "0.3 beta released"
lede: crowrock.jpg
wordpress_id: 207
tags:
  - announcement
  - darktable release
---
there have been some major internal changes in dt since 0.2, and some of them result in cool new features for the user, so it is time to pass it on to the non-git audience. this includes:

* most processing is now being done in a new color space (L a/L b/L). this results in nicer exposure/tonecurve/denoise/color correction results.
* the pixel pipeline is now free to change dimensions of the image, which makes a crop/rotate operation (and lensfun in the future) possible.
* the code is now organised as modules (image operations and views such as lighttable and darkroom).
* the lighttable view can filter and sort by rating.
* color management using lcms.
