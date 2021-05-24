---
author: smn
comments: true
date: 2013-12-26 14:25:12+00:00
layout: post
link: /2013/12/released-darktable-1-4/
slug: released-darktable-1-4
title: released darktable 1.4
lede: dt_wide.png
lede_author: <a href="https://houz.org/">houz</a>
wordpress_id: 3181
tags:
  - announcement
  - darktable release
---
merry christmas!

we've got a new release for you:

[https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.tar.xz/download](https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.tar.xz/download)

since we have quite a lot of new features (masks etc, see below), there is an updated usermanual:

[https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-usermanual.pdf/download](https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-usermanual.pdf/download)

ubuntu packages are already available in the usual place, and there is a new macintosh disk image:

[https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.dmg/download](https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4.dmg/download)

## more detailed release notes:

* darktable now [integrates a lua engine](/blog/2013-09-24-using-lua-with-darktable/2013-09-24-using-lua-with-darktable.md) that allows writing scripts to make it easier to use with other image processing software. These scripts can be run when a particular event takes place (for example when a new image is imported) or when a particular keyboard shortcut is used. There are very few scripts available at this point but we expect the community to provide some more during the next release cycle.
* darktable now [includes several kinds of drawn masks](/blog/2013-04-19-masks/2013-04-19-masks.md): brush, circle, ellipse, path and gradients
* exporting in WebP format
* serious speed enhancements of lighttable when using large colections
* [focus detection on lighttable](/blog/2013-11-01-determining-focus-in-lighttable/2013-11-01-determining-focus-in-lighttable.md)
* local cached copies of images for offline files
* a few new blend mode like "HSV lightness", "HSV color", "Lab lightness" and "Lab color"
* new modules "contrast brightness saturation", "color balance" and "color mapping" which replaces the now deprecated "color transfer" module
* [new histogram mode "waveform"](/blog/2013-12-06-of-histograms-and-waveforms/2013-12-06-of-histograms-and-waveforms.md)
* added a setting to automatically collapse modules to only have a single one expanded
* better user experience for bauhaus sliders: the popup now has a blinking cursor to make possible text entry more discoverable
* the text entry for bauhaus sliders and vimkeys' `:set` command can now evaluate mathematical expressions
* additional logarithmic mode for editing the basecurve
* many bug fixes and small improvements
* [a tool for measuring basecurves from a sample image](/blog/2013-10-28-about-basecurves/2013-10-28-about-basecurves.md)
* a tool to check the system's color management setup. call cmake with -DBUILD_CMSTEST=On to build and install it. packagers probably want that.
* updated usermanual
* darktable now requires Gtk+ in version >= 2.24, Glib in version >= 2.30

# known bugs

* Ricoh Pentax K-3 PEFs aren't supported yet (DNGs work fine)
* Nikon D5300 isn't supported yet

hope you have a couple of days off to enjoy the release!
