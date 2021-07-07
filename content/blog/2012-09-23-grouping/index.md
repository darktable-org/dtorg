---
author: houz
comments: true
date: 2012-09-23 22:11:45+00:00
layout: post
link: /2012/09/grouping/
slug: grouping
title: "Grouping"
wordpress_lede: IMG_6375_export.jpg
wordpress_id: 2154
tags:
  - upcoming feature
---
People following the development of darktable might have heard that we added a grouping feature. Everyone who hasn't heard of that yet: We added a grouping feature.

Now that everybody knows about it I should try to explain what it actually is and how it works/how to use it. For the technical specification you can have a look at [the design specs](https://github.com/darktable-org/darktable/blob/master/doc/grouping.txt).

<figure markdown="span" role="group">
![Grouping turned off](grouping_off.jpg)
<figcaption>Grouping turned off</figcaption>
</figure>

The first change in the GUI that can be noticed is a little ‘G’ button. Well, first of all we have to notice that there are two kinds of ‘G’ in the GUI: one in the top toolbar, next to the preferences wheel. The other kind is on images frames which are part of a group, next to the yin-yang-edited symbol.

With the G in the toolbar you can change if images are shown in groups or not. This corresponds to the “‘G’ on” and “‘G’ off” sections in the grouping.txt file. The interesting case is when the toolbar G is turned on. Now you can expand grouped images by clicking on the G in the thumbnail frame and collapse the group again with another click. Once a group is expanded you can change the representative of the group by clicking its G. This will be the image that is shown when the group is collapsed.

<figure markdown="span" role="group">
![Grouping turned on](grouping_on.jpg)
<figcaption>Grouping turned on</figcaption>
</figure>

If you want to play with that you obviously need grouped images in the first place. You get them either by importing files with the same base name and just
different extensions (like “img_0001.CR2” and “img_0001.JPG”) or by duplicating an image. You can also just put images into a group manually by selecting them
and hitting ctrl-g. If you expanded a group before hitting these keys the selected images will be added to the expanded group, otherwise a new group is
created. Removing images from a group is done by selecting them and hitting ctrl-shift-g.

To select all images in an expanded group you can ctrl-click or shift-click the G of one image of the group.

<figure markdown="span" role="group">
![Grouping turned on and one group expanded](group_expanded.jpg)
<figcaption>Grouping turned on and one group expanded</figcaption>
</figure>

So at the end of the day it all boils down to keep your lighttable nice and tidy by only allowing you to only see a single thumbnail for a logical group of images. Please keep in mind however that changes done to the representative of a group (by opening it in darkroom mode and working on it) are only applied to that one image, not all images in the group!

I know that this explanation is a little hard to follow if you didn't play with the functionality in darktable yet. So just go and try it.
