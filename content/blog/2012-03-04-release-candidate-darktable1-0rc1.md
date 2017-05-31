author: smn
comments: true
date: 2012-03-04 08:46:51+00:00
layout: post
link: http://www.darktable.org/2012/03/release-candidate-darktable1-0rc1/
slug: release-candidate-darktable1-0rc1
title: Release Candidate darktable1.0~rc1
wordpress_id: 1306
tags: announcement, darktable, candidate, release, tarball

There are still bug fixes coming, which is good. But nevertheless we just released a release candidate tarball, available for download from here:

[https://sourceforge.net/projects/darktable/files/darktable/1.0/darktable-1.0~rc1.tar.gz/download](https://sourceforge.net/projects/darktable/files/darktable/1.0/darktable-1.0~rc1.tar.gz/download)

which will hopefully help us to get rid of the last couple of remaining bugs before 1.0. For install instructions have a look on how to compile from source: [http://www.darktable.org/install/#source](http://www.darktable.org/install/#source)

This is a rough outline of the changes since 0.9.3 (quite sure we forgot something, it's been > 1000 commits):

	



  * bugfixes

	
  * translations (we now have chinese!)

	
  * new cameras supported

    * Leica M9

  
    * NX100/NX5/NX10/NX11

  
    * Panasonic DMC-GX1

  
    * Pentax K-r

  
    * Canon Powershot S100

  
    * Olympus XZ-1

  
    * Olympus E-P3

  
    * Sony DSLR A330

  
    * Sony NEX-5N

  
    * Canon EOS 1000D

  
    * Canon EOS 600D

  
    * Sony Alpha 390

  
    * Fuji Finepix HS20EXR



  * removed gconf: not used anymore, we have our own backend


  * new modules:
  
    * shadows & highlights

  
    * enhanced tone curve. now operates in a and b channels as well


    * keywords. allows usage and reordering of hierarchical keywords



  * new cache:

    * faster

  
    * reduces needed memory

  
    * more thumbnails stored on disk



  * read embedded jpegs for creating thumbnails (faster folder import)


 
  * unity launcher support (ubuntu)



  * increased general speed on sqlite3 (journaled)



  * quicktool bar: exposure, presets and styles



  * shortcuts support - key accelerators (GSoC)



  * modular ui



  * new color picker



  * web gallery export now with next/prev buttons per image



  * refactored modules:

    * import


    * snapshots (enable sliding separation line between before/after images)


    * metadata


In case you didn't notice yet, there is now also a quite active blog with some insights in ongoing development and new modules, you might want to check it out: [http://www.darktable.org/category/blog/](http://www.darktable.org/category/blog/)

We've updated the about dialog and the manpage with a new author list including the period release-0.9.3..master, but please double check if we forgot someone..

Thanks all for being a great community, thanks to all contributors! We know how hard it is to spare a few minutes each week to make dt great!

Enjoy the release, let us know about any remaining issues!
