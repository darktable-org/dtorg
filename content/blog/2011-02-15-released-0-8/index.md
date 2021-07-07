---
author: dt
comments: true
date: 2011-02-15 22:07:53+00:00
layout: post
link: /2011/02/released-0-8/
slug: released-0-8
title: "released 0.8"
wordpress_lede: donau.jpg
wordpress_id: 225
tags:
  - announcement
  - darktable release
---
we released version 0.8, which obsoletes 0.7.1 in a lot of ways:

* _much_ faster image loading due to _rawspeed_, an awesome new library by klaus post @rawstudio
* lots of performance improvements in our caches and pixel pipelines (together with the above like 5x--10x)
* gpu computing using opencl (for graphics boards that support it) for a lot of common modules, to give a huge performance boost
* overhauled collection module for more flexible image collections
* metadata editor (set author and copyright information etc)
* fast demosaicing now done on roi and in floating point
* HDR bracketing and tone mapping (somewhat experimental)
* flickr upload
* new languages: thai and japanese
* lots of new color matrices and white balance presets
* lots of bugfixes

according to the git log, this release introduces over 900 new commits brought to you by (in order of commits): johannes hanika, Tobias Ellinghaus, Henrik Andersson, Pascal de Bruijn, Ger Siemerink, Bruce Guenter, Jose Carlos Garcia Sogo, Boucman, Alexandre Prokoudine, Simon Spannagel, Olivier, Jochen, Karl Mikaelsson, Jochen Schroeder, Brian Teague, Pascal Obry, calca, Ville Pätsi, Uli Scholler, Thierry Leconte, Pacsal de Bruijn, and Alex Chateau.
special thanks to Pacsal ;) and to Robert Park for an awesome amount of color matrices created with his help, also for Klaus Staedtler for the new icons.
