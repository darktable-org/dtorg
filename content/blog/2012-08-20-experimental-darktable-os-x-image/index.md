---
author: smn
comments: true
date: 2012-08-20 21:33:34+00:00
layout: post
link: /2012/08/experimental-darktable-os-x-image/
slug: experimental-darktable-os-x-image
title: "Experimental darktable OS X image"
wordpress_lede: spider.jpg
wordpress_id: 1959
tags:
  - announcement
  - darktable release
---
After the progress reported in the [latest blog post](/blog/2012-08-14-bringing-current-darktable-to-os-x/2012-08-14-bringing-current-darktable-to-os-x.md) on the OS X port of darktable we now have something new for the Mac users:

[parafin]({author}parafin) just released an experimental DMG image of darktable!

Please be aware of this being an experimental OS X build as well as experimental software in general&nbsp;– it's based on the latest development version of darktable that will be darktable 1.1 someday in the future.

You can grab the file from here:

[https://sourceforge.net/projects/darktable/files/darktable/](https://sourceforge.net/projects/darktable/files/darktable/) (look for the most recent .dmg file)

Just as a reminder (see the blog post for more information): There's an issue with gphoto on OS X, which prevents a plugged-in camera from appearing in darktable. To fix it simply run `killall PTPCamera` command after connecting the camera.

Please report back any issues you have with it to help improving this software. Use our bug tracker for reporting, that makes it easier for us to keep track of your problems: [file new bug](https://darktable.org/redmine/projects/darktable/issues/new)

Enjoy it!

Edit: disk image updated to support older than Mountain Lion OS X versions (but at least as new as Snow Leopard).
