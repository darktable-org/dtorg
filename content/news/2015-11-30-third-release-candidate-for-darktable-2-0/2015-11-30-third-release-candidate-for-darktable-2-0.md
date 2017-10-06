author: houz
comments: true
date: 2015-11-30 10:55:34+00:00
layout: post
link: http://www.darktable.org/2015/11/third-release-candidate-for-darktable-2-0/
slug: third-release-candidate-for-darktable-2-0
title: third release candidate for darktable 2.0 & string freeze
wordpress_lede: autumn_path.jpg
wordpress_id: 3883
tags: announcement, darktable release

we're proud to announce the third release candidate in the new feature release of darktable, 2.0~rc3.

the release notes and relevant downloads can be found attached to this git tag:
[https://github.com/darktable-org/darktable/releases/tag/release-2.0rc3](https://github.com/darktable-org/darktable/releases/tag/release-2.0rc3)
please only use our provided packages ("darktable-2.0.rc3.*" tar.xz and dmg) not the auto-created tarballs from github ("Source code", zip and tar.gz). the latter are just git snapshots and will not work! here are the direct links to tar.xz and dmg:
[https://github.com/darktable-org/darktable/releases/download/release-2.0rc3/darktable-2.0.rc3.tar.xz](https://github.com/darktable-org/darktable/releases/download/release-2.0rc3/darktable-2.0.rc3.tar.xz)
[https://github.com/darktable-org/darktable/releases/download/release-2.0rc3/darktable-2.0.rc3.dmg](https://github.com/darktable-org/darktable/releases/download/release-2.0rc3/darktable-2.0.rc3.dmg)

the checksums are:

    
    $ sha256sum darktable-2.0~rc3.tar.xz
    4d81527350e6f722da484bdcd3f620918321b0e15b1fdad219821abbf23c2c89
    darktable-2.0~rc3.tar.xz
    $ sha256sum darktable-2.0~rc3.dmg
    109d5f14cd71fcee29b6646698028fde1f864c6cd51c5c25086b1a1d9f9578b2
    darktable-2.0~rc3.dmg


packages for individual platforms and distros will follow shortly.

as we're closing in to the final version, we are also officially in string freeze as of now. this affects darktable, not the user manual.

the changes from rc2 include minor bugfixes, such as:



	
  * camera support improvements

	
    * add support for the Canon PowerShot G5 X

	
    * basic support for Olympus SP320

	
    * Panasonic LF1 noise profile and white balance presets

	
    * noiseprofiles: add Sony A77mk2




	
  * high-dpi fixes

	
  * fixed a few memleaks

	
  * 3:1 aspect ratio as preset in crop&rotate

	
  * magic lantern-style deflicker has been activated in the exposure module

	
  * updated translations


and the preliminary changelog as compared to the 1.6.x series can be found below.

when updating from the currently stable 1.6.x series, please bear in mind that your edits will be preserved during this process, but it will not be possible to downgrade from 2.0 to 1.6.x any more. be careful if you need darktable for production work!

happy 2.0~rc3 everyone :)

	
  * darktable has been ported to gtk-3.0

	
  * new thumbnail cache replaces mipmap cache (much improved speed, less crashiness)

	
  * added print mode

	
  * reworked screen color management (softproof, gamut check etc.)

	
  * removed dependency on libraw

	
  * removed dependency on libsquish (solves patent issues as a side effect)

	
  * unbundled pugixml, osm-gps-map and colord-gtk

	
  * text watermarks

	
  * color reconstruction module

	
  * raw black/white point module

	
  * delete/trash feature

	
  * addition to shadows&highlights

	
  * more proper Kelvin temperature, fine-tuning preset interpolation in WB iop

	
  * noiseprofiles are in external JSON file now

	
  * monochrome raw demosaicing (not sure whether it will stay for release, like Deflicker, but hopefully it will stay)

	
  * aspect ratios for crop&rotate can be added to conf (ae36f03)

	
  * navigating lighttable with arrow keys and space/enter

	
  * pdf export – some changes might happen there still

	
  * brush size/hardness/opacity have key accels

	
  * the facebook login procedure is a little different now

	
  * export can upscale

	
  * we no longer drop history entries above the selected one when leaving darkroom or switching images

	
  * text/font/color in watermarks

	
  * image information now supports GPS altitude

	
  * allow adding tone- and basecurve nodes with ctrl-click

	
  * new "mode" parameter in the export panel

	
  * high quality export now downsamples before watermark and frame to guarantee consistent results

	
  * Lua scripts can now add UI elements to the lighttable view (buttons, sliders etc …)

	
  * a new repository for external Lua scripts was started


