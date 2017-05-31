author: parafin
comments: true
date: 2012-08-14 19:44:11+00:00
layout: post
link: http://www.darktable.org/2012/08/bringing-current-darktable-to-os-x/
slug: bringing-current-darktable-to-os-x
title: Bringing current darktable to OS X
wordpress_id: 1918
tags: blog, development, bugfixes, darktable, git, macports, os

Darktable has been software of my choice for raw photo development for quite some time now, I've occasionally submitted bug reports and patches and kept an eye on current development by using git master version. My main operating system is Linux, which is the priority target of darktable support, but recently I bought MacBook Air to take with me on trips and such. Also my current project at work consists of porting a library to OS X, so this presented to me as a great opportunity to contribute to one of my favorite open-source projects and make darktable work reliably on Macs. Some work has already been done in the past, there's even a package of an old darktable version for OS X, but of course I was interested in bringing the latest darktable experience to OS X.


# How things were at the beginning of my work


Since OS X support was present in some way in current codebase, compiling darktable wasn't a problem. All I had to do is install dependencies via macports, checkout git repository and run cmake and make. Darktable even successfully started, at least sometimes :) That was a good start actually.


# Killed bugs


First problem I noticed was reproducible crash when switching to darkroom mode. Using gdb I traced it back to text rendering in bauhaus code. On Linux fontconfig considers "sans", "sans serif" and "sans-serif" as aliases to default font from Sans family, but OS X isn't so accepting and chokes on "sans-serif" spelling, which was used in bauhaus. Changing it to "sans" solved this problem.

Second reproducible crash was triggered by attaching/detaching any USB devices. This time it wasn't anything darktable code did wrong, but libgphoto's fault. It was dynamically loading and unloading libusb-0.1, which left usb event handling threads running even after library with thread's main function code was unloaded from the memory. Workaround I used to circumvent this issue is to link darktable itself against libusb, thus making sure it stays in the memory. Hopefully gphoto will soon finally migrate to libusb-1 backend (it's already there, but needs more work and isn't a default choice yet) which has a proper exit function for stopping such threads before unloading.

Third crash was more tricky since it was happening almost randomly and in different functions. All of them though were in sqlite3 library. When I tried to build and install sqlite3 with debugging symbols to better understand what was happening, I realized that darktable was using system libsqlite3 instead of macports version. Forcing build system to link against libsqlite3 in /opt/local/lib directory helped (OS X dynamic linker/loader works differently than Linux one, it allows to prefer one library from /opt/local/lib and another from default system path). So OS X ships an old/buggy version of libsqlite3, something to watch out for if you're writing for Mac platform.

Next improvement was enabling OpenCL support on OS X. Apple began including it since Snow Leopard, so it would be a shame not to take advantage of that fact. OpenCL library is installed as a "framework" on OS X, this concept was new to me, and first I thought that there was no way to load it dynamically how it's done on Linux. I rewrote code so that darktable would link against OpenCL framework on OS X, but after some discussion and help on IRC, I've managed to find where exactly dynamic library resided - /System/Library/Frameworks/OpenCL.framework/Versions/Current/OpenCL. Now OpenCL library successfully loads, but I can't do any further testing, since my laptop doesn't have discrete GPU.

Next issue was that function keys weren't recognized by darktable and so most common shortcuts didn't work. This turned out to be a bug in GTK, that was already fixed and just updating GTK from outdated macports version helped (use at least 2.24.11).

All other fixes were about GUI appearance. Font subsystem on OS X has different idea about what font size numbers mean, "Sans 8" on Linux looks something like "Sans 13" on Mac. So font sizes had to be changed for OS X in several places. This fact though exposed an issue with bauhaus widgets (they are quite new after all) that wasn't specific to OS X - code made assumption that ratio between font size and its height in pixels is constant. This isn't true even for Linux systems with different DPI settings, but since cairo by default doesn't pay attention to monitor's DPI, everything looked fine. This all has been fixed, now bauhaus is correctly rendered on Linux and OS X systems with any DPI setting.

Lastly there was a mismatch in GUI colors, which made darktable look somewhat ugly. It was probably the most hard problem to debug and fix. It turned out to be caused by use of different functions to set color space in cairo and gtk quartz backends. Apple documentation wrongly stated though that both variants are actually equivalent, so it took some time for me and GTK+ developers to figure out what was happening. Details and patch can be found in [GNOME bugzilla](https://bugzilla.gnome.org/show_bug.cgi?id=681784).


# To be done


OpenMP is still disabled on OS X. System compiler is too old to support it and I'm still to experiment with other options.

Creating application bundle is obviously the final target of this process, there's a script for that already in git repository, but it needs to be tested and most likely adjusted.


# Feedback required


Though darktable appears to run stably on my system, I haven't actually processed any considerable number of photos with it on OS X yet. Also I use Mountain Lion, and obviously other OS X versions differ, which can expose more bugs. So you are welcome to try darktable on your Mac and report any crashes or bugs using [our bug tracker](http://www.darktable.org/redmine/projects/darktable/issues). OS X saves backtraces of all segfaults, you can find them in Console application (Diagnostic And Usage Information/User Diagnostic Reports), so please attach them to your bug reports.

To build darktable on OS X follow these steps:



	
  1. Install MacPorts (instructions and prerequisites can be found on [official website](http://www.macports.org/install.php)), please use default installation path (/opt/local)

	
  2. Add "+no_gnome +no_x11 +quartz -x11 -gnome" to /opt/local/etc/macports/variants.conf

	
  3. Install required dependencies: sudo port install git exiv2 libgphoto2 gtk-engines2 gtk-osx-application-gtk2 lensfun librsvg libsoup openexr json-glib flickcurl GraphicsMagick openjpeg15 lua webp libsecret

	
  4. Clone darktable git repository: git clone git://github.com/darktable-org/darktable.git

	
  5. Finally build and install darktable: cd darktable ; mkdir build ; cd build ; cmake .. ; make ; sudo make install


After this darktable will be installed in /usr/local directory and can be started by typing "darktable" in terminal.

**P.S.**

There's an issue with gphoto on OS X, which prevents a plugged-in camera from appearing in darktable - OS X starts PTPCamera daemon when it detects a camera, which blocks the access to the device from any other application. To fix it simply run "killall PTPCamera" command after connecting the camera. An automated solution also exists (I haven't tried it myself, so no warranties): [http://valelab.ucsf.edu/~MM/MMwiki/index.php/GPhoto](http://valelab.ucsf.edu/~MM/MMwiki/index.php/GPhoto) (scroll to the bottom).

[![darktable on OS X](http://www.darktable.org/wp-content/uploads/2012/08/dtonosx.png)](http://www.darktable.org/2012/08/bringing-current-darktable-to-os-x/dtonosx/)


