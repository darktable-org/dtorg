author: pmjdebruijn
comments: true
date: 2012-07-01 13:45:16+00:00
layout: post
link: http://www.darktable.org/2012/07/fixed-darktable-crashing-unity/
slug: fixed-darktable-crashing-unity
title: 'Fixed: Darktable crashing Unity'
wordpress_lede: SAM_1890.jpg
wordpress_id: 1813
tags: announcement, ubuntu, unity

Some Ubuntu 12.04 (Precise) users who use Ubuntu's default Unity desktop environment may have noticed that it's commonplace for Unity to crash when closing Darktable. It so happens that Darktable is exposing a [bug in Unity](https://bugs.launchpad.net/ubuntu/+source/unity/+bug/851982), which got fixed upstream with a [one-liner patch](https://code.launchpad.net/~andyrock/unity/fix-851982/+merge/112440/+preview-diff/+files/preview.diff).

The above fix will be available in the next major update of Unity (5.14), but in the meanwhile I cherry picked the relevant patch to the current released version of Unity (5.12). The fixed version of Unity is available from a special temporary PPA:

[https://launchpad.net/~pmjdebruijn/+archive/unity-testing](https://launchpad.net/~pmjdebruijn/+archive/unity-testing)
