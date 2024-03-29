---
author: Pascal Obry
date: 2023-07-22 01:00:00+00:00
layout: post
title: "darktable 4.4.2 released"
lede: ladefense.jpg
lede_author: Pascal Obry
tags:
  - announcement
  - darktable release
---

We're proud to announce the new corrective release of darktable, 4.4.2!

The github release is here: [https://github.com/darktable-org/darktable/releases/tag/release-4.4.2](https://github.com/darktable-org/darktable/releases/tag/release-4.4.2).

As always, please don't use the autogenerated tarball provided by
github, but only our tar.xz file. The checksums are:

```
$ sha256sum darktable-4.4.2.tar.xz
c11d28434fdf2e9ce572b9b1f9bc4e64dcebf6148e25080b4c32eb51916cfa98  darktable-4.4.2.tar.xz
$ sha256sum darktable-4.4.2-x86_64.dmg
9eb84ea041daad704a8d4226d8c7cba77522dcd003d7166961869b1cfaa9ac9a  darktable-4.4.2-x86_64.dmg
$ sha256sum darktable-4.4.2-arm64.dmg
4576f4cc25f96d5a2334993bb847e826591b3190ddf24fb83461df093ce8ee2a  darktable-4.4.2-arm64.dmg
$ sha256sum darktable-4.4.2-win64.exe
3f3557281a24f61080181cbde09c3d0f9853f81ff08485247e844afa9b2171a6  darktable-4.4.2-win64.exe
```

When updating from the stable 4.2.x series, please bear in
mind that your edits will be preserved during this process, but the new
library and configuration will no longer be usable with 4.2.x.

You are strongly advised to take a backup first.

#### Important note: to make sure that darktable can keep on supporting the raw file format for your camera, *please* read [this post](https://discuss.pixls.us/t/raw-samples-wanted/5420?u=lebedevri) on how/what raw samples you can contribute to ensure that we have the *full* raw sample set for your camera under CC0 license!

Since darktable 4.4.1:

- 53 commits to darktable+rawspeed
- 19 pull requests handled
-  1 issues closed


_Please note that the darktable documentation is not currently complete for release 4.4
and contributions are greatly appreciated. Please see the
[project documentation](https://github.com/darktable-org/dtdocs#contributing)
for more information on how to contribute._

## Bug Fixes

- Graduated Density : Fix density computation for negative EVs.

- Fixed wrong allocation of OpenCL image buffers for blending in
  DEVELOP_BLEND_CS_RAW.

- Fixed roi_in calculation in highlights and RAW Chromatic
  Aberrations modules.

- Fix snap to grid for cm/inch units in print view. Only mm was
  properly handled.

- Fix issue where the highlight reconstruction method was reset to
  clip when applying a style from the lighttable.

- Fix loading some image format using GraphicMagick on Windows.

- Fix some possible wrong pixels at the lower-right border of images
  due to some miscalculation in Input Color Profile & Color Balance.

- Fix retouch module ROI computation when a crop is active making some
  clone area inactive when the source was outside of the cropped
  area. This bug was only visible in darkroom main view.

- Fix positioning of demosaicer RoI in according to algorithm and
  sensor. Avoid some possible (small) black artifacts on image
  borders.

## Lua

### API Version

- N/A

### Other Lua changes

- N/A

## Notes

- When exporting to AVIF, EXR, JPEG XL, or XCF, selecting specific
  metadata (e.g. geo tag or creator) is not currently possible. For
  AVIF, EXR, JPEG XL, and XCF formats, darktable will not include any
  metadata fields unless the user selects all of the checkboxes in the
  export preference options.

- In order to support the correct display of numbers in darktable, the
  minimum supported Gtk version has had to be increased to
  3.24.15. For people who need to build darktable with an older
  version, this can be achieved by removing line 241 of the
  `darktable.css` file on your system. See
  https://github.com/darktable-org/darktable/issues/13166.

- Starting with this release a new support policy regarding macOS
  versions will be in place -- darktable releases will now only
  support those macOS versions that are also supported by Apple.
  Release 4.4 therefore drops support for macOS versions older than
  11.3.

## Changed Dependencies

### Mandatory

- None

### Optional

- None

## RawSpeed changes


## Camera support, compared to 4.2

### Base Support

- N/A

### White Balance Presets

### Noise Profiles

### Missing Compression Mode Support

- Apple ProRAW DNGs
- CinemaDNG lossless (Blackmagic, DJI, etc.)
- Fujifilm lossy RAFs
- Nikon high efficiency NEFs
- Samsung Expert RAW DNGs

### Suspended Support

Support for the following cameras is suspended because no samples
are available on raw.pixls.us:

- Creo/Leaf Aptus 22(LF3779)/Hasselblad H1
- Fujifilm FinePix S9600fd
- Fujifilm IS-1
- GoPro FUSION
- Kodak EasyShare Z980
- Leaf Aptus-II 5(LI300059)/Mamiya 645 AFD
- Leaf Credo 60
- Leaf Credo 80
- Minolta DiMAGE 5
- Olympus SP320
- Panasonic DMC-FX150
- Pentax Q10
- Phase One IQ250
- Samsung GX10
- Samsung GX20
- Samsung EK-GN120
- Samsung SM-G920F
- Samsung SM-G935F
- Sinar Hy6/ Sinarback eXact
- ST Micro STV680

## Translations

- New English translation with capital letters
- German
- European Spanish
- Finnish
- French
- Hebrew
- Hungarian
- Japanese
- Polish
- Brazilian Portuguese
- Russian
- Turkish
- Slovenian
- Albanian
- Ukrainian
- Chinese - China
- Chinese - Taiwan
