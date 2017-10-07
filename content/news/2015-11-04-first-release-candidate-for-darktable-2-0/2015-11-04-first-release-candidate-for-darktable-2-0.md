author: houz
comments: true
date: 2015-11-04 12:27:28+00:00
layout: post
link: http://www.darktable.org/2015/11/first-release-candidate-for-darktable-2-0/
slug: first-release-candidate-for-darktable-2-0
title: first release candidate for darktable 2.0
lede: nut_wide.jpg
wordpress_id: 3835
tags: announcement, darktable release

We're proud to announce the first release candidate in the new feature release of darktable, 2.0~rc1.

The release notes and relevant downloads can be found attached to this git tag:
https://github.com/darktable-org/darktable/releases/tag/release-2.0rc1
Please only use our provided packages ("darktable-2.0.rc1.*" tar.xz and dmg) not the auto-created tarballs from GitHub ("Source code", zip and tar.gz). The latter are just git snapshots and will not work! Here are the direct links to tar.xz and dmg:
https://github.com/darktable-org/darktable/releases/download/release-2.0rc1/darktable-2.0.rc1.tar.xz
https://github.com/darktable-org/darktable/releases/download/release-2.0rc1/darktable-2.0.rc1.dmg


    $ sha256sum darktable-2.0.rc1.tar.xz
    412f17131c8674e266c91c933de1aa2b04c2ab7efdc04a60b00faf3abffc0446
    darktable-2.0.rc1.tar.xz
    $ sha256sum darktable-2.0.rc1.dmg
    080b846e677e0e2471389375a103c1714eefd0f9e7c64658758f2a7bf56f69c8
    darktable-2.0.rc1.dmg


Packages for individual platforms and distros will follow shortly.

For your convenience, these are the ubuntu/debian packages required to build the source:


    $ sudo apt-get build-dep darktable && sudo apt-get install libgtk-3-dev libpugixml-dev libcolord-gtk-dev libosmgpsmap-1.0-0-dev libcups2-dev



And the preliminary changelog can be found below.

When updating from the currently stable 1.6.x series, please bear in mind that your edits will be preserved during this process, but it will not be possible to downgrade from 2.0 to 1.6.x any more. Be careful if you need darktable for production work!

Happy 2.0~rc1 everyone :)




  * darktable has been ported to gtk-3.0


  * new thumbnail cache replaces mipmap cache (much improved speed, less crashiness)


  * added print mode


  * reworked screen color management (softproof, gamut check etc.)


  * text watermarks


  * color reconstruction module


  * raw black/white point module


  * delete/trash feature


  * addition to shadows&highlights


  * more proper Kelvin temperature, fine-tuning preset interpolation in the white balance module


  * noiseprofiles are in external JSON file now


  * monochrome raw demosaicing (not sure whether it will stay for release, like Deflicker, but hopefully it will stay)


  * aspect ratios for crop&rotate can be added to conf ([ae36f03](https://github.com/darktable-org/darktable/commit/ae36f035e1496b8b8befeb74ce81edf3be588801))


  * navigating lighttable with arrow keys and space/enter


  * pdf export – some changes might happen there still


  * brush size/hardness/opacity have key accels


  * the facebook login procedure is a little different now


  * export can upscale


  * we no longer drop history entries above the selected one when leaving darkroom or switching images


  * text/font/color in watermarks


  * image information now supports GPS altitude


  * allow adding tone- and basecurve nodes with ctrl-click


  * we renamed mipmaps to thumbnails in the preferences


  * new “mode” parameter in the export panel


  * high quality export now downsamples before watermark and frame to guarantee consistent results


  * Lua scripts can now add UI elements to the lighttable view (buttons, sliders etc.)


  * a new repository for external Lua scripts was started.


