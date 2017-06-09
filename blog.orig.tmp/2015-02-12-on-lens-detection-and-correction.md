author: pmjdebruijn
comments: true
date: 2015-02-12 20:10:37+00:00
layout: post
link: http://www.darktable.org/2015/02/on-lens-detection-and-correction/
slug: on-lens-detection-and-correction
title: On Lens Detection and Correction
wordpress_id: 3543
tags: blog

darktable (and some other projects, like for example ufraw) don't do any real lens detection or correction by itself. We depend on two libraries which in most cases are provided by the Linux distribution you're using.


## Lens Detection


Many image files contain metadata about how the image was created. In case of digital camera images, a standard called Exif is used, this standard allows a camera to record many details about how an image was taken. However Exif is not a singular well defined specification, there is a common part that is well defined, and there are the so-called MakerNotes. The MakerNotes are parts of Exif that each vendors gets to do with whatever they like. They are typically completely undocumented, and have to be reverse-engineered to be able to handle them in any way. For most vendors this reverse engineering has been done to some degree and at least parts of the MakerNotes can be deciphered most of the time.

It's in these undocumented MakerNotes that the camera vendors tend to encode a lens id, this lens id typically is just a number for which the camera vendors provide no reference. And without a reference lookup table such a number is quite useless. Open source tools end up having to crowd source it and collate lensid – lensname pairs to be able to identify lenses. darktable, like many others, in particular uses the Exiv2 library.

You can use Exiv2's command line tool to search for lens related tags in your own raw files like so:

    
    # exiv2 -pt IMG_1234.CR2 | grep -ai lens


And if you have a lens that's already been reported to the Exiv2 project, you'll see something along these lines:

    
    Exif.CanonCs.LensType       Short       1  Canon EF-S 24mm f/2.8 STM


However if you have a fairly new lens, chances are it hasn't been reported yet, and you'll get something like this:

    
    Exif.CanonCs.LensType       Short       1  (4154)


There are also cases, where Exiv2 might report the wrong lens, this happens because the vendors don't preallocate numbers for third party lens manufacturers, so they end up having to occupy random lens ids, which can end up conflicting with new first party lenses later on. Exiv2 tries to resolve such conflicts on a best effort basis using some heuristics, like trying to match min/max focal lengths and min/max aperture.

The Exiv2 project, like many open source projects, isn't particularly overstaffed, so they tend to release fairly infrequently, thus the difference between what's available in their development tree and what's available in released distributions can diverge significantly. Practically this means that any lens newly released in the last 6 – 12 months is not likely to be detected properly.

So if you have a lens that is not being properly reported, the best course of action is to check Exiv2's development sources, to see if it's already known (the line references may drift over time, so you might need to scroll around a bit):



	
  * Canon bodies: [http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/canonmn.cpp#L600](http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/canonmn.cpp#L600)

	
  * Sony or Minolta bodies: [http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/minoltamn.cpp#L1613](http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/minoltamn.cpp#L1613)

	
  * Nikon bodies: [http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/nikonmn.cpp#L1737](http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/nikonmn.cpp#L1737)

	
  * Olympus bodies: [http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/olympusmn.cpp#L1254](http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/olympusmn.cpp#L1254)

	
  * Pentax bodies: [http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/pentaxmn.cpp#L687](http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/pentaxmn.cpp#L687)

	
  * Samsung bodies: [http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/samsungmn.cpp#L52](http://dev.exiv2.org/projects/exiv2/repository/entry/trunk/src/samsungmn.cpp#L52)


If you can find your lens in one of the above source files, it means even though your current version of Exiv2 might not recognize the lens, the developers are already aware of it, and a future release of Exiv2 will likely be able to recognize that lens. We highly recommend against trying to update your Exiv2 library manually.

If you still can't find your lens, please file a feature request with the Exiv2 project here (and yes, you'll need to create an account):

	
  * [http://dev.exiv2.org/projects/exiv2/issues/new](http://dev.exiv2.org/projects/exiv2/issues/new)


Please include the following information:

	
  * Full output of:

    
    exiv2 -pt FILENAME | grep -ai lens




	
  * The proper full name of the lens (be mindful of capitalization)

	
  * Preferably include a link to the lens' product page on the manufacturers website

	
  * Attach a sample low resolution JPEG (unmodified, most cameras allow you to shoot lower resolution JPEGs)




## Lens Correction


Presuming Exiv2 (and thus darktable) detects your lens properly, it passes the lens name off to the Lensfun library, which searches its own lens correction database for that particular name. And if it finds a match, it applies that correction data to your image.

But for this to work the name Exiv2 supplies and the name in the Lensfun database need to be a fairly close match. As far as I'm aware Lensfun does ignore punctuation, but other than that, you need a proper match for the correction to be automatic.

Also keep in mind that the lens correction data isn't provided by the vendors, so this is yet again something that needs to be crowd sourced. However in stark contrast to the Exiv2 situation, the process of generating decent correction data is quite a bit more involved.

So if you're missing your particular lens in your particular version of Lensfun, you can check here to see if your lens might already have correction data in Lensfun's development tree:



	
  * [http://lensfun.sourceforge.net/lenslist/](http://lensfun.sourceforge.net/lenslist/)

	
  * [http://sourceforge.net/p/lensfun/code/ci/master/tree/data/db/](http://sourceforge.net/p/lensfun/code/ci/master/tree/data/db/)


As you might notice, not all types of correction are available for all lenses.

If you want to generate correction data for your own lenses and submit it to the Lensfun project, please have a look here:

	
  * [http://lensfun.sourceforge.net/calibration/](http://lensfun.sourceforge.net/calibration/)



