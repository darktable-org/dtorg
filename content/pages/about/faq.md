Title: faq
Slug: about/faq
Date: 2017-09-20T16:18:43-06:00
author: smn
wordpress_id: 1536
lede: lede-faq.jpg
lede_author: <a href="https://jo.dreggn.org/home/">jo</a>

* **What's the best way to contact the developers/report bugs?**

    For fast discussions and short questions it's best to visit us in IRC (on Freenode, channel #darktable), especially in the Western European evening hours. If you don't want to use IRC, don't know what it is or want something less transient you can use our mailing lists. See our [contact page]({filename}/pages/contact.md).

* **After updating my system I suddenly see red borders and giant buttons everywhere!**

    darktable uses GTK3 to create its GUI. We make heavy use of styling to change the look to what you are used to. Unfortunately there were several incompatible changes in the past with how GTK3 handles that. As a result darktable needs to be compiled for the same version of the library as what it's being used with later. Otherwise you risk GTK3 not supporting the stylesheet darktable uses. When you see those red borders that's exactly what's happening.

    * Most of the time this happens when using third party package repos like Pascal's PPA on Ubuntu. When upgrading the base system the PPA gets disabled while the old darktable package is still installed. Just make sure to re-enable it, point it to the right distro release version and update darktable. That should fix the problem.
    * If you compiled darktable yourself make sure to remove both the installed files as well as your build/ folder before re-compiling.
    * If you use your system's official darktable package you should file a bug report against the distribution and ask them to build a new package.
    * It is possible to customize the looks of darktable by copying the `darktable.css` file to `~/.config/darktable/` and editing it. If you did that with an old version of the stylesheet it might no longer be compatible when updating darktable. Please update your CSS file.

* **How do I rename files on my hard disk?**

    Use your file manager (or the command line). You already know how to do that. We have image editing code to write so we don't spend time to rewrite a file manager. Just make sure to first remove the files from darktable's library, then rename them and re-import them afterwards.

* **Will you add file manager capabilities in the future?**

    No.

* **How do I change the order in which modules are applied to an image?**

    You don't. The order of the processing pixel pipeline is fixed and supposed to "just work". If you have a (valid) use case where the order doesn't work feel free to tell us. And if you really want to know the reason why this is fixed you may want to have a look at the output SVG of `tools/iop_dependencies.py`

* **Modules? What modules?**

    See the section below about the manual, book and tutorial videos.

* **darktable crashes with SIGILL. What's up?**

    Due to the large number of mathematically intense operations which the Image Operators (IOPs) perform, the minimum requirement for a CPU to run darktable is one which supports SSE2. If your cpu does not support SSE2 more than fifteen years after the feature's introduction, then it really is time for you to upgrade. Please see [the Wikipedia page](https://en.wikipedia.org/wiki/SSE2) for more details on SSE2-capable CPUs.

* **How do I open images? I only see a grey canvas.**

    You have to import a single image or a film roll (directory) using the buttons on the left side of the lighttable.

* **Ok, I imported some images, but I still don't see anything, though after importing a single image it is shown in darkroom mode.**

    Try to set the display filter in the top panel to "all" and check the "initial rating when importing filmrolls" setting in the preference pane (the small gear wheel at the top).

* **How do I save my changes?**

    You don't have to. Everything you do is immediately stored on disk. You can just quit darktable and go on editing later. Once you are done you have to _export_ your final image (while in lighttable mode) using the export module.

* **What happened to the demosaic module in darkroom? How can I select more demosaicing algorithms?**

    We moved the demosaicing into our internal pixel pipeline. The benefit is that it is faster and more accurate. The downside is that we have to implement the demosaicing algorithms ourselves. Since the differences are really small with real world photos we didn't bother to port more than PPG and AMaZE. If anyone feels the need for more choice we will gladly accept patches.

* **This confuses me. Is there a manual?**

    Yes, [here](/usermanual/en/). There is also [a book]({filename}/pages/resources/resources.md#the-book) in finished PDF format or .zip file containing the Open Document source and image files. Pascal has created some [screencast tutorials]({filename}/pages/resources/resources.md#screencast-tutorials) that cover many fundamental use cases and descriptions of technical expressions. You might also want to read through the [blog section](/blog/) of this website.

* **My auto-applied presets aren't enabled for pictures imported before upgrade to version 1.1 (or higher), what's happening?**

    *This question is probably not affecting many people these days, but we kept it for historical reasons.*

    This is intended. In pre-1.1 era enabled by default modules didn't get recorded in the history stack, which meant that changing these presets would retroactively change your pictures. It was decided that this is totally broken behaviour and since darktable version 1.1 auto-enabled modules for newly imported pictures are saved in history stack. However this change left all old photos without any user-defined auto-applied presets enabled. To fix this you will have to manually edit them. We suggest making a style out of preset, filtering photos to which it should apply using collect module, then selecting all in resulting collection and applying the style, repeat for every needed preset.

* **I attached and turned on my camera, but it doesn't show up in darktable, what's wrong?**

    If the camera in question is supported by libgphoto2, then the most likely cause is that some other process is blocking the device.

    If you're using Linux, check that your desktop environment hasn't auto-mounted it.

    In case of OS X, there's PTPCamera daemon which starts for every attached camera, so you must kill it before you can use the camera in darktable. Either run `killall PTPCamera` or implement more automated solution like described at the bottom of this page: [https://micro-manager.org/wiki/GPhoto](https://micro-manager.org/wiki/GPhoto).

    On Windows the situation is a little more complicated. libgphoto2 doesn't work with the default Windows drivers used for connecting them via USB. For tethering to work (in general for libgphoto2 and libusb to work):

    * Use [this program](http://zadig.akeo.ie/) to install USB driver on Windows for your camera
    * Follow [the description](https://github.com/pbatard/libwdi/wiki/Zadig).
    * When you run it, replace the current Windows camera driver with WinUSB driver.
    * Start darktable after replacing the driver.

    In rare cases that might break other software accessing the camera though! If you experience this, you can roll back, and remove the WinUSB driver following [this description](https://github.com/pbatard/libwdi/wiki/FAQ#Help_Zadig_replaced_the_driver_for_the_wrong_device_How_do_I_restore_it) – but then your camera won't work with darktable.

* **I see there is now a new Windows version, what can I expect?**

    The Windows port is relatively new, and therefore might have some rough edges, or missing functionality compared to the more mature OS ports. If you experience problems, please check the next few known issues below specific to the Windows port. If you don't find your answer or believe that you have found a new bug, please report it through our [bug tracking](https://redmine.darktable.org/projects/darktable/issues/new) system.

    * **How does the OpenCL support in darktable work on Windows?**

        The Windows port of darktable fully supports OpenCL with all the performance benefits, assuming you have a GPU with appropriate OpenCL drivers installed. Popular NVIDIA and AMD GPUs are working fine, but please note that in some cases the default drivers which are installed/updated by Windows Update are not necessarily containing the OpenCL driver. The best solution is typically to install the driver directly from the GPU manufacturers (like) [NVIDIA drivers](http://www.nvidia.com/Download/index.aspx?lang=en-us) or [AMD drivers](http://support.amd.com/en-us/download)), and check the OpenCL support at the driver first.

        * You can always run an OpenCL test by launching `C:\Program Files\darktable\bin\darktable-cltest.exe` from a command line window, this will give you detailed information on your current OpenCL status.

    * **I cannot see the Print module in the Windows version. How can I print my images?**

        Please be patient, currently you can not print. The Print module in darktable is using [CUPS](https://en.wikipedia.org/wiki/CUPS) on all operating systems, but that is not available on Windows. This means there was no easy way to port that functionality, and it will require further efforts to find a proper solution for printing in the Windows version as well. Until that time you can use your favorite image printing software separately to print the exported images.

    * **I have started darktable and its user interface is Finnish/Italian/Urdu/etc. How can I change the language of the user interface to English?**

        By default darktable uses you operating system's language and if a localization is available in that language it will start using that localization for the user interface. You can override that and switch to an English user interface in multiple ways:

        * You can launch darktable using the command line `darkable --conf ui_last/gui_language=C`
        * You can change the darktable shortcut at the Start Menu and append `--conf ui_last/gui_language=C` to the Target field
        * You can change this setting in the configuration file itself. Open with an editor the configuration file of darktable `C:\Users\[[username]]\AppData\Local\darktable\darktablerc`, find the line `ui_last/gui_language=` and modify it to `ui_last/gui_language=C`. Please use a text editor which can handle Unix line endings, like Notepad++ or similar

    * **I try to export to a TIFF file and it takes ages, what's happening?**

        We have got a few similar reports on slow TIFF export, but so far we were not able to reproduce it. If you have this problem, please help us by reproducing it and sharing the image file and the reproduction steps using the [bug tracking](https://redmine.darktable.org/projects/darktable/issues/new) system.

    * **I export my image with a filename which contains some non-English characters, and it's not working perfectly, what can I do?**

        Windows handles path names very differently than Unix-like systems. One of the biggest challenges of porting to Windows was making sure that path and file name handling works both on original Unix-like operating systems and also on Windows. While we have tested the Windows port with various Unicode path and file names, it still can happen that it won't work in all cases, mostly due to external libraries used by darktable. In such cases you can fall back using plain ASCII characters in path and file names, but please also file a [bug report](https://redmine.darktable.org/projects/darktable/issues/new).

    * **I was working with darktable and it suddenly just crashed! What should I do?**

        Don't panic, sometimes it happens. If you can reproduce the crash, please file a [bug report](https://redmine.darktable.org/projects/darktable/issues/new), and send the so called "backtrace" file as well. You can find the location of this backtrace file in the folder where the crash dialog indicates.
