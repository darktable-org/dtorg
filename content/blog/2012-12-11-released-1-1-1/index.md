---
author: jo
comments: true
date: 2012-12-11 07:02:17+00:00
layout: post
link: /2012/12/released-1-1-1/
slug: released-1-1-1
title: "released 1.1.1"
lede: threerocks_wide.jpg
lede_author: <a href="https://jo.dreggn.org/home/">jo</a>
wordpress_id: 2590
tags:
  - announcement
---
we released a patch release:

[https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.1.tar.gz/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.1.tar.gz/download)

along with an updated usermanual:

[https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-usermanual-1.1.1.pdf/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-usermanual-1.1.1.pdf/download)

this resolves a couple of issues with 1.1. so no new features here, but:

* minor reordering of lighttable mode modules (geotagging, keywords and recent collections)
* cleaned up the default visible plugins when first starting darktable
* in most cases raw files will now show thumbnails in the import dialog (thanks to Mattias Eriksson)
* a curve related crash was fixed (#9906 thanks to James C. McPherson)
* comma seperated tags should work everywhere now (#9006 thanks to Tobias Ellinghaus)
* Ulrich Pegelow fixed a huge amount of opencl related issues, particularly for AMD GPUs
* we now deal better with hybrid GPU machines (#9074 by Ulrich Pegelow)
* a deadlock in the lens correction module was fixed (#9106 thanks to Ulrich Pegelow)
* we don't delete module presets when cancelling the dialog anymore (#9108 thanks to Tobias Ellinghaus)
* we now have better default memory usage settings (which are set upon starting darktable the first time)
* initial support for SONY NEX 5R
* preliminary/experimental Canon EOS 6D and Sony RX1 support (future changes for these camera's may (for the time being) retroactively affect your images)
* Canon EOS 6D white balance presets (thanks to no_maam_)
* lots of updates for the usermanual (make sure you [download a new copy from here](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-usermanual-1.1.1.pdf/download))
* and for our 1.1 the ubuntu packages from the PPAs were built without facebook export support, this has been fixed for 1.1.1

darktable wouldn't be where it is now if we weren't able to depend on
the great work of others, in particular we'd like to thank:

Klaus Post (RawSpeed), Dave Coffin (dcraw), Andreas Hugel (Exiv2),
Andrew Zabolotny (Lensfun), Marti Maria (lcms), Niels Kristian Bech Jensen (ufraw).

have a lot of fun!
