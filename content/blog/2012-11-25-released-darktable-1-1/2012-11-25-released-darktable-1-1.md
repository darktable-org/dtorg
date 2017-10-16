author: jo
comments: true
date: 2012-11-25 20:17:08+00:00
layout: post
link: http://www.darktable.org/2012/11/released-darktable-1-1/
slug: released-darktable-1-1
title: released darktable 1.1
wordpress_lede: panda.jpg
wordpress_id: 2378
tags: announcement

[https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.tar.gz/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.tar.gz/download)

this is a feature release, so there is a lot of new stuff:

# general

* new camera support, new whitebalance presets, etc., including canon eos m support and samsung nx fix
* similarity matching search for images that look alike.
* geotagging, complete with map view (thanks to dinamic for starting that ages ago and to houz for actually bringing it home): "[{article.title}/blog/2012-09-23-geotagging-in-darktable/2012-09-23-geotagging-in-darktable.md]({filename}/blog/2012-09-23-geotagging-in-darktable/2012-09-23-geotagging-in-darktable.md)"
* mac os package: "[{article.title}/blog/2012-08-14-bringing-current-darktable-to-os-x/2012-08-14-bringing-current-darktable-to-os-x.md]({filename}/blog/2012-08-14-bringing-current-darktable-to-os-x/2012-08-14-bringing-current-darktable-to-os-x.md)"
* a lot of bugfixes (mainly thanks to ulrich for his meticulous work)
* facebook exporter (for those who have an account there)

# ui

* reworked the much hated `more plugins' widget (thanks to boucman)
* image grouping: "[{article.title}/blog/2012-09-23-grouping/2012-09-23-grouping.md]({filename}/blog/2012-09-23-grouping/2012-09-23-grouping.md)"
* command line interface! "[{article.title}/blog/2012-07-05-exporting-images-on-the-command-line/2012-07-05-exporting-images-on-the-command-line.md]({filename}/blog/2012-07-05-exporting-images-on-the-command-line/2012-07-05-exporting-images-on-the-command-line.md)"
* tone and base curves got a new user interface to better support fine grained workflow as in: "[{article.title}/blog/2012-02-12-mastering-color-with-lab-tone-curves/2012-02-12-mastering-color-with-lab-tone-curves.md]({filename}/blog/2012-02-12-mastering-color-with-lab-tone-curves/2012-02-12-mastering-color-with-lab-tone-curves.md)"
* visually low-profile controls with finetuning: "[{article.title}/blog/2012-03-02-bauhaus-widgets/2012-03-02-bauhaus-widgets.md]({filename}/blog/2012-03-02-bauhaus-widgets/2012-03-02-bauhaus-widgets.md)"
* color correction module ("[{article.title}/blog/2012-03-11-color-correction/2012-03-11-color-correction.md]({filename}/blog/2012-03-11-color-correction/2012-03-11-color-correction.md)") got a GUI update since the blog post (two circles indicating shadows and highlights instead of the quad).
* live view for tethered shooting! "[{article.title}/blog/2012-05-30-live-view/2012-05-30-live-view.md]({filename}/blog/2012-05-30-live-view/2012-05-30-live-view.md)"

# darkroom

* extensive use of edge-aware filtering techniques to suppress noise, halos and ringing all around darktable: "[{article.title}/blog/2012-09-02-edge-aware-image-development/2012-09-02-edge-aware-image-development.md]({filename}/blog/2012-09-02-edge-aware-image-development/2012-09-02-edge-aware-image-development.md)"
* conditional blending, and a lot of goodies around it! "[{article.title}/blog/2012-07-11-some-enhancements-to-conditional-blending/2012-07-11-some-enhancements-to-conditional-blending.md]({filename}/blog/2012-07-11-some-enhancements-to-conditional-blending/2012-07-11-some-enhancements-to-conditional-blending.md)"
* magenta highlights: "[{article.title}/blog/2012-07-05-magenta-highlights/2012-07-05-magenta-highlights.md]({filename}/blog/2012-07-05-magenta-highlights/2012-07-05-magenta-highlights.md)" improved on high-contrast edges to overexposed areas (should get rid of purple highlights on tiny water waves and purple fringes around tree leaves for example)
* much improved sharpness for both export and darkroom view, especially for downsampled images and if you use lens corrections or rotations/perspective corrections. check the new options in the preferences dialog, also one more than mentioned in the blog ("demosaicing for zoomed out darkroom mode" to trade performance for even more sharpness): "[{article.title}/blog/2012-06-02-upcoming-features-new-interpolation-modes-and-better-resize/2012-06-02-upcoming-features-new-interpolation-modes-and-better-resize.md]({filename}/blog/2012-06-02-upcoming-features-new-interpolation-modes-and-better-resize/2012-06-02-upcoming-features-new-interpolation-modes-and-better-resize.md)"

# color management

* improved per-screen color management (should reload the screen profile automatically)
* more compatible embedded color profiles (should fix problems on windows viewing our images, if that matters)
* read embedded color profiles from jpg

# opencl

* most of our modules now can take advantage of your computer's gpu power
* caching for compiled opencl kernels (even in case the driver doesn't do it) for faster startup times

# usermanual

* find a pdf snapshot here: [https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-usermanual.pdf/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-usermanual.pdf/download)
* is reasonably up to date again
* not translated so far

# translations

* two new translations (both portuguese ... ;) )
* well translated: cs de es fr it ja nl pl pt_BR pt_PT sv
* half translated: ca fi gl ro ru sq th zh_CN

enjoy!
