author: Henrik Andersson
comments: true
date: 2011-03-28 22:08:40+00:00
layout: post
link: http://www.darktable.org/2011/03/darktable-user-manual-revisited/
slug: darktable-user-manual-revisited
title: darktable user manual revisited
wordpress_id: 457
tags: development

![usermanual]({attach}usermanual.jpg)

Up till recently the usermanual has been only available for those who got the source and the necessary tools to generate and even than it would generate a HUGE pdf file due to the amount of high resolution of screenshots. I revisited the build system with the goals of shrink-en the size of the final PDF and to produce an html output that could be integrated in our website.

First off I added the media transformation parts which gathered all images, resize and compress them using jpeg before embedding them into the final media output, this resulted in a size change of final PDF to a more reasonable size 5Mb for the full draft document which earlier was  25Mb. This change introduced some additional passes in buildsystem but it also cleaned up some of the dependency problems that existed ...

Second part I added a target for html output and trimmed a style-sheet to produced a chunked html output of the user manual which in the end should in-cooperate nicely with the current website and it’s styles. This journey introduced a lot of regex/javascript/dynamic html hacking and I think at last I got all in place.

So I’ll announce hereby that [http://darktable.sourceforge.net/](http://darktable.sourceforge.net/) does now have the draft user manual browsable online.
