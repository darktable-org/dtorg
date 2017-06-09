author: jo
comments: true
date: 2012-11-25 20:17:08+00:00
layout: post
link: http://www.darktable.org/2012/11/released-darktable-1-1/
slug: released-darktable-1-1
title: released darktable 1.1
wordpress_id: 2378
tags: announcement

[https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.tar.gz/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-1.1.tar.gz/download)

this is a feature release, so there is a lot of new stuff:


# general





	
  * new camera support, new whitebalance presets, etc., including
canon eos m support and samsung nx fix

	
  * similarity matching search for images that look alike.

	
  * geotagging, complete with map view (thanks to dinamic for starting that ages ago and to houz for actually bringing it home):
[http://www.darktable.org/2012/09/geotagging-in-darktable/](http://www.darktable.org/2012/09/geotagging-in-darktable/)

	
  * mac os package: [http://www.darktable.org/2012/08/bringing-current-darktable-to-os-x/](http://www.darktable.org/2012/08/bringing-current-darktable-to-os-x/)

	
  * a lot of bugfixes (mainly thanks to ulrich for his meticulous work)

	
  * facebook exporter (for those who have an account there)




# ui





	
  * reworked the much hated `more plugins' widget (thanks to boucman)

	
  * image grouping: [http://www.darktable.org/2012/09/grouping/](http://www.darktable.org/2012/09/grouping/)

	
  * command line interface! [http://www.darktable.org/2012/07/exporting-images-on-the-command-line/](http://www.darktable.org/2012/07/exporting-images-on-the-command-line/)

	
  * tone and base curves got a new user interface to better support fine grained workflow as in: [http://www.darktable.org/2012/02/mastering-color-with-lab-tone-curves/](http://www.darktable.org/2012/02/mastering-color-with-lab-tone-curves/)

	
  * visually low-profile controls with finetuning: [http://www.darktable.org/2012/03/bauhaus-widgets/](http://www.darktable.org/2012/03/bauhaus-widgets/)

	
  * color correction module ([http://www.darktable.org/2012/03/color-correction](http://www.darktable.org/2012/03/color-correction/)/) got a GUI update since the blog post (two circles indicating shadows and highlights instead of the quad).

	
  * live view for tethered shooting! [http://www.darktable.org/2012/05/live-view/](http://www.darktable.org/2012/05/live-view/)




# darkroom





	
  * extensive use of edge-aware filtering techniques to suppress noise, halos and ringing all around darktable: [http://www.darktable.org/2012/09/edge-aware-image-development/](http://www.darktable.org/2012/09/edge-aware-image-development/)

	
  * conditional blending, and a lot of goodies around it! [http://www.darktable.org/2012/07/some-enhancements-to-conditional-blending/](http://www.darktable.org/2012/07/some-enhancements-to-conditional-blending/)

	
  * magenta highlights: [http://www.darktable.org/2012/07/magenta-highlights/](http://www.darktable.org/2012/07/magenta-highlights/)improved on high-contrast edges to overexposed areas (should get rid of purple highlights on tiny water waves and purple fringes around tree leaves for example)

	
  * much improved sharpness for both export and darkroom view, especially for downsampled images and if you use lens corrections or rotations/perspective corrections. check the new options in the preferences dialog, also one more than mentioned in the blog ("demosaicing for zoomed out darkroom mode" to trade performance for even more sharpness): [http://www.darktable.org/2012/06/upcoming-features-new-interpolation-modes-and-better-resize/](http://www.darktable.org/2012/06/upcoming-features-new-interpolation-modes-and-better-resize/)




# color management





	
  * improved per-screen color management (should reload the screen profile automatically)

	
  * more compatible embedded color profiles (should fix problems on windows viewing our images, if that matters)

	
  * read embedded color profiles from jpg




# opencl





	
  * most of our modules now can take advantage of your computer's gpu power

	
  * caching for compiled opencl kernels (even in case the driver doesn't do it) for faster startup times




# usermanual








	
  * find a pdf snapshot here: [https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-usermanual.pdf/download](https://sourceforge.net/projects/darktable/files/darktable/1.1/darktable-usermanual.pdf/download)

	
  * is reasonably up to date again

	
  * not translated so far







# translations





	
  * two new translations (both portuguese.. ;) )

	
  * well translated: cs de es fr it ja nl pl pt_BR pt_PT sv

	
  * half translated: ca fi gl ro ru sq th zh_CN


enjoy!
