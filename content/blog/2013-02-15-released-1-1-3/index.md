---
author: jo
comments: true
date: 2013-02-15 02:41:01+00:00
layout: post
link: /2013/02/released-1-1-3/
slug: released-1-1-3
title: "released 1.1.3"
lede: img_0012.jpg
wordpress_id: 2743
tags:
  - announcement
  - darktable release
---
hi,

there is a new point release with a couple of smaller updates.

source tarball:

https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.3.tar.xz/download

mac disk image:

https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.3.2.dmg/download

and the usermanual is still the same.

## fixes:

* check (on build) if glib 2.28 or higher is present
* don't sanitize exif when creating hdr dngs
* colorpicker now disappears immediately when disabling it
* lens correction now uses loose lens matching (ivan tarozzi)
* konica minolta dynax 5d rotation fix
* removed an outdated assertion which could cause a crash in rare cases
* don't crash when loading half-corrupted xmps
* don't crash when an imported file contains incomplete gps information
* libjpeg-turbo workaround (klaus post)

## camera support:

* preliminary support for the new nikon d5200

## white balance presets:

* sony alpha 700 (update to firmware v4)
* sony alpha 230 (new)
* canon eos 650d (new)
* canon eos rebel t2i (fixed)
* canon eos m (fixed)

## enhanced color rendition:

* konica minolta dynax 5d (wolfgang kuehnel)
* sony nex 3 (wolfgang kuehnel)
* sony alpha 230 (wolfgang kuehnel)
* sony rx100 (josef wells)

darktable wouldn't be where it is now if we weren't able to depend on the great work of others, in particular we'd like to thank:

klaus post (rawspeed), dave coffin (dcraw), andreas hugel (exiv2), andrew zabolotny (lensfun), marti maria (lcms), niels kristian bech jensen (ufraw).

cheers-
