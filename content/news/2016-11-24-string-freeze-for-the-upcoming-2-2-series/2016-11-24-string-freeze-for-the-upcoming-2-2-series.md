author: houz
comments: true
date: 2016-11-24 11:31:33+00:00
layout: post
link: http://www.darktable.org/2016/11/string-freeze-for-the-upcoming-2-2-series/
slug: string-freeze-for-the-upcoming-2-2-series
title: String freeze for the upcoming 2.2 series
lede: castle3_wide.jpg
wordpress_id: 4616
tags: announcement

This is a call for all our translators, now is the time to bring your .po file in the master branch up to date. We will not ship any translation that is not relatively complete, the exact threshold is still to be determined.

As a quick reminder, these are the steps to update the translation if you are working from git. `language_code` is not the whole filename of the po file but just the first part of it. For example, when for Italian the language code is `it` while the filename is `it.po`. You also have to compile darktable before updating your .po file as some of the translated files are auto-generated.


    cd /path/to/your/darktable/checkout/
    git checkout master
    git pull
    ./build.sh
    cd po/
    intltool-update <language_code>
    <edit language_code.po>


If you don't have a build environment set up to compile darktable you can also use [this .pot file](/files/darktable_2.2.0.pot).
