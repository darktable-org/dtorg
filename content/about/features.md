---
Title: features
Date: 2017-06-13T21:58:51-06:00
lede: lede-features.jpg
lede_author: <a href="https://jo.dreggn.org/home/">jo</a>
weight: 2
menu: "footer"
---
Here is a short list of highlights where darktable can improve your digital photography processing workflow and help you to make better images with less effort. You can find a more detailed description of every single item in our [online user manual](https://www.darktable.org/usermanual/3.6/en/ "usermanual").

# General Features

![gold](../gold.jpg "gold")

*   **Non-destructive** editing throughout the complete workflow, your original images are never modified.
*   **Take advantage of the real power of raw**: All darktable core functions operate on **4x32-bit floating point pixel buffers**, enabling SSE instructions for speedups.
*   **GPU accelerated image processing**: many image opertions are lightning fast thanks to  **OpenCL** support (runtime detection and enabling).
*   **Professional color management**: darktable is fully color managed, supporting automatic display profile detection on most systems, including built-in ICC profile support for sRGB, Adobe RGB, XYZ and linear RGB color spaces.
*   **Cross platform**: darktable runs on Linux, Mac OS X / macports, BSD, Windows and Solaris 11 / GNOME.
*   **Filtering and sorting**: search your image collections by tags, image rating (stars), color labels and many more, use flexible database queries on all metadata of your images.
*   **Image formats**: darktable can import a variety of standard, raw and high dynamic range image formats (e.g. JPEG, CR2, NEF, HDR, PFM, RAF ... ).
*   **Zero-latency, zoomable user interface**: through multi-level software caches darktable provides a fluid experience.
*   **Tethered shooting**: support for instrumentation of your camera with live view for some camera brands.
*   **Speaks your language**: darktable currently comes with **21 translations:** Albanian, Catalan, Czech, Danish, Dutch, French, German, Greek, Hebrew, Hungarian, Italian, Japanese, Polish, Portuguese (Brazilian and Portuguese), Russian, Slovak, Slovenian, Spanish, Swedish, Ukrainian.
*   **Powerful export system** supports Piwigo webalbums, disk storage, 1:1 copy, email attachments and can generate a simple html-based web gallery. darktable allows you to export to low dynamic range (JPEG, PNG, TIFF), 16-bit (PPM, TIFF), or linear high dynamic range (PFM, EXR) images.
*   **Never lose your image development settings** darktable uses both **XMP sidecar** files as well as its **fast database** for saving metadata and processing settings. All Exif data is read and written using libexiv2.
*   **Automate repetitive tasks**: Many aspects of darktable can be scripted in Lua.

# Modules

![moon](../moon.jpg "moon")

Currently darktable contains 61 image operation modules. Many modules support powerful **blending operators** offering blend functionality that works on the incoming image information and the output of the current module or be used with drawn masks.

## Basic image operations:

*   contrast, brightness, saturation: Quickly tune your image using this simple module.
*   shadows and highlights: Improve images by lightening shadows and darkening highlights. Read [Ulrich's blog post](/2012/02/shadow-recovery-revisited "Shadow recovery revisited") on this.
*   crop and rotate: This module is used to crop, rotate and correct the perspective of your image. It also includes many helpful guidelines that assist you using the tools (e.g. rule of thirds or golden ratio).
*   base curve: darktable comes with general enhanced basecurve presets for several models that are automatically applied to raw images for better colors and contrast.
*   exposure controls: Tweak the image exposure either by using the sliders in the module or dragging the histogram around.
*   demosaic: You have the choice between several demosaicing methods when editing raw files.
*   highlight reconstruction: This module tries to reconstruct color information that is usually clipped due to information not being complete in all channels.
*   white balance: A module offering three ways to set the white balance. You can set tint and temperature or you define the value of each channel. The module offers predefined white balance settings as well. Or just pick a neutral region in the image to balance for that.
*   invert: A module inverting colors based on the color of film material.

## Tone image operations:

*   fill light: This module allows the local modification of the exposure based on pixel lightness.
*   levels: This module offers the well-known levels adjustment tools to set black, grey and white points.
*   tone curve: This module is a classical tool in digital photography. You can change the lightness by dragging the line up or down. darktable lets you separately control the L, a and b channel. Read in [Ulrich's blog post](/2012/02/mastering-color-with-lab-tone-curves "Mastering color with Lab tone curves") how to make use of this feature.
*   zone system: This module changes the lightness of your image. It is based on the Ansel Adams system. It allows to modify the lightness of a zone taking into account the effect on the adjacent zones. It divides the lightness in a user-defined number of zones.
*   local contrast: This module can be used to boost details in the image.
*   two different tone mapping modules: These modules allow to recreate some contrast for HDR images.

## Color image operations:

*   velvia: The velvia module enhances the saturation in the image; it increases saturation on lower saturated pixels more than on high saturated pixels.
*   channel mixer: This module is a powerful tool to manage channels. As entry, it manipulates red, green and blue channels. As output, it uses red, green, blue or grey or hue, saturation, lightness.
*   color contrast
*   color correction: This module can be used to modify the global saturation or to give a tint. Read [Johannes' blog post](/2012/03/color-correction "color correction").
*   monochrome: This module is a quick way to convert an image to black and white. You can simulate a color filter in order to modify your conversion. The filter can be changed in size and color center.
*   color zones: This module allows to selectively modify the colors in your image. It is highly versatile and allows every transformation possible in the LCh colorspace.
*   color balance: Use lift/gamma/gain to change highlights, midtones and shadows.
*   vibrance: For a detailed description read [Henrik's blog post](/2011/10/different-kind-of-saturation "different kind of saturation").
*   color look up table: Apply styles or film emulations. You can also easily edit the changes done. For more information you can [read this blog post](/2016/05/colour-manipulation-with-the-colour-checker-lut-module)
*   input/output/display color profile management
*   A useful feature that displays pixels outside the dynamic range.

## Correction modules:

*   dithering: This helps with banding in smooth gradients in the final image.
*   sharpen: This is a standard UnSharp Mask tool for sharpening the details of an image.
*   equalizer: This versatile module can be used to achieve a variety of effects, such as bloom, denoising, and local contrast enhancement. It works in the wavelet domain, and parameters can be tuned for each frequency band separately.
*   denoise (non-local means): Denoising with separated color / brightness smoothing.
*   defringe: Remove color fringes on high contrast edges.
*   haze removal: This module allows to remove the low contrast and color tint coming from haze and air pollution.
*   denoise (bilateral filter): Another denoising module.
*   liquify: Push image parts around, grow them, shrink them. More information can be found in [this blog post](/2016/04//liquify-liquify "liquify")
*   perspective correction: A great module to automatically un-distort shots with straight lines. See [our blog post](/2016/03/a-new-module-for-automatic-perspective-correction "Perspective correction") for an introduction and examples.
*   lens correction: lens defect correction using [lensfun](https://github.com/lensfun/lensfun "liblensfun").
*   spot removal: Spot removal allows you to correct a zone in your image by using another zone as model.
*   profiled denoise: By measuring the typical noise of cameras at the different ISO levels darktable is able to remove a lot of it. Read [this blog post](/2012/12/profiling-sensor-and-photon-noise "profiling sensor and photon noise") for more information.
*   raw denoise: Raw denoise allows you to perfom denoising on pre-demosaic data. It is ported from [dcraw](https://www.cybercom.net/~dcoffin/dcraw/ "dcraw").
*   hot pixels: This module allows you to visualize and correct stuck and hot pixels.
*   chromatic aberrations: This module automatically detects and corrects chromatic aberrations.

## Effects/artistic image postprocessing:


*   watermark: The watermark module provides a way to render a vector-based overlay onto your image. Watermarks are standard SVG documents and can be designed using Inkscape. The SVG processor of darktable also substitutes strings within the SVG document which gives the opportunity to include image-dependent information in the watermark such as aperture, exposure time and other metadata.
*   framing: This module allows you to add an artistic frame around an image.
*   split toning: Original split toning method creates a two color linear toning effect where the shadows and highlights are represented by two different colors. darktable split toning module is more complex and offers more parameters to tweak the result.
*   vignetting: This module is an artistic feature which creates vignetting (modification of the brightness/saturation at the borders).
*   soften: This module is an artistic feature that creates the Orton effect also commonly known as softening the image. Michael Orton achieved such result on slide film by using 2 exposures of the same scene: one well exposed and one overexposed; then he used a technique to blend those into a final image where the overexposed image was blurred.
*   grain: This module is an artistic feature which simulates the grain of a film.
*   highpass: This module acts as highpass filter.
*   lowpass: This module acts as lowpass filter. One use case is described in [Ulrich's blog post](/2012/02/using-lowpass-filter-to-recover-shadows "Using lowpass filter to recover shadows").
*   lowlight vision: Low light module allows to simulate human lowlight vision, thus providing the ability to make lowlight pictures look closer to reality. It can also be used to perform a day to night conversion.
*   bloom: This module boost highlights and softly blooms them over the image.
*   color mapping: Transfer colors from one image to another.
*   colorize
*   graduated density: This module aims at simulating a neutral density filter, in order to correct exposure and color in a progressive manner.
