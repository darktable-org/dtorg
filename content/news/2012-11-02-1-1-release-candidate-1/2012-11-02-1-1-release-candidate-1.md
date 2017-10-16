author: jo
comments: true
date: 2012-11-02 02:04:00+00:00
layout: post
link: http://www.darktable.org/2012/11/1-1-release-candidate-1/
slug: 1-1-release-candidate-1
title: 1.1 release candidate 1
wordpress_lede: cloud.jpg
wordpress_id: 2328
tags: announcement

as commits are easing down a little lately it seems appropriate to push out the first release candidate of the new version:

[https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1~rc1.tar.gz/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1~rc1.tar.gz/download)

[update: mac package is available from [https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1~rc1.dmg/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1~rc1.dmg/download) ]

That doesn't mean this tarball is final or perfect by any means. we'll probably go on releasing a couple of these on our way to the final release in a few weeks. This will be a feature release, as opposed to the bug fixing point release series 1.0.x, so we've got a huge bunch of changes for you this time. The changelog is not the final one either, but here it is:

* new camera support, new whitebalance presets, etc.
* similarity matching search for images that look alike.
* geotagging, complete with map view (thanks to dinamic for starting that ages ago and to houz for actually bringing it home): "[{article.title}/blog/2012-09-23-geotagging-in-darktable/2012-09-23-geotagging-in-darktable.md]({filename}/blog/2012-09-23-geotagging-in-darktable/2012-09-23-geotagging-in-darktable.md)"
* image grouping: "[{article.title}/blog/2012-09-23-grouping/2012-09-23-grouping.md]({filename}/blog/2012-09-23-grouping/2012-09-23-grouping.md)"
* extensive use of edge-aware filtering techniques to suppress noise, halos and ringing all around darktable: "[{article.title}/blog/2012-09-02-edge-aware-image-development/2012-09-02-edge-aware-image-development.md]({filename}/blog/2012-09-02-edge-aware-image-development/2012-09-02-edge-aware-image-development.md)"
* mac os package: "[{article.title}/blog/2012-08-14-bringing-current-darktable-to-os-x/2012-08-14-bringing-current-darktable-to-os-x.md]({filename}/blog/2012-08-14-bringing-current-darktable-to-os-x/2012-08-14-bringing-current-darktable-to-os-x.md)"
* conditional blending, and a lot of goodies around it! "[{article.title}/blog/2012-07-11-some-enhancements-to-conditional-blending/2012-07-11-some-enhancements-to-conditional-blending.md]({filename}/blog/2012-07-11-some-enhancements-to-conditional-blending/2012-07-11-some-enhancements-to-conditional-blending.md)"
* magenta highlights: "[{article.title}/blog/2012-07-05-magenta-highlights/2012-07-05-magenta-highlights.md]({filename}/blog/2012-07-05-magenta-highlights/2012-07-05-magenta-highlights.md)" improved on high-contrast edges to overexposed areas (should get rid of purple highlights on tiny water waves and purple fringes around tree leaves for example)
* command line interface! "[{article.title}/blog/2012-07-05-exporting-images-on-the-command-line/2012-07-05-exporting-images-on-the-command-line.md]({filename}/blog/2012-07-05-exporting-images-on-the-command-line/2012-07-05-exporting-images-on-the-command-line.md)"
* much improved sharpness for both export and darkroom view, especially for downsampled images and if you use lens corrections or rotations/perspective corrections. check the new options in the preferences dialog, also one more than mentioned in the blog ("demosaicing for zoomed out darkroom mode" to trade performance for even more sharpness): "[{article.title}/blog/2012-06-02-upcoming-features-new-interpolation-modes-and-better-resize/2012-06-02-upcoming-features-new-interpolation-modes-and-better-resize.md]({filename}/blog/2012-06-02-upcoming-features-new-interpolation-modes-and-better-resize/2012-06-02-upcoming-features-new-interpolation-modes-and-better-resize.md)"
* live view for tethered shooting! "[{article.title}/blog/2012-05-30-live-view/2012-05-30-live-view.md]({filename}/blog/2012-05-30-live-view/2012-05-30-live-view.md)"
* tone and base curves got a new user interface to better support fine grained workflow as in: "[{article.title}/blog/2012-02-12-mastering-color-with-lab-tone-curves/2012-02-12-mastering-color-with-lab-tone-curves.md]({filename}/blog/2012-02-12-mastering-color-with-lab-tone-curves/2012-02-12-mastering-color-with-lab-tone-curves.md)"
* visually low-profile controls with finetuning: "[{article.title}/blog/2012-03-02-bauhaus-widgets/2012-03-02-bauhaus-widgets.md]({filename}/blog/2012-03-02-bauhaus-widgets/2012-03-02-bauhaus-widgets.md)"
* color correction module ("[{article.title}/blog/2012-03-11-color-correction/2012-03-11-color-correction.md]({filename}/blog/2012-03-11-color-correction/2012-03-11-color-correction.md)") got a GUI update since the blog post (two circles indicating shadows and highlights instead of the quad).
* Facebook exporter (for those who have an account there)

## color management:

* improved per-screen color management (should reload the screen profile automatically)
* more compatible embedded color profiles (should fix problems on windows viewing our images, if that matters)
* read embedded color profiles from jpg

## OpenCL

most of our modules now can take advantage of your computer's gpu power. caching for compiled opencl kernels (even in case the driver doesn't do it) for faster startup times.

Furthermore there are tons of updates to the usermanual and many updated translations:

* french: perfect! thanks to Olivier Tribout!
* italian: all done, thanks to Eugenio!
* japanese: great, thanks a3novy!
* nl: Ger Siemerink got it all covered :)
* sv: Henrik and Richard Levitte (all done in git)
* es: thanks to tatica! (git is good)

* de: 1400 translated messages, 64 fuzzy translations, 45 untranslated messages.

and those lag behind a little more. any takers?

* ca: 261 translated messages, 371 fuzzy translations, 877 untranslated messages.
* cs: 1107 translated messages, 224 fuzzy translations, 178 untranslated messages.
* fi: 639 translated messages, 478 fuzzy translations, 392 untranslated messages.
* gl: 418 translated messages, 531 fuzzy translations, 560 untranslated messages.
* pl: 1122 translated messages, 210 fuzzy translations, 177 untranslated messages.
* ro: 747 translated messages, 417 fuzzy translations, 345 untranslated messages.
* ru: 1118 translated messages, 215 fuzzy translations, 176 untranslated messages.
* sq: 1104 translated messages, 219 fuzzy translations, 186 untranslated messages.
* th: 180 translated messages, 176 fuzzy translations, 1153 untranslated messages.
* zh_CN: 1116 translated messages, 205 fuzzy translations, 188 untranslated messages.

enjoy!
