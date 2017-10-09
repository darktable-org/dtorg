author: Henrik Andersson
comments: true
date: 2012-10-06 17:16:03+00:00
layout: post
link: http://www.darktable.org/2012/10/process-hdr-images-using-darktable/
slug: process-hdr-images-using-darktable
title: Process HDR images using darktable.
wordpress_lede: img_0001.jpg
wordpress_id: 2193
tags: blog, HDR, processing, workflow

**Introduction**

This blog post will go through a simple workflow when working with high dynamic ranged images using darktable and the modules for processing, you need use darktable 1.1RC for this guide. The example image used in the screenshots can be downloaded at following link: [AtriumMorning](http://www.mpi-inf.mpg.de/resources/hdr/img_hdr/AtriumMorning.exr)


# **How to make an HDR image**


I'm not going into details of the process of making an HDR image, there are many guides out there describing manual methods or automatic ones which some cameras have, but basically, take a bracket shot of your scene and import them into darktable and do no processing at all, export to 16bit tiff and import the tiff files into luminance hdr where you use its align and merge HDR functionality, when HDR is merged and cooked just save the image as EXR image format which you load into darktable for further processing.


# **Processing the HDR image using darktable**


**Step 1**, load your HDR image into darktable, and enter darkroom, the image will probably look very strange and the first thing is disable all auto applied modules by selecting the "active group" and turn off all modules.



**Step 2**,  the first thing to do now is to settle a base for further processing correcting the image exposure, the approach differs between processing a day or night shoot. If you have a night shot with a few light sources you should now correct the exposure of the light source to bring back as much detail into light source without lowering its intensity so it end up looking dull. If you process a daylight shoot for example a room with windows where you have a indoor scene and sunlit outdoor scene, the approach will be to adjust exposure so the darkest part of the image eg. shadows contains details and have a nice dark tone. This is just a starting point for both night and day shoots, you will likely get back to this step for fine tuning the end result so don't spend too much time on this step for now, just do a rough estimation of what you think you want according to the 2 approaches described above.

![exposure]({attach}exposure.jpg)



**Step 3**, we should now apply a tone map operator, which purpose is to compress a high dynamic ranged image into a lower range suitable for display on screen etc. There are 2 variants of tone map operators, global and local, local tone map operators tries to preserve contrast, some is better than others but in general will make the image look unrealistic and are commonly used to do "artistic"  HDR images. This blog post is not about doing cartoons and therefore i will not go though a process of doing such thing. At our hands we have 'global tonemap' module in darktable which has 3 standard implementations of tonemappers, reinhard, filmic response curve and drago. The choice of operator is just a choice of what get closest to what you want. All three of them have their own pros and cons but is usable in both day and night shoots, I use all three of them depending of what result I'm after. Choose a global tone map operator and tune available controls to your like, if you processing a day shot you want to bring details in highlights and if you are on a night shot the shadows are what you aim to bring back. You will probably depending on tone map operator choice and its controls go back to step 2 to fine tune the exposure. The detail slider within the global tonemap module will try to recover some contrast details which is lost in the tonemap operation.

![tonemap]({attach}tonemap.jpg)



**Step 4**, the image can sometimes look somewhat dull and local contrast enhancement comes to the rescue, darktable have 2 approaches of local contrast, the equalizer can enhance contrast locally and the module named local contrast which at the time writing only is available in the source repo but will be available in the next release of darktable.

![localcontrast]({attach}localcontrast.jpg)



Additionally, you can use any module to enhance the image in the way you want. Play around and you will find how to get closer to the end result you are searching for, but remember not to touch exposure slider when you archived the result from above steps, that will ruin the process and you will have to start over from begin.
