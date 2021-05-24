---
author: pmjdebruijn
comments: true
date: 2013-05-10 17:47:54+00:00
layout: post
link: /2013/05/display-color-management-in-darktable/
slug: display-color-management-in-darktable
title: "Display color management in darktable"
lede: lego_doctor.jpg
wordpress_id: 2908
tags:
  - blog
---
## The general picture on the modern Linux desktop

Modern Linux distros featuring either GNOME, Unity or KDE offer fairly easy configuration of color management, this system level configuration mostly pertains to the handling of an ICC display profile.

If you have set a display profile via your system configuration tool (The Color applet in System Settings for GNOME or Unity), there are a few things to keep in mind.

An ICC display profile consists of two main parts. First the so-called "vcgt", which corrects for whitepoint (this is most noticeable on laptops which shift from being very blueish to a bit more yellowish) and gamma. The "vcgt" is loaded into X11 and applied to your whole screen, so all applications automatically benefit. On a GNOME or Unity desktop this is done by GNOME Settings Daemon during login.

The second is the rest of the ICC profile, and this has to be processed in color management enabled application (typically via liblcms2). So we need a mechanism to pass the actual ICC profile to our applications without having to configure them all individually.

The oldest mechanism is the _ICC_PROFILE atom, which allows a single display profile to be defined for your system (this obviously fails for dual head configurations). You can check if a profile is setup like so:

    $ xprop -display :0.0 -len 14 -root _ICC_PROFILE

On a GNOME or Unity system the _ICC_PROFILE is setup by GNOME Setting Daemon during login.

On some systems there may be a _ICC_PROFILE_1 and _ICC_PROFILE_2 atom to facilitate dual head configurations. While darktable should pick up on those, I'm not sure how well other applications support this mechanism.

The another relatively new mechanism is colord by Richard Hughes, which is an infrastructure daemon, which by it self does very little, as it's mostly just an information/configuration store. But modern GNOME, Unity or KDE desktops store their display profile setups in colord, so applications can query colord which profile to apply depending on which screen they are displayed on (in case of a dual head configuration). Currently few applications are colord aware however. darktable is one of those few.

If you haven't setup a display profile yourself that doesn't per-se mean there is no display profile active. Modern desktops actually query the display (via EDID) itself about its advertised color coverage, from which an automatic display profile is generated. An easy way to check if such an automatic profile was generated:

    # ls -l ~/.local/share/icc/edid-*.icc

For more in-depth information the following articles are highly recommended:

* [https://encrypted.pcode.nl/blog/2013/04/14/display-profiles-generated-from-edid/](https://encrypted.pcode.nl/blog/2013/04/14/display-profiles-generated-from-edid/)
* [https://encrypted.pcode.nl/blog/2012/01/29/color-management-on-linux/](https://encrypted.pcode.nl/blog/2012/01/29/color-management-on-linux/)

## darktable's current (1.0/1.1/1.2) implementation

First off I want to make something very clear, darktable's darkroom mode is fully color managed and should always be used in situations where you are evaluating color. Since darktable is colord enabled (and if colord is properly setup) it should even render correct color in dual head configurations.

In darktable's lighttable mode there are however a few things you need to be aware of. When importing new raw photos into darktable, it will display the raws embedded thumbnail (which has been fully processed by the camera software) and the display profile is currently NOT being applied to these embedded thumbnails. Keep in mind, that these thumbnails have been processed by the proprietary firmware of the camera, so even if we applied the display profile it would still not match the processing that is done by darktable by default. It is however possible to disable the use of these embedded thumbnails altogether in darktable's preferences, forcing all raws to be processed by darktable's own imaging pipeline. This will slow down thumbnail generation by a few orders of magnitude, which is why this isn't our default behavior.

Once you've entered darkroom mode for a raw, the image has been processed in darktable's imaging pipeline including the application of the display profile, so this result is now kept as an accurate thumbnail for that particular raw.

If you've read that well, you might have noticed that we currently keep the display profile pre-applied in our thumbnail cache. Which is good for performance, and works just fine in most use-cases, but can result in ugly behavior for example when you change/replace your display, since darktable will still show thumbnails applied with the display profile of your previous display. In such a case you can forcibly remove the thumbnail cache like so:

    $ rm -Iv ~/.cache/darktable/mipmaps-*
