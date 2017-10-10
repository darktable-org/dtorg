Title: about
Date: 2017-05-23T15:16:37-06:00


*darktable is an open source photography workflow application and raw developer. A virtual lighttable and darkroom for photographers. It manages your digital negatives in a database, lets you view them through a zoomable lighttable and enables you to develop raw images and enhance them.*

Raw is the unprocessed capture straight from the camera's sensor to the memory card, nothing has been altered. There are multiple alternatives in the open source world for raw development (ufraw, dcraw, rawtherapee) but darktable tries to fill the gap between the excellent existing free raw converters and image management tools (such as e.g. ufraw, rawstudio, f-spot, digikam, shotwell). It focuses on the workflow to make it easier for the photographer to quickly handle the thousands of images a day of shooting can produce. It's also one of the very few FOSS projects able to do tethered shooting.

The internal architecture of darktable allows users to easily add modules for all sorts of image processing, from the very simple (crop, exposure, spot removal) to the most advanced (simulation of human night vision).

The user interface is built around efficient caching of image metadata and mipmaps, all stored in a database. The main focus lies on user interaction, both in terms of a smooth interface design as well as processing speed. High quality output is also one of our goals.

All editing is fully non-destructive and only operates on cached image buffers for display. The full image is only converted during export. Raw image loading is done using rawspeed, high-dynamic range and standard image formats such as jpeg are also supported. The core operates completely on floating point values, so darktable can not only be used for photography but also for scientifically acquired images or output of renderers (high dynamic range).

For a more complete list of darktable's current features have a look at the [features]({filename}/pages/about/features.md) page. Or&nbsp;– even better&nbsp;– just [install]({filename}/pages/install.md) it and try it out!

darktable is released under the terms of the [GNU General Public License Version 3](https://www.gnu.org/licenses/gpl-3.0.txt) or later.

