author: pmjdebruijn
comments: true
date: 2012-10-23 20:12:25+00:00
layout: post
link: http://www.darktable.org/2012/10/whats-involved-with-adding-support-for-new-cameras/
slug: whats-involved-with-adding-support-for-new-cameras
title: What's involved with adding support for new cameras
wordpress_lede: camera.jpg
wordpress_id: 2300
tags: blog

_Update: This post is a few years old by now, and while most things are still valid there is at least one change: darktable doesn't use dcraw/libraw and more._

Say you're running darktable, you've just bought a brand spanking new camera and it's not supported yet by darktable. Here is a list of things that need to be done (typically we'd recommend to check this _before_ actually buying anything, often you'll be able to find sample raw files online):

## Raw format support

darktable uses two libraries to read raw files. Most common raw formats are read via the RawSpeed library (by Klaus Post), more esoteric raw formats not supported by RawSpeed are read via LibRaw (which in turn is based on Dave Coffin's dcraw). While most vendors have only a single raw format there are camera to camera variations.

So if darktable isn't recognizing your raw files at all (or they show up as corrupted images), it is always a good idea to check if darktable's development version (git master) does read them (before running darktable git master, please do backup your database and images).

If it still doesn't work, it's a good idea to check if the latest dcraw (the version that comes with the distros tends to lag behind) can handle the files:

Install the build dependancies liblcms-dev(el) libjpeg-dev(el) and libjasper-dev(el) (or whatever your distro calls them)

    # wget https://www.cybercom.net/~dcoffin/dcraw/dcraw.c
    # gcc -o dcraw -O4 dcraw.c -lm -ljasper -ljpeg -llcms
    # ./dcraw -v -w -o 1 -f -T IMG_0000.RAW

If it doesn't work you may want to supply Dave Coffin with sample raw files.
Also, please mail the raw samples to our devel mailing list so we can take a look.

## Sensor support

darktable currently only supports regular Bayer style sensors (which probably accounts for 99% of available cameras). This means darktable will not be able to handle Sigma FOVEON based cameras. A lot of Fuji cameras have weird variations of the standard Bayer scheme which make them incompatible with darktable, too. We currently have no plans to support these cameras either.

## Black and White levels

Take a sample raw. Convert it to DNG via Adobe DNG Converter (make sure you have the latest version, assuming Adobe updated the converter for your particular camera model).
The Blacklevel usually corrects for a green or purplish color cast:

    exiv2 -pt MY.DNG | grep BlackLevel
    Exif.SubImage1.BlackLevel Rational 4 37376/256 37376/256 37376/256 37376/256

This effectively means the blacklevel is 37376/256 = 146, expected values are usually well below 1000.
On the other hand the whitelevel influences highlight handling:

    exiv2 -pt MY.DNG | grep WhiteLevel
    Exif.SubImage1.WhiteLevel Short 1 3956

Expected values ranges commonly range from about 3000 to 17000.

## Panasonic Aspect Ratio's

Most modern cameras which output raw files, also allow the user to set non sensor native aspect ratio's. So even if the sensor has a real world aspect ratio of 4:3, you can have the camera automatically center crop your images to for example 3:2. This usually only affects JPEG output, leaving the output raw still at an uncropped full resolution at it's original aspect ratio 4:3.

Panasonic cameras are different however, they actually seem to crop the raw images themselves, which means every aspect ratio mode needs it's each set of parameters.

For most Panasonic cameras we have data for the 4:3 mode, but often not for the other modes. When we don't have data for the other modes darktable falls back to use LibRaw, which may or may not work properly.

If you own a Panasonic camera, please check the file below, if your camera has defined support for all four aspect ratio modes (4:3/3:2/16:9/1:1):

[https://github.com/darktable-org/rawspeed/blob/develop/data/cameras.xml](https://github.com/darktable-org/rawspeed/blob/develop/data/cameras.xml)

If they are defined please do test them, and if they are either undefined or you're getting weird behavior (like pixel artifacts in the right hand image border) we'd very much be interested in a set of RW2 samples.

## Basecurve

By default raw files are more or less linear, meaning they look fairly dark/murky by default. So one needs to apply a curve to make it look decent. For darktable we try to get a ballpark match with the camera's JPEG output with regard to tonality, to do this we use the so-called basecurve, which we manually derived from raw+JPG samples. Typically the basecurves seem to be vendor specific (but less so camera model specific). That said, in some cases there can still be some camera model specific differences, in which case you might want to take a look at [this post]({filename}/blog/2013-10-28-about-basecurves/2013-10-28-about-basecurves.md).

That said, dynamic image processing technologies like Nikon's Active D-light, Canon's Auto Lighting Optimizer, Samsung's Smart Range, Sony's Dynamic Range Optimizer, etc do throw a monkey wrench into raw converters ability to approximate camera output in any way. So when doing comparisons make sure you've turned the above off, and also don't forget to keep [this]({filename}/blog/2013-05-10-display-color-management-in-darktable/2013-05-10-display-color-management-in-darktable.md) in mind.

## Color Matrices

The plain red, green and blue values we get straight from the sensor are never a good representation of color. This is fixed by characterizing the sensor's behavior in a so called XYZ matrix (often referred to as a color matrix). There are two kinds in darktable (and you need at least one of those to get decent color rendition in darktable):

The standard color matrix is a color matrix we get from dcraw (which in turn gets most of them via Adobe's DNG Converter).

Take a sample raw

Convert it to DNG via Adobe DNG Converter (make sure you have the latest version, assuming Adobe updated the converter for your particular camera model)

    exiv2 -pt MY.DNG 2>/dev/null | grep CalibrationIlluminant2
    # Exif.Image.CalibrationIlluminant2 Short 1  21

Assuming the above is 21:

    # exiv2 -pt MY.DNG 2>/dev/null | grep ColorMatrix2
    Exif.Image.ColorMatrix2 SRational 9  7798/10000 -2562/10000 -740/10000 -3879/10000 11584/10000 2613/10000 -1055/10000 2248/10000 5434/10000

The enhanced color matrix which we calculate from user submitted color charts.

[https://encrypted.pcode.nl/blog/2010/06/28/darktable-camera-color-profiling/](https://encrypted.pcode.nl/blog/2010/06/28/darktable-camera-color-profiling/)

Neither of the above color matrices have the goal of emulating the camera's JPEG color rendition. So even though the basecurve will in most cases give you similar tonality, the colors are unlikely to match.

## White balance presets

darktable gets a library of white balance presets from the UFRaw project. This means you can select camera white balance presets in darktable's user interface. Having white balance presets for your camera is a convenience, it's not critical. But if they are missing, you can contribute them:

Upgrade the camera firmware (use a full, known reliable battery), be aware that it can brick your camera if done improperly. (having the latest firmware is preferable, but not critical, if you are uncomfortable with the risks involved in upgrading your camera you should not attempt it)

Shoot a single raw file for each of the camera's white balance presets (make sure you don't have any white balance finetuning enabled) (image content doesn't matter) (these are usually 5-10 shots). Make sure you have a recent version of ExifTool installed (if not, you need to edit wb_extract.pl and point it to your updated copy).

Download [http://ufraw.cvs.sourceforge.net/viewvc/ufraw/ufraw/wb_extract.pl](http://ufraw.cvs.sourceforge.net/viewvc/ufraw/ufraw/wb_extract.pl)

    perl wb_extract.pl  2>/dev/null

(If you are adept at Perl, you could help us/UFRaw by revising the above script)

Some cameras optionally offer the ability to tune their white balance presets. You can include these as well (but the numbers of shots increase rapidly, as there are typically 5-10 base presets, offering as much as 19 steps of finetuning per preset). For the time being you need to shoot either all or none of the finetuning steps as darktable hasn't implemented finetuning interpolation yet. If you do, use only the blue-amber axis, leave the green-purple axis centered (0).

When contributing your white balance presets please do include your camera's firmware version (for future reference).

## EXIF support & Lens Recognition

darktable uses the Exiv2 library to read EXIF data from image files. As with all raw formats, while there is common ground, there can be camera to camera differences.

You can check what Exiv2 can (or can't) read from your raw file using the exiv2 command line utility:

    # exiv2 -pt IMG_0000.RAW

A common problem is lenses not being recognized. Most raw files store the lens identifiers as a number, which Exiv2 translates into a lens name via a lookup table. Vendors don't advertise these numbers, so this lookup table is put together from community submissions. Another problem that arises is that the main camera vendors don't account for third party lenses. So a Canon and a Sigma lens can end up reported as the same number in which case it's hard to tell for Exiv2 which is which. I think a heuristic is used where focal lengths are compared to see which matches best (assuming both variants are known).

If you have any issues with EXIF you can report these to the Exiv2 project, don't forget to include sample files. Also when reporting issues with lens detection, **always** include the **full** lens name in the bug report, so "Canon 18-55" isn't useful (as there are 4 (or whatever) variants of that lens). Even if there aren't variants, still include the full/proper lens name.

While darktable doesn't use ExifTool for anything, it's still a good idea to check if ExifTool handles your files well, too, and if not report this to the ExifTool project.

Many distros ship older versions of Exiv2/Exiftool. Be very careful when updating your system copies of these libraries as you may inadvertently break other applications and/or create problems with future operating system upgrades.

## Lens correction

Assuming Exiv2 translated the LensID in EXIF in to a proper lens name. The Lensfun project may or may not have correction information for your lens. For the lenses that do have correction information this is typically limited to distortion correction. If there isn't any correction information for your lens yet, you can calibrate it yourself (don't forget to submit the results to the Lensfun project, assuming they work well, please do verify this before submitting):

These articles might be helpful:

* darktable blog: "[have your lens calibrated!]({filename}/blog/2013-07-30-have-your-lens-calibrated/2013-07-30-have-your-lens-calibrated.md)"
* [http://libregraphicsworld.org/blog/entry/creating-lens-distorsion-models-with-hugin-lens-calibrator](http://libregraphicsworld.org/blog/entry/creating-lens-distorsion-models-with-hugin-lens-calibrator)
* [http://lensfun.sourceforge.net/calibration/](http://lensfun.sourceforge.net/calibration/)
* [http://wilson.bronger.org/lens_calibration_tutorial/](http://wilson.bronger.org/lens_calibration_tutorial/)

## Final notes

If the above doesn't help you in assessing your problem and you need to contact us, please do keep the following in mind:

Where appropriate include raw samples so developers can check your problem (please use English language file sharing services)

For some issues it's useful to upload screenshots, however please make screenshots of darktable using an English GUI:

    # LANG=C darktable
