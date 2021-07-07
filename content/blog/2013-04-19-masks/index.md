---
author: alicvb
comments: true
date: 2013-04-19 09:05:43+00:00
layout: post
link: /2013/04/masks/
slug: masks
title: "masks"
lede: example_end_wide.jpg
lede_author: Aldric Renaudin
wordpress_id: 2884
tags:
  - blog
  - development
  - upcoming feature
---
In darktable, selective editing was a long awaited feature. Our development version now allow limiting module effects to a region of the image.

Remember the old times, the red light of the darkroom, the smell of the developing bath ...

Remember when you were using your hands or a small piece of cardboard to achieve some masking ...

Now you can do that in darktable.

# example

let take this photo as an example.

![example_ini](example_ini.jpg)

Here, we will get rid of the fluorescent orange wall. We will use the color zone module to desaturate reds, but doing so would also desaturate the lighthouse railings. We will use masks to avoid that.

![example_desaturate](example_desaturate.jpg)

we now add a masks to limit the effect of the module to the wall only. Using the masks combobox from the module, we add a curve shape:

![example_curve](example_curve.jpg)

And here is our final image:

![example_end](example_end.jpg)

# masking interfaces

The masks combobox inside modules let you add new shapes, reuse existing shapes. But if you want to perform more complex tasks, you will have to use the masks manager which is in the left panel:

![manager](manager.png)

Right-clicking on a shapes will open a popup menu with all the possible actions.

# editing shapes

Two shapes types have been implemented: the simple circle (with feathering borders) and the more powerful curve shape. Here's some tips to help you in shape creation:

circle & curve:

* you can change the radius of the circle by using the mousewheel within the circle.
* you can set the border size by using the mousewheel between the circle and the border

curve:

* you can add control points by shift+clicking on an existing curve
* you can remove corners by right-clicking on them
* clicking on an existing control point will select it, allowing you to move it and making control-hooks appear that allow you to change the sharpness of the point
* right-clicking on a control hook will reset it.
* when creating a shape, you can press ctrl while adding control-points to add a sharp corner directly
* you can use the scrollwheel to change the border width of the whole shape
* the border width can also be set separately at each control point using the available anchors.

# Advanced tips

* combining masks and blendif offers a whole new world of possibilities
* when a shape is assigned to a module, a group of shapes is automatically created. You can use that group to build complex combinations of shapes
* shapes can be moved and combined within a group using boolean operators: union, intersection, difference and exclusion
* opacity can be set per-shape using ctrl+wheel

# Cloning

The spot removal module is not limited to circles anymore. It can use any shape for advanced cloning.

# Warning

masks are only available in the development branch of darktable. We wanted to share with you the awesome features that are coming but installing the development version of darktable isn't a trivial thing. Do not use this on production work.

Masks still have some known limitations

* there is no brush painting. masks are currently limited to curves
* very complex, self-intersecting curves might not render correctly

_Note: again, great thanks to Jeremy Rosen for his help in the writing of this blog post_
