author: LebedevRI
comments: true
date: 2017-01-12 17:57:27+00:00
layout: post
link: http://www.darktable.org/2017/01/rawsamples-ch-replacement/
slug: rawsamples-ch-replacement
title: rawsamples.ch replacement
wordpress_id: 4694
tags: announcement, blog, community, '@andabata', '@lebedevri', '@pixlsus', foss, photography, rawsamples

[Rawsamples.ch](http://rawsamples.ch) is a website with the goal to:



<blockquote> …provide RAW-Files of nearly all available Digitalcameras mainly to software-developers.  [sic]</blockquote>



It was created by Jakob Rohrbach and had been running since March 2007, having amassed over 360 raw files in that time from various manufacturers and cameras. Unfortunately, back in 2016 the site was hit with an SQL-injection that ended up corrupting the database for the Joomla install that hosted the site. To compound the pain, there were no database backups … :(

Luckily, [Kees Guequierre](https://www.flickr.com/photos/andabata) ([dtstyle.net](https://dtstyle.net/)) decided to build a site where contributors could upload sample raw files from their cameras for everyone to use - particularly developers. We downloaded the archive of the raw files kept at rawsamples.ch to include with files that we already had. The biggest difference between the files from [rawsamples.ch](http://rawsamples.ch) and [raw.pixls.us](https://raw.pixls.us) is the licensing. The existing files, and the preference for any new contributions, are licensed as [Creative Commons Zero – Public Domain](https://creativecommons.org/publicdomain/zero/1.0/) (as opposed to [CC-BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)).

After some hacking, with input and guidance from darktable developer [Roman Lebedev](https://github.com/LebedevRI), the site was finally ready.



## raw.pixls.us



The site is now live at [https://raw.pixls.us](https://raw.pixls.us).

You can [look at the submitted files](https://raw.pixls.us#repo) and search/sort through all of them (and download the ones you want).

In addition to browsing the archive, it would be fantastic if you're able to supplement the database by upload sample images.  Many of the images from the rawsamples.ch archive are licensed [CC-BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/), but we'd rather have the files licensed [CC0](https://creativecommons.org/publicdomain/zero/1.0/).  CC0 is preferable to CC-BY-NC-SA because if the sample raw files are separated from the database, they can safely be redistributed without attribution (attribution is required by CC-BY-NC-SA). So if you have a camera that is already in the list with the more restrictive Creative Commons license, then please consider uploading a replacement for us!

**We are looking for shots that are:**




  * Lens mounted on the camera


  * Lens cap off


  * In focus


  * With normal exposure, not underexposed and not overexposed


  * Landscape orientation


  * Licensed under the [Creative Commons Zero](https://creativecommons.org/publicdomain/zero/1.0/)



**We are _not_ looking for:**




  * Series of images with different ISO, aperture, shutter, wb, or lighting  
(Even if it's a shot of a color target)


  * DNG files created with Adobe DNG Converter



Please take a moment and see if you can provide samples to help the developers!

This post has been written in collaboration with [pixls.us](https://pixls.us/)
