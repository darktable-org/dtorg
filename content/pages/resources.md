Title: Resources
Date: 2017-05-23T15:32:24-06:00

Resources page.

This is testing formatting for fenced code blocks:

Required packages:

```
libsqlite3, libjpeg, libpng, libpugixml, rawspeed (supplied), gtk+-3, cairo, lcms2, exiv2, tiff, curl, gphoto2, dbus-glib, fop, openexr, libsoup2.4
```

Another test:

```bash
$ sudo apt-get install debhelper dpkg-dev fakeroot
$ sudo apt-get build-dep darktable
$ tar zxvf darktable_$VERSION.orig.tar.gz
$ cd darktable-$VERSION
$ tar zxvf ../darktable_$VERSION.debian.tar.gz
$ dpkg-buildpackage -rfakeroot
```
