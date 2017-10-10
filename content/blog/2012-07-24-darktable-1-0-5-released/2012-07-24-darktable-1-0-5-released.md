author: jo
comments: true
date: 2012-07-24 09:34:47+00:00
layout: post
link: http://www.darktable.org/2012/07/darktable-1-0-5-released/
slug: darktable-1-0-5-released
title: darktable 1.0.5 released
wordpress_lede: ladybugs.jpg
wordpress_id: 1890
tags: announcement, darktable release

It's our pleasure to announce that darktable-1.0.5 has been released. Find the tarball on sf.net:

[https://sourceforge.net/projects/darktable/files/darktable/1.0/darktable-1.0.5.tar.gz/download](https://sourceforge.net/projects/darktable/files/darktable/1.0/darktable-1.0.5.tar.gz/download)

The Ubuntu PPAs have been built already, you should get them with your next update automatically if you subscribed to Pascal's PPA.

This has a good chance of being the last one in a series of stable releases (with stuff backported from our latest and greatest). Thanks to Pascal for maintaining it! As such, it comes with a short list of maintenance things as change log:

* Update to RawSpeed r438
* Update to LibRaw 0.14.7
* White balance presets for Nikon Coolpix P7100 and Panasonic GF3
* White balance preset updates for Canon EOS 7D, Canon EOS 350D
* Standard Color Matrices for Canon EOS 650D, Canon EOS 5D Mark III, Canon EOS 1D X, Canon PowerShot G1 X, Canon PowerShot SX220, Nikon D3200, Nikon D4, Nikon D800, Olympus E-M5, Panasonic GF5, Sony SLT-A37/A57, Leica X1/X2, Sony DSC-RX100
* A few memory leaks were resolved
* A few generic bugs were resolved

We'd like to take the opportunity this time to thank some other projects we depend on, and their authors for being awesome:

* **RawSpeed**: Klaus Post
* **LibRaw**: Alex Tutubalin
* **UFraw**: (white balance presets), Niels Kristian Bech Jensen, Udi Fuchs
* **DCraw**: Dave Coffin
* **Adobe** (standard matrices)
* **Exiv2**: Andreas Hugel
* **Lensfun**: Andrew Zabolotny, Sebastian Kraft

Commits on top of 1.0.4 proudly brought to you by:

Pascal de Bruijn, Tobias Ellinghaus, Simon Spannagel, johannes hanika, Christian Tellefsen, Richard Wonka, Olivier Tribout, Ger Siemerink, Ulrich Pegelow, Petr Styblo, madanyang, Jesper Pedersen, James C. McPherson, Boucman, Bastien Bouclet.

Thanks for playing everyone!

All the rest: hope you enjoy the release and bear with us while we prepare git master for 1.1 ...
