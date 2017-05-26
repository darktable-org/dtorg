---
author: houz
comments: true
date: 2012-07-05 14:13:10+00:00
layout: post
link: http://www.darktable.org/2012/07/exporting-images-on-the-command-line/
slug: exporting-images-on-the-command-line
title: Exporting images on the command line
wordpress_id: 1837
categories:
- blog
- development
---

Recent builds from git will bring you a new executable, “darktable-cli”. With this tool you can export images using the processing power of darktable on the command line.

The simplest way to call the utility is

    
    darktable-cli <input> <output>


This will take the _input_ image, look for the XMP file associated with it, process it at maximal resolution and write the output to _output_, trying to guess the output format from the output filename. You can also explicitly give a XMP file by running

    
    darktable-cli <input> <xmp> <output>


When a scaled down output is needed you can overwrite the default 0x0 size by adding one or both of

    
    --width <max x size> --height <max y size>


These settings work the same as in the darktable gui. There is also a setting

    
    --bpp <max bitdepth>


which is not working at the time of writing this, so currently the highest possible bit depth for the chosen output format is used.

All of this is subject to change so expect more options to be added in the future. To be on the safe side darktable-cli will not overwrite files but just terminate when _output_ already exists.

As always, play with it, use it, break it, and report back. Preferably on the mailing lists or in IRC.
