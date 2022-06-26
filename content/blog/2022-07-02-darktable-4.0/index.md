---
title: "darktable 4.0: 3763 Days Later"
author: the darktable team
slug: darktable-4.0
date: 2022-07-02
lede: sky.jpg
lede_author: AxelG
tags:
  - announcement
  - darktable-release
---

_Translations of this article: [German](https://www.bilddateien.de/blog/2022-07-02-darktable-4-0.html)._

A little over 10 years since darktable 1.0 was first released, the darktable team is proud to present darktable 4.0!

For a complete changelog, please see the [release notes](https://www.darktable.org/2022/07/darktable-4.0.0-released/).

## Color and Exposure Mapping

In both the [exposure](https://docs.darktable.org/usermanual/4.0/en/module-reference/processing-modules/exposure/#spot-exposure-mapping) and [color calibration](https://docs.darktable.org/usermanual/4.0/en/module-reference/processing-modules/color-calibration/#spot-color-mapping) modules you can now define and save a target patch of the image using color pickers, allowing you to match any source object in the image against an arbitry target color/exposure. This can be used, for example, to perform white balance (chromatic adaptation) against non-grey objects of known color, or to ensure color and exposure consistency of an object across a series of pictures. A "sampling" mode lets you pick a reference color in the image, recording the output color after the current exposure and color calibration modules respectively. Then, the "correction" mode computes the relevant exposure and color calibration settings so as to match the color selected from the color-picker against the target acquired from the sample. The target can also be manually defined by direct input of the appropriate CIE Lab 1976 color coordinates.

This feature was developed because copying and pasting an editing history over a series of pictures, even when shot in the same conditions, does not necessarily ensure uniform color rendition, and often still requires additional manual adjustment, since lighting may still slightly vary from image to image. From a single reference edit, the mapping feature ensures that the parameters scale properly to the rest of the series. Note that this color matching will still not be enough to ensure a completely identical perceptual sensation across images, since perception is also dependent on the distribution of lightness in the image: a landscape that is 1/3 bright sky and 2/3 dark ground will not yield a color perception similar to a landscape with inverted sky/ground proportions, even though the color grading is the same and a colorimeter records the same values.

## Color Glossary in the Global Color Picker

The [global color picker](https://docs.darktable.org/usermanual/4.0/en/module-reference/utility-modules/darkroom/global-color-picker/), in the darkroom view's left panel, now displays the name of the picked color in the tooltip. This feature was requested by several color-impaired photographers to assert the perceptual validity of their editing regarding colors they don't see in the same way as an average observer.

The color vocabulary contains 76 entries: 15 hues × 5 lightnesses + neutral (grey). It does not separate across the chroma axis, so all colors are registred the same no matter their colorfulness.

Additionally, the vocabulary includes average skin colors for 3 body parts (forearm, forehead and cheek) of 6 ethnicities (Chinese, Thai, Kurdish, Mexican, Caucasian, African-American). These values come from the academic databases of cosmetology and dermatology available at the time of programming. They are only valid for a D65 illuminant, and for an exposure setting anchoring diffuse white at 92% relative luminance. Note that the skin type is returned at 95% confidence, and there is a significant overlap in skin color between ethnicities, so this tool is meant to ensure that a source color matches an average human skin ± 2 standard deviations, but does not infer the most probable ethnicity of someone.

## Filmic Version 6

The [filmic rgb](https://docs.darktable.org/usermanual/4.0/en/module-reference/processing-modules/filmic-rgb/) module gets new color science in version 4.0. As part of this work the mandatory desaturation (close to medium white and black) is removed and replaced with a true gamut mapping against the output (or export) color space. This gamut mapping is performed using the ICC "relative colorimetric" intent, where we clip chroma to the maximum allowed in the output space at constant lightness and hue. This will allow for more saturated colors, particularly noticeable in blue skies.

For users who still prefer the "desaturated highlights" look, the variant without chroma preservation (processing RGB channels independently) does still allow it, but version 6 adds a hue handcuff to prevent the traditional hue shift that comes with this method (where saturated blue skies degrade to cyan and saturated red to yellow).

Out-of-gamut colors typically result from colors that have a saturation that is too high for their luminance level, and therefore cannot be digitally encoded in bounded integer RGB spaces nor physically displayed on output media. This piece of gamut sanitization is the third and last to be added to darktable, which now has a fully sanitized color pipeline, from input (color calibration) to output (filmic v6), via artistic changes (color balance RGB). Users can now color-grade pictures safe in the knowledge that invalid input colors can be recovered in the least destructive fashion possible early in the pipeline, and valid colors can't be pushed out of gamut along the pipeline.

Note that legacy (display-referred) modules are applied after filmic in the pipeline. These modules will not benefit from filmic's gamut mapping and will rely on LittleCMS2 (if enabled) at the final export stage, which does not gamut map as it should. Also, since filmic v6 desaturates much less than v5 (only when colors would fall out of gamut) and preserves chromaticity by default, it will preserve invalid colors as well (clipped magenta highlights, chromatic aberrations) and will hide them less than before. Such colorful artifacts will need to be properly corrected with the relevant modules beforehand.

## Introducing the darktable Uniform Color Space 2022

The [color balance RGB](https://docs.darktable.org/usermanual/4.0/en/module-reference/processing-modules/color-balance-rgb/) module uses a saturation algorithm that was designed to simulate color shading as done traditionally by painters, meaning rich colorful colors degrade to light pastels, and pastels degrade to pure primary colors. This implies that some darkening needs to happen along with the saturation boost, and some brightening needs to happen along with any desaturation. This is unlike most "saturation" operators that act over chroma at constant lightness and may degrade saturated colors to a seemingly-fluorescent version of themselves, looking particularly wrong on reflective objects.

So far, a custom saturation method involving use of the JzAzBz (2017) perceptually-uniform color space had been used in color balance RGB. This has proven to lack smoothness and darkened too much for the amount it resaturated. Also, the JzAzBz color space doesn't account for the [Helmholtz-Kohlrausch effect](https://en.wikipedia.org/wiki/Helmholtz%E2%80%93Kohlrausch_effect), which makes colors of high chroma appear brighter than their low-chroma equivalent, even when their lightness (or luminance) is constant.

A [3-months research project](https://eng.aurelienpierre.com/2022/02/color-saturation-control-for-the-21th-century/) has led to the creation of a new perceptually uniform color space designed specifically for the needs of the color balance RGB module's saturation algorithm. This color space is the second "practically usable" published space that accounts for the contribution of colorfulness to the perception of brightness (Helmholtz-Kohlrausch effect), and was fitted on top of the Munsell renotation experimental dataset from 1943 (40 observers, 3 millions observations). To quantify the Helmholtz-Kohlrausch effect, four different brightness-chroma experimental datasets from 1963 to 2013 were used, a total of 29 observers for 154 color samples. It took 26 hours for a computer to find the best fit by optimizing 23 parameters.

Altough this changes nothing from a GUI perspective, the saturation should be smoother to control, more perceptually-even across hues and yield a better saturating/darkening ratio. As with the previous method, it will prevent the degradation of colors toward fluorescent or neon. The previous JzAzBz variant is still available in the module as an option and will also be retained for old edits.

This perceptual space finally allows for a more accurate and computationally-efficient way to express the gamut of the working RGB space, which allows for gamut-mapping colors smoothly at constant brightness and hue, and will allow users to push saturation by large amounts without having to fear the consequences of gamut clipping (non-smooth hue shifts).

This research has been made possible solely by [crowdfunding](https://liberapay.com/aurelienpierre/) of the developer. The source code (Python, C, OpenCL) of the space has been released under a very permissive MIT license.

## Guided Laplacian Highlight Reconstruction

Highlight reconstruction has long been a major pain-point in darktable, made even more obvious by the scene-referred workflow and chroma preservation.

The new guided laplacian reconstruction method in the [highlight reconstruction](https://docs.darktable.org/usermanual/4.0/en/module-reference/processing-modules/highlight-reconstruction/) module is a spin-off from the [diffuse or sharpen](https://docs.darktable.org/usermanual/4.0/en/module-reference/processing-modules/diffuse/) module introduced in darktable 3.8. It uses the same iterative and multi-scale wavelet scheme to extract valid details from any non-clipped RGB channel(s) and uses these valid details to guide the reconstruction of clipped channels. The module then propagates color gradients from neighbouring valid regions, using edge-aware color diffusion that limits color bleeding through edges (preventing green leaves from bleeding color into the reconstruction of clipped blue sky, for example). It benefits from not relying on any perceptual definition of color and being immune to white balance, and yields smooth reconstructions, though it is efficient only for spotlights or simple shapes over small areas. For larger clipped areas, it may fail to entirely remove the magenta color and, for complex shapes, it may create strange patterns and color bleeding. In these situations, the filmic module's highlight reconstruction is to be preferred or used as a complement, since it has a more basic and robust way of in-painting color.

An additional noise setting allows you to add Poisson noise (the natural type of noise affecting the collection of photons) into reconstructed highlights, to help blending them into noisy high-ISO images where smooth color gradients would immediately de-tone.

As with any reconstruction method attempting to infer damaged content from analysis of the neighborhood, this method comes with a number of assumptions and trade-offs. The first caveat is its computational price, which will require a GPU to run in reasonable timescales -- the computational time increases with the radius of reconstruction. For this reason, the default settings assume fairly small radii, meaning that large blown-out areas will not be reconstructed properly until you adjust settings manually. The second caveat is that this method does not use a perceptual framework, since it works before any color profiling or calibration (and even prior to demosaicing in the pipe) so it cannot rely on a definition of white that would allow it to simply desaturate highlights to avoid magenta. For this reason, other methods may work better for very large blown-out areas, and the filmic module's highlight reconstruction may be needed in order to force a desaturation to white. In addition, since it in-paints the damaged parts of the image, this method will make the sun disc disappear into the rest of the sky for sunset scenes, because it enforces a smooth reconstruction. Masking may be needed to exclude the sun or the moon to prevent it from vanishing into the sky.

Finally, this method is only available for Bayer sensors -- is not possible to adapt directly to X-Trans sensors due to their non-uniform pattern.

## Speed-ups and Optimizations

The stress-test inflicted on the pixel pipe by resource-intensive modules such as "diffuse or sharpen" have revealed bugs and shortcomings in the way the memory was handled on GPU by OpenCL drivers. The code planning and memory allocation for GPUs has therefore been corrected and almost entirely rewritten. The tiling strategies for X-Trans demosaicing and retouch modules have been fixed.

New "user friendly" planning strategies for GPU memory use have been added in the global preferences, allowing users to minimize memory use and/or memory read-write cycles, and can now be changed at runtime without requiring a restart. The power-user OpenCL optimizations (compilation flags and memory sizes) can now be tuned for each OpenCL device independently.

The wavelet decompositions used in filmic's highlights reconstruction, diffuse or sharpen, and the guided laplacian highlights reconstruction have been rewritten for better performance (15 to 25% faster).

## Darktable 4.2

As usual, the next feature release is already in development. Here are a couple of features you can expect to find under the Christmas tree this year...

A CYM channel-mixer is being developed, to allow users to digitally restore scans of damaged prints and films. Since dyes and pigments don't age at the same rate, their colors shift -- usually towards red. However, the current toolset of darktable, centered around an additive RGB framework, doesn't play well with subtractive CYM(K) media and this needs a proper display-referred CYM tool.

A [color equalizer](https://github.com/darktable-org/darktable/pull/12082) is also in development, as rewrite of the existing color zones module, compatible with HDR signals and using the new darktable Uniform Color Space 2022, with a simplified GUI, built-in gamut mapping against pipeline RGB space and a protection against chroma noise. It will complement the color balance RGB module for minor and fine-grained color tweaks like replacing some colors.
