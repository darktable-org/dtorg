author: smn
comments: true
date: 2013-12-02 09:50:21+00:00
layout: post
link: http://www.darktable.org/2013/12/darktable-1-4-release-candidate/
slug: darktable-1-4-release-candidate
title: darktable 1.4 release candidate
wordpress_id: 3133
tags: announcement, darktable

We just packaged darktable 1.4rc1 for more testing before releasing 1.4 proper in a few weeks. We've got tarballs,


[https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4~rc1.tar.xz/download](https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4~rc1.tar.xz/download)


debian packages,


[http://packages.debian.org/experimental/darktable](http://packages.debian.org/experimental/darktable)


a Macintosh DMG,


[https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4~rc1.dmg/download](https://sourceforge.net/projects/darktable/files/darktable/1.4/darktable-1.4~rc1.dmg/download)


and Pascal's Ubuntu darktable Unstable PPA has been updated, too:


[https://launchpad.net/~pmjdebruijn/+archive/darktable-unstable](https://launchpad.net/~pmjdebruijn/+archive/darktable-unstable)



Preliminary release notes are (also see RELEASE_NOTES in git/tarball):






	
  * darktable now integrates a lua engine that allows writing scripts to make it easier to use with other image processing software. These scripts can be run when a particular event takes place (for example when a new image is imported) or when a particular keyboard shortcut is used. There are very few scripts available at this point but we expect the community to provide some more during the next release cycle.

	
  * darktable now include several kinds of drawn masks: brush, circle, ellipse, path and gradients

	
  * exporting in WebP format

	
  * serious speed enhancements of lighttable when using large collections

	
  * focus detection on lighttable

	
  * local cached copies of images for offline files

	
  * a few new blend mode like "HSV lightness", "HSV color", "Lab lightness" and "Lab color"

	
  * new modules "contrast brightness saturation", "color balance" and "color mapping" which replaces the now deprecated "color transfer" module

	
  * new histogram mode "waveform"

	
  * added a setting to automatically collapse modules to only have a single one expanded

	
  * better user experience for bauhaus sliders: the popup now has a blinking cursor to make possible text entry more discoverable

	
  * the text entry for bauhaus sliders and vimkeys' ":set" command can now evaluate mathematical expressions

	
  * many bug fixes and small improvements

	
  * a tool for measuring basecurves from a sample image

	
  * updated usermanual

	
  * darktable now requires Gtk+ in version >= 2.24, Glib in version >= 2.30





Thanks to everybody helping out! please double check your credits in the about dialog and the AUTHORS file and give us a shout if you're missing.





This is still a testing version, so please report all bugs you find to our bug tracker [http://darktable.org/redmine/projects/darktable/issues](http://darktable.org/redmine/projects/darktable/issues) so we can take care of them and make the release an outstanding one.





Hope you enjoy the release!
