author: smn
comments: true
date: 2012-04-28 14:25:13+00:00
layout: post
link: http://www.darktable.org/2012/04/darktable-1-0-1-released/
slug: darktable-1-0-1-released
title: darktable 1.0.3 released
wordpress_id: 1486
tags: announcement, darktable, darktable, download, opensolaris, release, tarball

Pascal de Bruijn did some good work backporting some of the progress from git master to the 1.0 release. We packed that into a tarball, here it is:

<del>[https://sourceforge.net/projects/darktable/files/darktable/1.0/darktable-1.0.1.tar.gz/download](https://sourceforge.net/projects/darktable/files/darktable/1.0/darktable-1.0.1.tar.gz/download)</del>

[http://sourceforge.net/projects/darktable/files/darktable/1.0/darktable-1.0.3.tar.gz/download](http://sourceforge.net/projects/darktable/files/darktable/1.0/darktable-1.0.3.tar.gz/download)

(We had a problem packaging sources, so 1.0.3 is now on air. Please use it instead of 1.0.1)

As usual we have Ubuntu Packages are readily available on Pascal's PPA, for Lucid, Natty, Oneiric and Precise:
[https://launchpad.net/~pmjdebruijn/+archive/darktable-release](https://launchpad.net/%7Epmjdebruijn/+archive/darktable-release)
[https://launchpad.net/~pmjdebruijn/+archive/darktable-release-plus](https://launchpad.net/%7Epmjdebruijn/+archive/darktable-release-plus)

And these are the major changes:

**Usability improvements:**



	
  * Filmstrip centers on selected image


**Behavioral changes:**



	
  * Improved (hierarchical) tag export for flickr and friends


**Camera support:**



	
  * Improved Sony NEX-7 support

	
  * Initial camera support for Nikon D800 and Sony SLT-A57 (color rendition of these cameras might still be suboptimal due to the lack of a proper color matrix, and is subject to future change.)

	
  * White balance updates for Canon EOS Rebel T3, Olympus E-5 & Nikon D800


**Platform support:**



	
  * Fixes for FreeBSD


**Various:**



	
  * New subtle denoise preset for equalizer

	
  * Various build fixes

	
  * Numerous other fixes



James C. McPherson provides a preliminary Solaris 11 package for this release:

<del>[http://www.jmcp.homeunix.com/Packages/dt-1.0.1-release.p5p.gz](http://www.jmcp.homeunix.com/Packages/dt-1.0.1-release.p5p.gz)</del>

[http://www.jmcp.homeunix.com/Packages/dt-1.0.3-release.p5p.gz](http://www.jmcp.homeunix.com/Packages/dt-1.0.3-release.p5p.gz)
with associated verbiage at
[http://www.jmcp.homeunix.com/blog/2012/04/29/darktable-1-0-3-ips-package-available/](http://www.jmcp.homeunix.com/blog/2012/04/29/darktable-1-0-3-ips-package-available/)

Thanks to everyone who contributed to this and especially to Pascal for taking care of this release.

Enjoy it!
