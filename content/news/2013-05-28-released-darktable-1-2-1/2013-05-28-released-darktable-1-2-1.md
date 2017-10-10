author: smn
comments: true
date: 2013-05-28 12:21:15+00:00
layout: post
link: http://www.darktable.org/2013/05/released-darktable-1-2-1/
slug: released-darktable-1-2-1
title: released darktable 1.2.1
wordpress_lede: IMG_5490_export2.jpg
wordpress_id: 2930
tags: announcement, darktable release

Dear all,

we just released a patch version for the stable branch 1.2. As usual you can find the source tarball here:




  * [source tarball](https://sourceforge.net/projects/darktable/files/darktable/1.2/darktable-1.2.1.tar.xz/download)


  * The Ubuntu PPA has already been updated by Pascal (thanks!),


  * the Mac OSX image will probably take a little longer.



We collected almost 150 commits on top of the last release from April, 7 which bring you quite some bugfixes, new noise profiles and white balance settings for several cameras etc.

One major change concerning the release itself has been made. The development team decided to exclude translations which are not properly finished from releases. The corresponding PO files will however stay in the git version. The selection has been done based on the percentage of translated and fuzzy strings since we are lacking detailed knowledge about the languages in
question.

But have a look yourself:



## Translation changes






  * New translation: Danish


  * Some translations have been removed from the release due to missing strings





## New noise profiles






  * Canon EOS 450D / Kiss X2


  * Canon EOS 1100D / REBEL T3


  * Canon EOS 1D Mark II


  * Canon EOS 1D Mark III


  * All Canon Model names are now recognized, e.g. Canon EOS 350D and Canon EOS 350D DIGITAL and Canon EOS DIGITAL REBEL XT and Canon EOS Kiss Digital N point to the same camera.


  * Olympus E-520


  * Olympus E-1


  * Olympus E-3


  * Olympus E-P2


  * Pentax K-30


  * Panasonic GH-2


  * Panasonic DMZ-FZ18


  * Additional data for Pentax K-5 II


  * Nikon D7100


  * Nikon D5200


  * Sony A57





## White balances, color matrices






  * Fix issues with different camera model names for various Canon cameras (see above)


  * White balance for Panasonic DMC-GH2


  * Updates whitebalance list with the latest version of UFRaw's cvs version


  * Whitebalances for Samsung NX5, NX10, NX11 (copied from NX100)





## Bugfixes






  * new RawSpeed version r537


  * Compatible with openEXR 2.0


  * Facebook export now allows HQ images (up to 2048px)


  * Blend mode "vividlight" should work for NaNs


  * Fix compile issues for OpenBSD


  * Whitebalance is now relative to daylight, not to camera white balance (this will not change any processing you have done, only the values displayed will differ)


  * Now importing folder via key accelerator is supported.


  * Only one temperature slider in white balance


  * Some fixes to the zoom behaviour in darkroom mode


  * New lensfun geometries now supported (with lensfun >= 0.2.7)


  * More coherent bauhaus UI for the split toning module


  * The color transfer module is now marked as deprecated. Will be superseeded by color mapping in the next major release.


  * Fix some possible deadlocks, memory leaks and null pointer dereferences


  * Status message in top bar should be updated more frequently now


  * Some more elaborate status messages if lens/camera not found in the lens correction module, if export failed


  * Option for parallel export threads removed from config, too dangerous


  * Option for thumbnail cache now specified in MB


  * Updated purge_non_existing_images.sh script


  * CLI option -d nan gives per-module output of NaN values


  * Some minor renamings, typo fixings...




Thanks to everybody who made this release possible. All developers, translators, proof readers, battle testers and the guys who maintain the great libraries we depend on. Furthermore a big thanks to all users which help to make darktable better by providing noise profiles, color matrices and white balance settings for their cameras, you effort is greatly appreciated!

As usual, we have not been lazy, so for those of you which do not need to have a reliable darktable installation all the time: in git master some amazing new features have landed (check the blog...)&nbsp;– try it out!

Cheers,
Simon

