---
author: jcsogo
comments: true
date: 2012-03-15 07:53:25+00:00
layout: post
link: http://www.darktable.org/2012/03/darktable-1-0-released/
slug: darktable-1-0-released
title: darktable 1.0 released
wordpress_id: 1396
categories:
- announcement
- darktable release
tags:
- darktable
- release
---

It is done, 1.0 is out. I sent out most of the new features with the announcement for 1.0rc2 a few weeks ago already, but for completeness, here it is again:


  * New cameras supported 
    *   Leica M9

	
    *   NX100/NX5/NX10/NX11

	
    *   Panasonic DMC-GX1

	
    *   Pentax K-r

	
    *   Canon Powershot S100

	
    *   Olympus XZ-1

	
    *   Olympus E-P3

	
    *   Sony DSLR A330

	
    *   Sony NEX-5N

	
    *   Canon EOS 1000D

	
    *   Canon EOS 600D

	
    *   Sony Alpha 390

	
    *   Fuji Finepix HS20EXR




  * New and updated translations (we now have chinese!)


  * New modules:

	
    *   shadows & highlights

	
    *   enhanced tone curve. now operates in a and b channels as well




  * Refactored modules:

	
    *   import

	
    *   snapshots (enable sliding separation line between before/after images)

	
    *   metadata




  * New image cache

	
    *   faster concurrent access and insertion

	
    *   reduces needed memory

	
    *   more thumbnails stored on disk

	
    *   read embedded jpegs for creating thumbnails (faster folder import)




  * Increased general speed on sqlite3 (journaled, pagesize optimizations)


  * Reworked, modular UI


  * Keyboard shortcuts support - key accelerators (GSoC)


  * Unity launcher support (Ubuntu)


  * Quicktool bar: exposure, presets and styles


  * New color picker


  * Web gallery export now with next/prev buttons per image


  * Removed gconf: not used anymore, we have our own backend


  * Bugfixes



Also, a couple of caveats to keep in mind this time:


  * We don't support fuji superccd at this point (more or less a simple fix, if you want to do it, contact us..)


  * We disabled openmp by default for mac builds, as gcc on that platform seems to have some issues (<gcc 4.6, that is).


  * We had to roll back libraw to <14.5, so the fuji X10 is not working at the moment.


  * There have been issues with memory on 32-bit systems. seems to be okay currently, but something to keep in mind. use 64-bits if you can!



And as always a couple of links, just in case.



  * Source tar.gz:  

[https://sourceforge.net/projects/darktable/files/latest/download](https://sourceforge.net/projects/darktable/files/latest/download)


  * Ubuntu Packages are readily available on Pascal's PPA, for Lucid, Natty, Oneiric and Precise. Support for Maverick has been fully deprecated.
[https://launchpad.net/~pmjdebruijn/+archive/darktable-release](https://launchpad.net/%7Epmjdebruijn/+archive/darktable-release)
[https://launchpad.net/~pmjdebruijn/+archive/darktable-release-plus](https://launchpad.net/%7Epmjdebruijn/+archive/darktable-release-plus)
If you have 0.9.3 already installed and are upgrading using update-manager, it may ask about a partial upgrade, which should be ok (since we are rejecting the old darktable-plugins-experimental package).


  * Pascal's screen casts (for the 0.9 series, but still valid):  

[http://blog.pcode.nl/2011/11/05/darktable-0-9-screencast-library-addition/](http://blog.pcode.nl/2011/11/05/darktable-0-9-screencast-library-addition/)


  * Our blog with some cool insider info:  

[http://www.darktable.org/category/blog/](../category/blog/)



And some advertising, we might be looking for students to take on GSoC this year:

[https://sourceforge.net/apps/trac/darktable/wiki/GSOC](https://sourceforge.net/apps/trac/darktable/wiki/GSOC)
[https://sourceforge.net/apps/trac/darktable/wiki/GSOC_idea_list](https://sourceforge.net/apps/trac/darktable/wiki/GSOC_idea_list)


And of course, huge thanks to all who helped make this possible! every half hour you can steal from your jobs and families makes a difference ;)

Also a darktable release announcement can't come without the warning that this version will soon be completely obsoleted feature-wise by the git version. We have some cool stuff sitting around in branches, waiting to be merged (spoiler: cleaner, more unified module UI with new widgets, similarity-based image clustering and search, refined conditional blend modes, maybe at some point geo tagging with map support in the center view, and possibly masking).

Have a lot of fun.
