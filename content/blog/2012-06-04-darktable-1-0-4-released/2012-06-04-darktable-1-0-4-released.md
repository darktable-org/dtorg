author: smn
comments: true
date: 2012-06-04 00:13:47+00:00
layout: post
link: http://www.darktable.org/2012/06/darktable-1-0-4-released/
slug: darktable-1-0-4-released
title: darktable 1.0.4 released
wordpress_lede: 20110428_IMG_3966_export.jpg
wordpress_id: 1794
tags: announcement, darktable release

Pascal was so kind to tend to a stable branch, the next incarnation of which we have the good fortune to announce.

The changes over darktable 1.0.3 are:

* More robust OpenMP compiler detection code
* New warming/cooling filter presets for color correction plugin
* Lighttable thumbnails should be slightly faster and sharper
* Correctly restore panels when using Tab.
* Checking if an export target directly is read-only
* Writing of hierarchical tags in our .xmp has been improved
* Don't list system display profile for anything but the display profile selection
* We disabled scrollwheel scrolling in darkroom mode as it sometimes
* conflicts with widget behavior
* Lighttable thumbnails are now color managed with some caveats (1)
* Improved color rendition:

    * Nikon D800
    * Canon EOS 5D Mark III

* White balance presets:

    * Canon EOS 5D Mark III
    * Canon EOS 7D (updated)
    * Olympus E-M5
    * Samsung NX100 (updated)
    * Olympus E-PL1 (updated)
    * Olympus E-PL2 (updated)
    * Olympus E-PL3 (updated)

(1) Lighttable color management caveats:

Our previous releases didn't have any color management in lighttable mode (and the filmstrip), in this release we have a quick-fix implementation of color management for lighttable mode. For 1.0.4, newly imported files use the Preview JPEG by default for the thumbnail, in that case it's still not color managed. After entering darkroom mode (after which the thumbnail is regenerated in case you changed the history stack) it will be color managed. Without changed history stack the thumbnail will always be the embedded JPEG. If you need lighttable mode to be color managed all the time you can disable reading of the Preview JPEGs in our Preferences dialog "don't use embedded preview jpeg but half-size raw", do note that this will significantly slow down thumbnail generation and consequently will slow down new imports. To have darktable regenerate all old previews (in a color managed fashion) you can delete the `~/.cache/darktable/mipmaps*` files.

And the log tells we have to thank the following people for making this release possible:

Pascal de Bruijn, johannes hanika, Tobias Ellinghaus, Raphael Manfredi, Ulrich Pegelow, James C. McPherson, parafin, Olivier Tribout, Moritz Lipp, Joao Trindade, Christian Tellefsen

You can grab the new source package from here:

[https://sourceforge.net/projects/darktable/files/darktable/1.0/darktable-1.0.4.tar.gz/download](https://sourceforge.net/projects/darktable/files/darktable/1.0/darktable-1.0.4.tar.gz/download)

PPA updates are available already.

The Solaris 11 package is available from

[http://www.jmcp.homeunix.com/Packages/Darktable.1.0.4.p5p.gz](http://www.jmcp.homeunix.com/Packages/Darktable.1.0.4.p5p.gz)

Enjoy the new release.
