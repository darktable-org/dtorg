---
author: dt
comments: true
date: 2011-05-23 21:36:18+00:00
layout: post
link: /2011/05/gsoc-2011-starts-today/
slug: gsoc-2011-starts-today
title: "GSOC 2011 Starts Today"
wordpress_id: 451
tags:
  - GSoC
---
Today I’ll be starting on my Summer of Code project for darktable, so I thought I’d start off with a blog post about just what I’ll be doing. This Summer I’ll be focusing on UI improvements in darktable, and I have four separate tasks to complete, in this order.

1. **Removing the libglade dependence.**

    There are two ways to construct a graphical interface in software: one is to build your interface one element at a time in your source code, and the other is to use a graphical tool to build a description of your desired interface that you can use a library (libglade in our case) to construct when the program actually runs. Currently, darktable uses both techniques. Much of the user interface is provided by libglade, but some elements are also created in code. My first task for the Summer will be to remove this dependence on libglade and construct the entire interface entirely in code. You won’t see any changes in the UI as a direct result of this, but it should make it easier for other developers going forward to make modifications to the user interface.


2. **Reworking the keyboard input system.**

    Currently, the different modules in darktable create their own keyboard shortcuts by directly making calls to the user interface library (GTK+). This is problematic for several reasons: from a user’s perspective, there’s no way ** **remap the shortcuts unless a module gives you a means to do so. You also have no way of preventing different modules from setting up keyboard shortcuts that conflict with each other, or determining whether a shortcut is local to that module or global to the entire application.

    I aim to replace the tradition of modules creating keyboard shortcuts directly with modules instead registering their shortcuts with darktable, and allowing darktable itself to detect executed shortcuts and decide which modules to notify. I’ll build a control panel for users which will allow you to view all the different shortcuts registered in the system and change them if you want. GIMP has a control panel like this, which is what I aim to recreate in darktable.

3. **Fixing up the color picker.**

    The color picker is currently a little bit confusing, and not as useful as in many other applications. While I haven’t determined exactly what the new color picker interface will look like (I’ll be working with the community to determine what would be most beneficial to the most users), I do have some definite goals in mind. It should allow easy sampling of individual pixels or areas, with the ability to view samples in different color spaces and save them for later reference. I also plan to allow the user to make color samples show up as vertical bars on histogram and curves displays, making it easy to determine just which part of the curve or histogram you need to manipulate to target a particular area in the image.


4. **Adding a levels tool.**

    My final change will be relatively minor compared to the rest, but useful nonetheless. darktable currently allows image manipulation through curves, but no equivalent to the levels tool found in most image editors. My plan is to add the levels tool as an alternative view to the curves tool, which will automatically set a curve that clips and/or modifies the intensity in the desired ranges.

With any luck, these changes will proceed smoothly and I’ll find myself with some extra time at the end of the Summer to tackle some additional modifications as well. I’ll be starting work today on the first task, and my progress will be visible in the “bieber” branch of the darktable git repository. I’ll also make periodic updates to the mailing list and this blog to keep the community informed of my progress. Please, don’t hesitate to let me know if you have comments, suggestions or criticisms of my work.


