author: houz
comments: true
date: 2015-10-20 15:36:49+00:00
layout: post
link: http://www.darktable.org/2015/10/released-darktable-1-6-9/
slug: released-darktable-1-6-9
title: released darktable 1.6.9
wordpress_lede: dt-3.jpg
wordpress_id: 3820
tags: announcement, darktable

We are happy to announce that darktable 1.6.9 has been released.

The release notes and relevant downloads can be found attached to this git tag:
[ https://github.com/darktable-org/darktable/releases/tag/release-1.6.9](https://github.com/darktable-org/darktable/releases/tag/release-1.6.9)
Please only use our provided packages ("darktable-1.6.9.*" tar.xz and dmg) not the auto-created tarballs from github ("Source code", zip and tar.gz). The latter are just git snapshots and will not work! Here are the direct links to tar.xz and dmg:
[ https://github.com/darktable-org/darktable/releases/download/release-1.6.9/darktable-1.6.9.tar.xz](https://github.com/darktable-org/darktable/releases/download/release-1.6.9/darktable-1.6.9.tar.xz)
[ https://github.com/darktable-org/darktable/releases/download/release-1.6.9/darktable-1.6.9.dmg](https://github.com/darktable-org/darktable/releases/download/release-1.6.9/darktable-1.6.9.dmg)

this will likely be the last maintenance release in our 1.6 major release
series

    
    $ sha256sum darktable-1.6.9.tar.xz
    0f721e9d298a9407f6c0325d9c95b9dc37fa60f3b6a2f2e3b5675ff97c423173 
    darktable-1.6.9.tar.xz
    $ sha256sum darktable-1.6.9.dmg
    f79b0c4f317f87aab353c25216f2a3628efa2a072b1ce64c21d075a3dda54e9e 
    darktable-1.6.9.dmg




## general





	
  * don't build with external lua 5.3 or higher (darktable MUST be built with
lua 5.2)

	
  * format datetime locale dependant (and try to handle timezones better)

	
  * fix various minor memory leaks

	
  * use sRGB as display profile on all versions of OS X, fixes monitor profile
being applied twice




## rawspeed


(newly added camera support should be considered experimental for the
time being):



	
  * Olympus E-M10 Mk2

	
  * Canon G3 X

	
  * Canon PowerShot SX60 HS

	
  * Sony A7R II

	
  * Fuji X-A2

	
  * Panasonic FZ1000 bad pixel detection

	
  * alias Panasonic TZ70/ZS50 to the TZ71

	
  * improve Samsung NX1/NX500 support (handle 12bit modes)

	
  * don't load broken Kodak kdc files




## white balance presets





	
  * Olympus E-M10 Mk2

	
  * Canon PowerShot SX60 HS

	
  * Canon PowerShot G7 X

	
  * Sony A7R II

	
  * Sony A7 II

	
  * Sony RX100M4

	
  * Sony RX10

	
  * Nikon 1 J5




## noiseprofiles





	
  * Nikon D3300

	
  * Canon PowerShot S120




## translations





	
  * Swedish (small updates)


