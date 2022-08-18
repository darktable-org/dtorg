---
Title: faq
Date: 2017-09-20T16:18:43-06:00
author: smn
wordpress_id: 1536
lede: lede-faq.jpg
lede_author: <a href="https://jo.dreggn.org/home/">jo</a>
weight: 1
menu: "footer"
---
* <a name="faq-spelling"></a>**So, I have seen a bunch of different ways to spell *darktable*. Which one is right?**<a href="#faq-spelling" class="anchor" title="Link to this FAQ entry">¶</a>

    There is only one way, and that is "darktable". All lower case, in one word, except when starting a sentence.

* <a name="faq-contact"></a>**What's the best way to contact the developers/report bugs?**<a href="#faq-contact" class="anchor" title="Link to this FAQ entry">¶</a>

    For fast discussions and short questions it's best to visit us in IRC (on _irc.oftc.net_, channel #darktable), especially in the Western European evening hours. If you don't want to use IRC, don't know what it is or want something less transient you can use our mailing lists. See our [contact page](/contact).

* <a name="faq-red-borders"></a>**After updating my system I suddenly see red borders and giant buttons everywhere!**<a href="#faq-red-borders" class="anchor" title="Link to this FAQ entry">¶</a>

    darktable uses GTK3 to create its GUI. We make heavy use of styling to change the look to what you are used to. Unfortunately there were several incompatible changes in the past with how GTK3 handles that. As a result darktable needs to be compiled for the same version of the library as what it's being used with later. Otherwise you risk GTK3 not supporting the stylesheet darktable uses. When you see those red borders that's exactly what's happening.

    * Most of the time this happens when using third party package repos like Pascal's PPA on Ubuntu. When upgrading the base system the PPA gets disabled while the old darktable package is still installed. Just make sure to re-enable it, point it to the right distro release version and update darktable. That should fix the problem.
    * If you compiled darktable yourself make sure to remove both the installed files as well as your build/ folder before re-compiling.
    * If you use your system's official darktable package you should file a bug report against the distribution and ask them to build a new package.
    * It is possible to customize the look of darktable by following these steps:
        * creating a CSS file (for example mytheme.css) on following folder:
             * **2.4.x and 2.6.x releases:** `~/.config/darktable/`
             * **On 3.0.x release:** `~/.config/darktable/themes` (themes folder needs to be created if it doesn't exist)
        * then add the following line on the beginning of the created css file: `@import url("/path/to/darktable.css");`, where the `/path/to/darktable.css` is the path... to the default darktable CSS (or one of the other themes you want to edit).
        * last step is to copy parts of the pointed css you want to edit and adjust settings as you want.
    * Be aware: darktable 3.0 brings a whole new UI, so 3.0 CSS themes are not compatible with previous releases, and previous 2.4 and 2.6 themes are not compatible with darktable 3.0.

    Since darktable 3.2, released in august 2020, CSS tweaks are far easier. Forget the steps described just above for that and just go into the preferences window. In the general tab: select your theme, check _modify selected theme with tweaks below_ and add your tweaks in text field below. That's all!

    By the way, CSS file should be easier to read and lot of comments will help you find faster CSS part you want to tweak and so copy/modify in preferences.

* <a name="faq-rename-files"></a>**How do I rename files on my hard disk?**<a href="#faq-rename-files" class="anchor" title="Link to this FAQ entry">¶</a>

    Use your file manager (or the command line). You already know how to do that. We have image editing code to write so we don't spend time to rewrite a file manager. Just make sure to first remove the files from darktable's library, then rename them and re-import them afterwards.

* <a name="faq-filemanager"></a>**Will you add file manager capabilities in the future?**<a href="#faq-filemanager" class="anchor" title="Link to this FAQ entry">¶</a>

    No.

* <a name="faq-moduleorder"></a>**How do I change the order in which modules are applied to an image?**<a href="#faq-moduleorder" class="anchor" title="Link to this FAQ entry">¶</a>

    See the [user manual](/usermanual/en/darkroom/pixelpipe/the-pixelpipe-and-module-order/#changing-module-order) for more details.

* <a name="faq-modules"></a>**Modules? What modules?**<a href="#faq-modules" class="anchor" title="Link to this FAQ entry">¶</a>

    See the section below about the manual, book and tutorial videos.

* <a name="faq-sigill"></a>**darktable crashes with SIGILL. What's up?**<a href="#faq-sigill" class="anchor" title="Link to this FAQ entry">¶</a>

    Due to the large number of mathematically intense operations which the Image Operators (IOPs) perform, the minimum requirement for a CPU to run darktable is one which supports SSE2. If your cpu does not support SSE2 more than fifteen years after the feature's introduction, then it really is time to upgrade. Please see [the Wikipedia page](https://en.wikipedia.org/wiki/SSE2) for more details on SSE2-capable CPUs.

* <a name="faq-import"></a>**How do I open images? I only see a grey canvas.**<a href="#faq-import" class="anchor" title="Link to this FAQ entry">¶</a>

    You have to import a single image or a film roll (directory) using the buttons on the left side of the lighttable.

* <a name="faq-filter"></a>**Ok, I imported some images, but I still don't see anything, though after importing a single image it is shown in darkroom mode.**<a href="#faq-filter" class="anchor" title="Link to this FAQ entry">¶</a>

    Try to set the display filter in the top panel to "all" and check the "initial rating when importing filmrolls" setting in the preference pane (the small gear wheel at the top).

* <a name="faq-save"></a>**How do I save my changes?**<a href="#faq-save" class="anchor" title="Link to this FAQ entry">¶</a>

    You don't have to. Everything you do is immediately saved. You can just quit darktable and go on editing later. Once you are done you have to _export_ your final image (while in lighttable mode) using the export module.

* <a name="faq-demosaic"></a>**What happened to the demosaic module in darkroom? How can I select more demosaicing algorithms?**<a href="#faq-demosaic" class="anchor" title="Link to this FAQ entry">¶</a>

    We moved the demosaicing into our internal pixel pipeline. The benefit is that it is faster and more accurate. The downside is that we have to implement the demosaicing algorithms ourselves. Since the differences are really small with real world photos we didn't bother to port more than PPG and AMaZE. If anyone feels the need for more choice we will gladly accept patches.

* <a name="faq-docs"></a>**This confuses me. Is there a manual?**<a href="#faq-docs" class="anchor" title="Link to this FAQ entry">¶</a>

    Yes, [here](/usermanual/en/). You might also want to read through the [blog section](/blog/) of this website.

* <a name="faq-old-presets"></a>**My auto-applied presets aren't enabled for pictures imported before upgrade to version 1.1 (or higher), what's happening?**<a href="#faq-old-presets" class="anchor" title="Link to this FAQ entry">¶</a>

    *This question is probably not affecting many people these days, but we kept it for historical reasons.*

    This is intended. In the pre-1.1 era, modules that were enabled by default didn't get recorded in the history stack, which meant that changing these presets would retroactively change your pictures. It was decided that this is totally broken behaviour and since darktable version 1.1 auto-enabled modules for newly imported pictures are saved in history stack. However this change left all old photos without any user-defined auto-applied presets enabled. To fix this you will have to manually edit them. We suggest making a style out of preset, filtering photos to which it should apply using collect module, then selecting all in resulting collection and applying the style, repeat for every needed preset.

* <a name="faq-tethering"></a>**I attached and turned on my camera, but it doesn't show up in darktable, what's wrong?**<a href="#faq-tethering" class="anchor" title="Link to this FAQ entry">¶</a>

    If the camera in question is supported by `libgphoto2`, then the most likely cause is that some other process is blocking the device.

    If you're using Linux, check that your desktop environment hasn't auto-mounted it.

    In case of OS X, there's PTPCamera daemon which starts for every attached camera, so you must kill it before you can use the camera in darktable. Either run `killall PTPCamera` or implement more automated solution like described at the bottom of this page: [https://micro-manager.org/wiki/GPhoto](https://micro-manager.org/wiki/GPhoto).

    On Windows the situation is a little more complicated. libgphoto2 doesn't work with the default Windows drivers used for connecting them via USB. For tethering to work (in general for libgphoto2 and libusb to work):

    * Use [this program](http://zadig.akeo.ie/) to install USB driver on Windows for your camera
    * Follow [the description](https://github.com/pbatard/libwdi/wiki/Zadig).
    * When you run it, replace the current Windows camera driver with WinUSB driver.
    * Start darktable after replacing the driver.

    In rare cases that might break other software accessing the camera though! If you experience this, you can roll back, and remove the WinUSB driver following [this description](https://github.com/pbatard/libwdi/wiki/FAQ#Help_Zadig_replaced_the_driver_for_the_wrong_device_How_do_I_restore_it) – but then your camera won't work with darktable.

* <a name="faq-external-deps"></a>**So, darktable uses gphoto2 for tethering. Are there any more third party projects influencing what works in darktable and what's not?**<a href="#faq-external-deps" class="anchor" title="Link to this FAQ entry">¶</a>

    Yes, there are two libraries we heavily rely on and which we point to quite often when people complain about darkable lacking something:

    * **exiv2** is used for reading metadata from image files. If something isn't shown correctly in the [image information](/usermanual/en/image_information.html) panel on the left side then please check with the command line tool `exiv2` and report any problems upstream on [their bug tracker](https://github.com/Exiv2/exiv2/issues)&nbsp;– there isn't much we can do to fix those things ourselves.
    * **lensfun** is used for lens correction. If the [lens correction](/usermanual/en/correction_group.html#lens_correction) module isn't showing your camera or lens, or a wrong one, then please report that to [those folks](https://github.com/lensfun/lensfun).

* <a name="faq-windows"></a>**I see there is now a new Windows version, what can I expect?**<a href="#faq-windows" class="anchor" title="Link to this FAQ entry">¶</a>

    The Windows port is relatively new, and therefore might have some rough edges, or missing functionality compared to the more mature OS ports. If you experience problems, please check the next few known issues below specific to the Windows port. If you don't find your answer or believe that you have found a new bug, please report it through our [bug tracking](https://github.com/darktable-org/darktable/issues) system.

    * <a name="faq-windows-opencl"></a>**How does the OpenCL support in darktable work on Windows?**<a href="#faq-windows-opencl" class="anchor" title="Link to this FAQ entry">¶</a>

        The Windows port of darktable fully supports OpenCL with all the performance benefits, assuming you have a GPU with appropriate OpenCL drivers installed. Popular NVIDIA and AMD GPUs are working fine, but please note that in some cases the default drivers which are installed/updated by Windows Update are not necessarily containing the OpenCL driver. The best solution is typically to install the driver directly from the GPU manufacturers (like) [NVIDIA drivers](http://www.nvidia.com/Download/index.aspx?lang=en-us) or [AMD drivers](http://support.amd.com/en-us/download)), and check the OpenCL support at the driver first.

        * You can always run an OpenCL test by launching `C:\Program Files\darktable\bin\darktable-cltest.exe` from a command line window, this will give you detailed information on your current OpenCL status.

    * <a name="faq-windows-print"></a>**I cannot see the Print module in the Windows version. How can I print my images?**<a href="#faq-windows-print" class="anchor" title="Link to this FAQ entry">¶</a>

        Please be patient, currently you can not print. The Print module in darktable is using [CUPS](https://en.wikipedia.org/wiki/CUPS) on all operating systems, but that is not available on Windows. This means there was no easy way to port that functionality, and it will require further efforts to find a proper solution for printing in the Windows version as well. Until that time you can use your favorite image printing software separately to print the exported images.

    * <a name="faq-windows-config"></a>**I read in the manual about changing some configuration setting, which supposed to be located in the user config directory. Where is the config file in the Windows version?**<a href="#faq-windows-config" class="anchor" title="Link to this FAQ entry">¶</a>

         The configuration file of darktable is located at `C:\Users\[username]\AppData\Local\darktable\darktablerc`. If you change it please use a text editor which can handle Unix line endings, like Notepad++ or similar.

    * <a name="faq-windows-language"></a>**I have started darktable and its user interface is Finnish/Italian/Urdu/etc. How can I change the language of the user interface to English?**<a href="#faq-windows-language" class="anchor" title="Link to this FAQ entry">¶</a>

        By default darktable uses your operating system's language and if a localization is available in that language it will start using that localization for the user interface. You can override that and switch to an English user interface in multiple ways:

        * You can launch darktable using the command line `darkable --conf ui_last/gui_language=C`
        * You can change the darktable shortcut at the Start Menu and append `--conf ui_last/gui_language=C` to the Target field
        * You can change this setting in the configuration file itself. Open with an editor the configuration file of darktable `C:\Users\[username]\AppData\Local\darktable\darktablerc`, find the line `ui_last/gui_language=` and modify it to `ui_last/gui_language=C`. Please use a text editor which can handle Unix line endings, like Notepad++ or similar

    * <a name="faq-windows-tiff"></a>**I try to export to a TIFF file and it takes ages, what's happening?**<a href="#faq-windows-tiff" class="anchor" title="Link to this FAQ entry">¶</a>

        We have got a few similar reports on slow TIFF export, and we have identified the root cause in an upstream system. Please update your darktable install, the fixes are part of the installer since 2.4.1.

    * <a name="faq-windows-logs"></a>**I read a lot of information in the manual to turn on some debug settings, but I cannot see any debug information. Where can I find those debug logs?**<a href="#faq-windows-logs" class="anchor" title="Link to this FAQ entry">¶</a>

        The Windows version of dt by default logs its debug information to the following places:

        Windows 10:
        `C:\Users\[username]\AppData\Local\Microsoft\Windows\INetCache\darktable\darktable-log.txt`

        Windows 7:
        `C:\Users\[username]\AppData\Local\Microsoft\Windows\Temporary Internet Files\darktable\darktable-log.txt`

    * <a name="faq-windows-unicode"></a>**I export my image with a filename which contains some non-English characters, and it's not working perfectly, what can I do?**<a href="#faq-windows-unicode" class="anchor" title="Link to this FAQ entry">¶</a>

        Windows handles path names very differently than Unix-like systems. One of the biggest challenges of porting to Windows was making sure that path and file name handling works both on original Unix-like operating systems and also on Windows. While we have tested the Windows port with various Unicode path and file names, it still can happen that it won't work in all cases, mostly due to external libraries used by darktable. In such cases you can fall back using plain ASCII characters in path and file names, but please also file a [bug report](https://github.com/darktable-org/darktable/issues).

    * <a name="faq-windows-bugs"></a>**I was working with darktable and it suddenly just crashed! What should I do?**<a href="#faq-windows-bugs" class="anchor" title="Link to this FAQ entry">¶</a>

        Don't panic, sometimes it happens. If you can reproduce the crash, please file a [bug report](https://github.com/darktable-org/darktable/issues), and send the so called "backtrace" file as well. You can find the location of this backtrace file in the folder where the crash dialog indicates.
