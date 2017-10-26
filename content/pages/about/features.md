Title: features
Date: 2017-06-13T21:58:51-06:00
Slug: about/features
lede: lede-features.jpg

These are some of darktable's current features, and a coarse overview over the current image operation modules. You can find a more detailed description of every single item in our [online user manual](/usermanual/ "usermanual").

# General

![gold]({attach}gold.jpg "gold")

*   darktable runs on **GNU/Linux / GNOME**, **Mac OS X / macports** and **Solaris 11 / GNOME**.
*   Fully **non-destructive** editing.
*   All darktable core functions operate on **4x32-bit floating point pixel buffers**, enabling SSE instructions for speedups. It offers GPU acceleration via **OpenCL** (runtime detection and enabling) and has **built-in ICC profile** support: sRGB, Adobe RGB, XYZ and linear RGB.
*   A _collect_ module allows you to execute **flexible database queries**, search your images by tags, image rating (stars), color labels and many more. **Filtering and sorting** your collections within the base query or simple tagging by related tags are useful tools in your every-day photo workflow.
*   Import a variety of standard, raw and high dynamic range image formats (e.g. jpg, cr2, hdr, pfm, ... ).
*   darktable has a zero-latency **fullscreen, zoomable user interface** through multi-level software caches.
*   Tethered shooting.
*   darktable currently comes with **21 translations:** Albanian, Catalan, Czech, Danish, Dutch, French, German, Greek, Hebrew, Hungarian, Italian, Japanese, Polish, Portugese (Brazilian and Portugese), Russian, Slovak, Slovenian, Spanish, Swedish, Ukrainian.
*   The **powerful export system** supports Picasa webalbum, flickr upload, disk storage, 1:1 copy, email attachments and can generate a simple html-based web gallery. darktable allows you to export to low dynamic range (JPEG, PNG, TIFF), 16-bit (PPM, TIFF), or linear high dynamic range (PFM, EXR) images.
*   darktable uses both **XMP sidecar** files as well as its **fast database** for saving metadata and processing settings. All Exif data is read and written using libexiv2.


# Modules

![moon]({attach}moon.jpg "moon")

Currently darktable serves 47 image operation modules in L*a*b* and profiled rgb. Some of them can be used as **blending operators** offering blend functionality that works on the incoming image information and the output of the current module.

## Basic image operations:

*   crop and rotate: This module is used to crop, rotate and correct perspective of your image. It also includes many helpful guidelines that assist you using the tools (e.g. rule of thirds or golden ratio).
*   base curve: darktable comes with general enhanced basecurve presets for several models that is per automatically applied to raw images for better colors and contrast.
*   exposure controls: Tweak the image exposure either by using the sliders in the module or dragging the histogram around.
*   highlight reconstruction: This module tries to reconstruct color information that is usually clipped due to information not being complete in all channels.
*   demosaic
*   white balance: A module offering three ways to set the white balance. You can set tint and temperature or you define the value of each channel. The module offers predefined white balance settings as well.
*   invert: A module working on JPEGs inverting colors based on the color of film material.

## Tone image operations:

*   fill light: This module allows the local modification of the exposure based on pixel lightness.
*   levels: This module offers the well-know levels adjustment tools to set black, grey and white points.
*   tone curve: This module is a classical tool in digital photography. You can change the lightness by dragging the line up or down. darktable let you separately control the L, a and b channel. Read in [Ulrich's blog post]({filename}/blog/2012-02-12-mastering-color-with-lab-tone-curves/2012-02-12-mastering-color-with-lab-tone-curves.md "Mastering color with Lab tone curves") how to make use of this feature.
*   zone system: This module changes the lightness of your image. It is based on the Ansel Adams' system. It allows to modify the lightness of a zone taking into account the effect on the adjacent zones. It divides the lightness in a user-defined number of zones.
*   tone mapping: This module allows to recreate some contrast for HDR images.

## Color image operations:

*   overexposed: This module is a useful feature that displays pixels outside dynamic range.
*   velvia: The velvia module enhances the saturation in the image; it increases saturation on lower saturated pixels more than on high saturated pixels.
*   channel mixer: This module is a powerful tool to manage channels. As entry, it manipulates red, green and blue channels. As output, it uses red, green, blue or grey or hue, saturation, lightness.
*   color contrast
*   color correction: This module can be used to modify the global saturation or to give a tint. Read [Johannes' blog post]({filename}/blog/2012-03-11-color-correction/2012-03-11-color-correction.md "color correction").
*   color zones: This module allows to selectively modify the colors in your image. It is highly versatile and allows every transformation possible in the LCh colorspace.
*   color transfer: Transfer colors from one image to another.
*   vibrance: For a detailed description read [Henrik's blog post]({filename}/blog/2011-10-22-different-kind-of-saturation/2011-10-22-different-kind-of-saturation.md "different kind of saturation").
*   input/output/display color profile management

## Correction modules:

*   sharpen: This is a standard UnSharp Mask tool for sharpen the details of an image.
*   equalizer: This versatile module can be used to achieve a variety of effects, such as bloom, denoising, and local contrast enhancement. It works in the wavelet domain, and parameters can be tuned for each frequency band separately.
*   denoise (non-local means): Denoising with separated color / brightness smoothing.
*   denoise (bilateral filter)
*   lens correction: lens defect correction using [lensfun](http://lensfun.sourceforge.net/ "liblensfun").
*   spot removal: Spot removal allows you to correct a zone in your image by using another zone as model.
*   chromatic aberrations: This module automatically detects and corrects chromatic aberrations.
*   raw denoise: Raw denoise allows you to perfom denoising on pre-demosaic data. It is ported from [dcraw](https://www.cybercom.net/~dcoffin/dcraw/ "dcraw").
*   hot pixels: This module allows you to visualize and correct stuck and hot pixels.

## Effects/artistic image postprocessing:

*   watermark: The watermark module provides a way to render a vector-based overlay onto your image. Watermarks are standard SVG documents and can be designed using Inkscape. The SVG processor of darktable also substitutes strings within the SVG document which gives the opportunity to include image-dependent information in the watermark such as aperture, exposure time and other metadata.
*   framing: This module allows you to add an artistic frame around an image.
*   split toning: Original split toning method creates a two color linear toning effect where the shadows and highlights are represented by two different colors. darktable split toning module is more complex and offers more parameters to tweak the result.
*   vignetting: This module is an artistic feature which creates vignetting (modification of the brightness/saturation at the borders).
*   soften: This module is an artistic feature that creates the Orton effect also commonly known as softening the image. Michael Orton achieved such result on slide film by using 2 exposures of the same scene: one well exposed and one overexposed; then he used a technique to blend those into a final image where the overexposed image was blurred.
*   grain: This module is an artistic feature which simulates the grain of a film.
*   highpass: This module acts as highpass filter.
*   lowpass: This module acts as lowpass filter. One use case is described in [Ulrich's blog post]({filename}/blog/2012-02-13-using-lowpass-filter-to-recover-shadows/2012-02-13-using-lowpass-filter-to-recover-shadows.md "Using lowpass filter to recover shadows").
*   monochrome: This module is a quick way to convert an image to black and white. You can simulate a color filter in order to modify your conversion. The filter can be changed in size and color center.
*   lowlight vision: Low light module allows to simulate human lowlight vision, thus providing the ability to make lowlight pictures look closer to reality. It can also be used to perform a day to night conversion.
*   shadows and highlights: Improve images by lightening shadows and darkening highlights. Read [Ulrich's blog post]({filename}/blog/2012-02-17-shadow-recovery-revisited/2012-02-17-shadow-recovery-revisited.md "Shadow recovery revisited") on this.
*   bloom: This module boost highlights and softly blooms them over the image.
*   colorize
*   graduated density: This module aims at simulating a neutral density filter, in order to correct exposure and color in a progressive manner.

