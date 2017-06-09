author: upegelow
comments: true
date: 2012-07-11 17:08:50+00:00
layout: post
link: http://www.darktable.org/2012/07/some-enhancements-to-conditional-blending/
slug: some-enhancements-to-conditional-blending
title: Some enhancements to conditional blending
wordpress_lede: IMG_4287x_0004.jpg
wordpress_id: 1862
tags: blog, community, development, blending, color, conditional, darktable, Lab, monochrome, saturation

Conditional blending, also known as "blend if", is a feature which is currently under development in our master branch. A general description of the idea together with some examples can be found [here](http://www.darktable.org/2012/03/upcoming-features-conditional-blending/). In short, conditional blending allows you to limit the effect of a module to certain pixels of an image, determined by their color coordinates. For modules in Lab space, you can restrict the effect of a module depending on the pixel’s L, a, and b value. For modules in RGB space, you can restrict the effect of a module depending on color channels Red, Green, and Blue plus a Gray value.

Today I’d like to describe a few recent extensions to conditional blending. All of them have the aim to give users better control to which of the pixels a module should be applied and to which not. These extensions can be found in branch _blendif_ and should soon be merged into master.


# New channels with chroma and hue characteristics


Although images normally only have three real data channels (L, a, b and R, G, B, respectively) we can define additional virtual channels and use them to better select a range of pixels. These virtual channels are calculated on a per-pixel basis only for the purpose of conditional blending. The already existing Gray channel in conditional blending of RGB modules is an example.

Modules in Lab color space now got two additional channel tabs "C" and "h". They stand for chroma (saturation) and hue in the _LCh_ color space - a color space closely linked to Lab. Chroma C goes from 0 (unsaturated) to 100 (maximum saturation). In real images you will hardly find pixels with a C value above 50. Hue is a parameter which describes a color circle with all possible colors at a given lightness and saturation. We express it in degrees from 0 to 360. The gradient of the slider will tell you where a certain color is to be found. You can also use the color picker to take up chroma and hue from any spot of your image.

Modules in RGB color space received three additional tabs "hue", "chroma" and "value", coming from an HSL color description. H (= hue) goes from 0 to 360 degrees and S (= chrom/saturation) from 0 to 100. Please note that measures for hue and chroma in _HSL_ are different from the ones in LCh. A high value for S (close to 100) is not uncommon for RGB images; that’s different from parameter C in Lab modules. Channel "value" is just another parameter for lightness - it’s added here for convenience reasons.


# New option to toggle polarity


In the previous implementation of conditional blending it was easy to select a (narrow) range of values where a module should be blended in, while all other pixels are being left alone. However, it was difficult or impossible to do the opposite - define a band of values, where a module should not be blended in.

Now you can change the polarity of each slider by an additional toggle button. A positive polarity is equivalent to the already known behavior. Switching to a negative polarity allows you to define a band of values where a module is not blended; all pixels which do not fall into this range can take effect from the module.


# A poppy blossom


Let’s go for an example. I took this photo of a poppy blossom because I liked the strong color contrast effect. As the flower grows in front of a pile sun-bleached dead wood, it receives a strong accent to its intense, lively red.

[![](http://www.darktable.org/wp-content/uploads/2012/07/IMG_4287x_0001.jpg)](http://www.darktable.org/2012/07/some-enhancements-to-conditional-blending/img_4287x_0001/)

On the problematic side remains a somewhat low contrast within the blossom. The petals appear a bit like a red blob, a typical problem of unprocessed raw images. The droplets, which the last shower of rain has left behind, are hardly discernible. Admittedly the blossom is a bit soft too, probably due to sloppy focusing on my side.

OK, there are a few modules in darktable which we could take to improve the image. Darktable’s swiss knife _equalizer_ comes to mind, or module _highpass_ combined with a suited blend mode.

I took highpass with blend mode _soft light_ in this case as it will increase contrast and sharpness, easily controlled with only two sliders. As described, I want to apply the module only to the red petals of the poppy flower; that’s why I need conditional blending.

Module highpass works in Lab mode and it would certainly be possible to select the right part of the images with the L, a, and b sliders. However, this is much easier done with channels C and h. Just take the color picker to identify the hue of the blossom and select a narrow band around this hue value. Then in addition limit the effect in chroma channel to the more saturated colors.

[![](http://www.darktable.org/wp-content/uploads/2012/07/blendif2-1.jpeg)](http://www.darktable.org/2012/07/some-enhancements-to-conditional-blending/blendif2-1/)[![](http://www.darktable.org/wp-content/uploads/2012/07/blendif2-2.jpeg)](http://www.darktable.org/2012/07/some-enhancements-to-conditional-blending/blendif2-2/)

With the recently added _display mask_ option, it’s now very easy to see what gets blended and what not. The yellow color shows you that we really only selected the petals of the poppy, everything else remains unaffected.

[![](http://www.darktable.org/wp-content/uploads/2012/07/blendif2-3.jpeg)](http://www.darktable.org/2012/07/some-enhancements-to-conditional-blending/blendif2-3/)

Here is the resulting image with some additional contrast enhancement.

[![](http://www.darktable.org/wp-content/uploads/2012/07/IMG_4287x_0002.jpg)](http://www.darktable.org/2012/07/some-enhancements-to-conditional-blending/img_4287x_0002/)

Now let’s assume we would want to turn this natural almost-colorkey image into a full colorkey (just for demonstration purposes; personally I do not like colorkey in most cases).

If we want to gray out all parts of the image except of the petals, we can use our monochrome module and use blendif’s new polarity option. Again we define a narrow band around the red hue of the blossom but this time with inverted polarity.

[![](http://www.darktable.org/wp-content/uploads/2012/07/blendif2-4.jpeg)](http://www.darktable.org/2012/07/some-enhancements-to-conditional-blending/blendif2-4/)

Here is the result of our exercise:

[![](http://www.darktable.org/wp-content/uploads/2012/07/IMG_4287x_0003.jpg)](http://www.darktable.org/2012/07/some-enhancements-to-conditional-blending/img_4287x_0003/)

When exporting images with highly saturated colors like this – where colors are relevant for the message of the image - you might experience some disappointment. If you have a wide gamut monitor like me and then export into a JPEG in sRGB color space, part of the color variation you achieved may get lost again. That’s because saturated colors may be well within the gamut of your monitor, but are already out of gamut for sRGB. Choosing AdobeRGB as output profile combined with a different output intent (like _relative colorimetric_ instead of perceptual) in darktable’s _output color_ module can help to improve the situation.
