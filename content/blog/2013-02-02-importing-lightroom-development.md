author: pascalobry
comments: true
date: 2013-02-02 11:44:22+00:00
layout: post
link: http://www.darktable.org/2013/02/importing-lightroom-development/
slug: importing-lightroom-development
title: Importing Lightroom Development
wordpress_id: 2692
tags: blog, development, upcoming, import, Lighroom, XMP

One of the most time consuming work for any photographer is probably the development process. Lot of time behind a computer screen to adjust the curves, the contrast, the colors, the sharpness... All these are application specific, that is, the development process done with Lightroom is not compatible with AfterShot Pro or darktable (to name just few RAW processing softwares around). This makes it really difficult to move from one software to another. The risk is loosing all the work done so far with a specific tool. After years, when the library contains some ten thousands pictures no one is ready for the switch.

Lightroom is a great software but it will probably never run on GNU/Linux, Adobe does not seem to have any plan for this platform (and not only for Lightroom, but this is not the subject). As a long time user of Lightroom wanting to move to GNU/Linux (which is my main working platform) I have started working on a Lightroom import support for darktable. Today I have a Windows dual-boot just to run Lightroom, a waste of disk space and a waste of time as I need to reboot when I want to process my pictures.

The import support is fully automatic and done in two phases. First when importing pictures the tags are imported, then when entering the darkroom the development process for the picture being edited are imported. This import is based on the Lightroom .xmp sidecar. The chance is that both XMP can live together as Lightroom ones are named <BASENAME>.xmp whereas darktable ones are named <BASENAME>.<ext>.xmp.

What can be imported? Many of the Lightroom developments, but it is not possible to have a 100% accurate conversion process. That's why at the moment there is no batch support. Importation is done on the darkroom, one picture at a time as it requires manual adjustments.

We can classify the importation support in three categories:



	
  1. 100% accurate:

	
    * crop

	
    * rotation

	
    * flip

	
    * tags




	
  2. Mostly accurate:

	
    * exposure / blacks

	
    * grain

	
    * tone curve (only lightness supported)

	
    * color zones

	
    * local contrast




	
  3. Needs tweaking:

	
    * vignette - The forms are not imported (rounded box effect).

	
    * spots removal - There is two kind of processing on Lightroom (clone, heal).





The work on this import module will continue, trying to be more accurate where it can be. At least I feel that this makes the migration less painful by giving the photographers an good help to quickly recover the development work done with Lightroom.

But let's look at an example, first the image as imported on Lightroom without any modifications:

[![1-initial-picture](http://www.darktable.org/wp-content/uploads/2013/02/1-initial-picture-200x100.jpg)](https://www.darktable.org/wp-content/uploads/2013/02/1-initial-picture.jpg)

Then the picture as developed on Lightroom (crop, tone curve, blacks and local contrast):

[![2-lr-develop](http://www.darktable.org/wp-content/uploads/2013/02/2-lr-develop-200x100.jpg)](https://www.darktable.org/wp-content/uploads/2013/02/2-lr-develop.jpg)

Then the picture as imported in darktable:

[![3-dt-import](http://www.darktable.org/wp-content/uploads/2013/02/3-dt-import-200x100.jpg)](https://www.darktable.org/wp-content/uploads/2013/02/3-dt-import.jpg)

Note that to be closer to the Lightroom rendering I found that decreasing the saturation to 0.90 in the color correction module and adding 0.10 in exposure is a good starting point. This is not done by the exporting module as it is really a matter of taste.
