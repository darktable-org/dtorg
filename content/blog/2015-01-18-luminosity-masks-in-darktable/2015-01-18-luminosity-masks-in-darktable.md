author: mueen
comments: true
date: 2015-01-18 20:43:58+00:00
layout: post
link: http://www.darktable.org/2015/01/luminosity-masks-in-darktable/
slug: luminosity-masks-in-darktable
title: Luminosity Masks in darktable
lede: lmaskdtyellow_wide.jpg
wordpress_id: 3473
tags: blog

Pat David has a great [blog](https://blog.patdavid.net/) on photoediting in [GIMP](https://www.gimp.org/). I recently read his [post](https://blog.patdavid.net/2013/11/getting-around-in-gimp-luminosity-masks.html) on luminosity masks and was fairly impressed. Can darktable do something similar? Yes&nbsp;– they're a special case of [parametric masks](/usermanual/en/parametric_mask.html).

I thought I'd post a quick tutorial on luminosity masks using parametric masks. First, I strongly suggest you read Pat David's [post](https://blog.patdavid.net/2013/11/getting-around-in-gimp-luminosity-masks.html) and thoroughly understand what's going on.

A quick and simplistic explanation follows: Normally, if we make a selection and, say, adjust the brightness dramatically in that selection, we get a sharp (and ugly) transition near the edge of the selection:

@![sharpedge](sharpedge.png)

The quick solution is to blur the mask (feathering in GIMP). Feathering simply makes the transition less sharp:

@![sharpedge1](sharpedge1.png)

Better, but still too sharp a transition. You can feather it even more if you wish, but however much you feather it, the transition is determined too heavily by your choice of selection (a rectangle in this case). We'd really like is a way to select based on the actual _contents_ of the image.

What luminosity masks do is let you select regions in your image in proportion to their brightness. So the L layer in Pat's article fully selects completely bright pixels, and only partially selects pixels that are half as bright, and doesn't select pixels that are not bright at all. When you now brighten the image, the effect of the brightening is greatest on the brightest pixels, and least on the darkest pixels. There are no sharp transitions like what I have in my screenshots above.

In that sense, some refer to these masks as _self-feathering_.

So how can we do this in darktable?

Consider the following image:

@![baseimage](baseimage.jpg)

Let's say I want to brighten it. Let me apply an aggressive curve:

@![curve](curve.png)

The result is:

@![fullbrighten](fullbrighten.jpg)

Let's use this as a "control" for the effect of luminosity masks.





## The L mask


Using Pat's technique, let's look at the L mask in GIMP:

@![lmaskgimp](lmaskgimp.png)

Brighter areas mean they are "more" selected. This means any operation we perform on the image will be applied more on the brighter pixels.

How do we get this in darktable?

Go to the Tone Curve module, set blend to parametric mask. Now comes the important part: In the Input sliders, select the _top left_ triangle and move it all the way to the right:

@![lmaskdt](lmaskdt.png)

The resulting mask looks like:

@![lmaskdtyellow](lmaskdtyellow.png)

What did I do here? To fully understand it, you should read the [parametric masks](/usermanual/en/parametric_mask.html) page in the darktable manual. By sliding the upper left triangle all the way to right, I told it to _fully_ select the brightest pixels, _not_ select the darkest pixels, and do a linear interpolation for all the intermediate pixels (so a 50% bright pixel is "half" selected).

Another way of looking at it: Apply the module to all the pixels, but apply an opacity on each pixel depending on its luminosity.

How does the image look with the same curve as before?

@![lbrightendt](lbrightendt.jpg)



## The D Mask


To create the D mask, Pat selected the whole image, and subtracted the L channel from it.

In darktable, we simply do the opposite of what we did for the L mask. We now move the _top right_ triangle to the extreme left:

@![dmaskdt](dmaskdt.png)

The mask now looks like:

@![dmaskdtyellow](dmaskdtyellow.png)

The result of the curve:

@![dbrightendt](dbrightendt.jpg)



## The M Mask


What about medium? Let's try:

@![mmaskdt](mmaskdt.png)

Here we moved both the upper triangles to the center.

The resulting image is:

@![mtoobright](mtoobright.jpg)

This is too strong! If I do the same using Pat's luminosity masks in GIMP, I get:

@![mbrightengimp](mbrightengimp.jpg)

This is not as strong as the darktable version. What went wrong?

If we read Pat's description, what he does is intersect the D and L channels. This results in the middle bright pixel only being 50% selected. In our darktable version, we have it 100% selected. So we compensate by setting the opacity to 50% and we get very similar results to GIMP.

The resulting mask is:

@![mmaskdtyellow](mmaskdtyellow.png)




## The Other Masks


What about the DD mask?

This is obtained by subtracting the L channel from the D mask. The equivalent mask in darktable is:

@![ddmaskdt](ddmaskdt.png)

This is the same as the D mask, but notice I moved the lower right triangle half way to the left. This has the effect that anything that is more than 50% bright will not be selected _at all_.

The resulting mask is:

@![ddmaskdtyellow](ddmaskdtyellow.png)

If we wanted DDD, we'd move the lower triangle two thirds of the way instead of half.



## Technical Details


Why did this work? Let's jump into the math:

Let the luminosity of a pixel be denoted by $lp$. A value of 1 means fully bright, 0 means fully dark, and 0.5 means 50% bright. In the L mask, $lp$ gives the percentage selection directly (1 means fully selected, 0.5 means half selected, etc).

To get the D mask, we select the whole image (which means each pixel is _fully_ selected), and subtract the luminosity from it. Thus, in the D mask, the "selectedness" is $1-lp$. So if $lp$ was very bright (close to 1), it is now barely selected, as $1-lp$ will be a small number close to 0. Similarly, if it was originally very dark (close to 0), $1-lp$ is now close to 1 and it is almost fully selected.

Does my darktable D mask translate to the same thing? Yes, as I believe darktable does a linear interpolation.

What about the DD mask? Pat obtained it by subtracting the L channel from the D channel. In terms of our equations, this is just $1-2lp$. Note that if $lp \geq 0.5$, (greater than 50% brightness), then $1-2lp \leq 0$, which means it is not selected at all. Only pixels less than 50% brightness are selected in this mask.

Again, my darktable DD mask translates to the same mask, as I cut it off at 0.5. Since darktable uses linear interpolation, the slope from 0.5 to 0 will be double the slope I had in D. Hence, the factor of 2 in $1-2lp$.

I'm assuming the M mask translates as well but I'm not 100% sure what the algorithm GIMP uses to perform intersection.



## Summary


So there you have it: Luminosity masks in darktable.

But we do not need to constrain ourselves to the "usual" luminosity masks. We can fiddle with the triangles a little more to get many different kinds of masks. Moreover, our masks need not merely be _luminosity_ masks. We can apply this logic to the hue, a and b channels (or R, G and B channels for the modules that work in RGB space). Or do a combination of both! Usually when I have  mask, I couple luminosity with one of the color channels for a more refined selection.

The important message, though, is that we can easily avoid sharp transitions by varying the upper and lower triangles independently.

For more on luminosity masks, I strongly recommend [Tony Kuyper's tutorials.](http://goodlight.us/writing/tutorials.html)

An earlier version of this article appeared [here.](http://blog.nawaz.org/posts/2015/Jan/luminosity-masks-in-darktable/)


