author: bieber
comments: true
date: 2011-07-30 21:22:56+00:00
layout: post
link: http://www.darktable.org/2011/07/introducing-the-levels-module/
slug: introducing-the-levels-module
title: Introducing The Levels Module
wordpress_id: 426
tags: GSoC

<figure markdown="span" class="u-pull-left">
![Screenshot]({attach}Screenshot.png)
</figure>

For my final GSOC 2011 task, I set out to build a levels module for darktable, which would behave more or less like the levels tool in GIMP and similar image editors.  The user sets a white point, black point, and middle grey point for their image on a histogram, and the tool adjusts the image to match the chosen boundaries.  In my git branch, I now have the levels module functional.

The interface for the levels module looks very similar to that of the tone curve module.  This is no coincidence: I got started on this task by copying the source files for the tone curve module and modifying them to fit my needs.  Interface-wise, the histogram, grid, and drag handles at the bottom are all identical to tone curve, but I removed the curve and added the vertical indicator lines.

To operate the levels tool, you simply click and drag the vertical lines which represent (from left to right) the black point, grey point, and white point of your image.  Whenever your mouse is over the module’s space, whichever line the pointer is closest to will light up.  Clicking and dragging will always move the highlighted line.  When moving the white or black point, the grey point will also move to keep the same ratio between white, black, and grey that you initially started with.  Keep in mind that the lines must always remain a minimum distance from each other (about 5% of the width of the histogram).  This is to make sure you can always easily select the correct handle to move.

Once you’ve made your selections, whatever range you have selected will be adjusted to fill the entire dynamic range of the image, and relative brightness within that range will be determined by your chosen grey point.  In the example pictured (a black and white print that I photographed), you can see that the levels tool has expanded the relatively narrow dynamic range of the original photo out to fill the entire available range.  This provides a simple method for removing empty spaces at the low or high ends of your dynamic range.  You can also use it to easily drop an almost-black background to pure black, or clip a not-quite-white background to proper white.

