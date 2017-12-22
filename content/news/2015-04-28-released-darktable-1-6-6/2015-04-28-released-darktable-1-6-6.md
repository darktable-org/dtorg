author: houz
comments: true
date: 2015-04-28 11:35:02+00:00
layout: post
link: http://www.darktable.org/2015/04/released-darktable-1-6-6/
slug: released-darktable-1-6-6
title: released darktable 1.6.6
lede: wheat_wide.jpg
lede_author: <a href="https://houz.org/">houz</a>
wordpress_id: 3659
tags: announcement, darktable release

We are happy to announce that darktable 1.6.6 has been released. Please note that the 1.6.5 release was broken so 1.6.6 was directly pushed out. Just pretend 1.6.5 had been skipped.

The release notes and relevant downloads can be found attached to this git tag:
[https://github.com/darktable-org/darktable/releases/tag/release-1.6.6](https://github.com/darktable-org/darktable/releases/tag/release-1.6.6)
Please only use our provided packages ("darktable-1.6.6.*" tar.xz and dmg) not the auto-created tarballs from github ("Source code", zip and tar.gz). The latter are just git snapshots and will not work! Here are the direct links to tar.xz and dmg:
[https://github.com/darktable-org/darktable/releases/download/release-1.6.6/darktable-1.6.6.tar.xz](https://github.com/darktable-org/darktable/releases/download/release-1.6.6/darktable-1.6.6.tar.xz)
[https://github.com/darktable-org/darktable/releases/download/release-1.6.6/darktable-1.6.6.dmg](https://github.com/darktable-org/darktable/releases/download/release-1.6.6/darktable-1.6.6.dmg)

this is another point release in the stable 1.6.x series.

    sha256sum darktable-1.6.6.tar.xz
    f85e4b8219677eba34f5a41e1a0784cc6ec06576326a99f04e460a4f41fd21a5
    sha256sum darktable-1.6.6.dmg
    bce9a792ee362c47769839ec3e49973c07663dbdf6533ef5a987c93301358607

## Improvements

* fix the Olympus E330 support (which was accidentally broken in 1.6.4)
* fix white balance reading for the Canon Powershot SX50 HS
* white balance presets for RICOH GR
* minor assorted bug fixes (masks, lens correction, profiled denoise, etc)

