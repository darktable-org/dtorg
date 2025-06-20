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

## New Users

### <a name="faq-lightroom"></a>Is darktable a free Lightroom alternative?<a href="#faq-lightroom" class="anchor" title="Link to this FAQ entry">¶</a>
No. Other than both being raw editors with DAM features, and looking somewhat similar, they have very little in common. Darktable is a powerful and flexible raw processing toolbox, that leaves the user in charge of their workflow and provides a level of power and control that few others can match. This also means that the initial learning curve can be steep, since very little workflow and tool knowledge can be transferred from other programs.

### <a name="faq-presets"></a>Is darktable compatible with presets from other programs?<a href="#faq-presets" class="anchor" title="Link to this FAQ entry">¶</a>
No. Presets (what darktable calls styles) are specific to the program that created them. It can, however, use LUTs in several different formats, so that may be a solution if cross-program compatibility is needed.

### <a name="faq-import-edits"></a>Can darktable import edits from other programs?<a href="#faq-import-edits" class="anchor" title="Link to this FAQ entry">¶</a>
No. Due to differences in how processing works in different programs, this is simply not possible to do properly. There is some very basic support for importing Lightroom edits, but that code is old and somewhat broken and you're probably best off discarding the edit history after import and just start over.

### <a name="faq-camera-support"></a>Is my camera supported?<a href="#faq-camera-support" class="anchor" title="Link to this FAQ entry">¶</a>
Please see the [camera support page](/resources/camera-support/).

### <a name="faq-file-support"></a>My camera is supported, but darktable can't open the photos<a href="#faq-file-support" class="anchor" title="Link to this FAQ entry">¶</a>
Some file formats are not supported. The camera support page has a full list.

### <a name="faq-initial-look"></a>Why doesn’t the raw image look like the JPEG?<a href="#faq-initial-look" class="anchor" title="Link to this FAQ entry">¶</a>
This is explained [in the manual](https://docs.darktable.org/usermanual/stable/en/overview/workflow/process/#why-doesnt-the-raw-image-look-like-the-jpeg).

### <a name="faq-grey-interface"></a>Why is the interface so flat and grey?<a href="#faq-grey-interface" class="anchor" title="Link to this FAQ entry">¶</a>
The default theme has been carefully designed to limit certain optical illusions that affect how brightness, contrast and saturation are perceived. Changing to a darker theme, in particular, can lead to images that are too dark or over-saturated. This is explained in detail in the manual [here](https://docs.darktable.org/usermanual/stable/en/module-reference/utility-modules/darkroom/color-assessment/), [here](https://docs.darktable.org/usermanual/stable/en/preferences-settings/general/) and [here](https://docs.darktable.org/usermanual/stable/en/overview/workflow/process/#edit-in-a-controlled-environment).

### <a name="faq-rename-files"></a>How do I rename files on my hard disk?<a href="#faq-rename-files" class="anchor" title="Link to this FAQ entry">¶</a>
Use your file manager (or the command line). Image renaming is not a feature we are developing for darktable. Make sure to first remove the files from darktable's library, then rename them (and the associated XMP sidecar files) and re-import them afterwards.

### <a name="faq-filemanager"></a>Will you add file manager capabilities in the future?<a href="#faq-filemanager" class="anchor" title="Link to this FAQ entry">¶</a>
No.

### <a name="faq-moduleorder"></a>How do I change the order in which modules are applied to an image?<a href="#faq-moduleorder" class="anchor" title="Link to this FAQ entry">¶</a>
See the [user manual](https://docs.darktable.org/usermanual/stable/en/darkroom/pixelpipe/the-pixelpipe-and-module-order/#changing-module-order) for more details.

### <a name="faq-modules"></a>Modules? What modules?<a href="#faq-modules" class="anchor" title="Link to this FAQ entry">¶</a>
darktable's interface is organised into modules. You can find a full list [in the manual](https://docs.darktable.org/usermanual/stable/en/module-reference/overview/).

### <a name="faq-import"></a>How do I open images? I only see a grey canvas.<a href="#faq-import" class="anchor" title="Link to this FAQ entry">¶</a>
You have to import a single image or a film roll (directory) using the [import module](https://docs.darktable.org/usermanual/stable/en/module-reference/utility-modules/lighttable/import/) on the left side of the lighttable.

### <a name="faq-filter"></a>Ok, I imported some images, but I still don't see anything, though after importing a single image it is shown in darkroom mode.<a href="#faq-filter" class="anchor" title="Link to this FAQ entry">¶</a>
You may have applied a filter, such as showing only certain star ratings. In either the [collection filters module](https://docs.darktable.org/usermanual/stable/en/module-reference/utility-modules/shared/collection-filters/) or [top panel](https://docs.darktable.org/usermanual/stable/en/overview/user-interface/top-panel/), make sure module order is set to "all images" and that all possible star ratings and no color labels have been selected. You may also want to check the *initial rating* parameter in the import module.

### <a name="faq-wb-error"></a>Why do I get an error about white balance being applied twice?<a href="#faq-wb-error" class="anchor" title="Link to this FAQ entry">¶</a>
This isn't really an error, but a warning that you're doing something that you probably shouldn't be doing. Normally you should set the correct white balance in Color Calibration and leave the White Balance module at its default setting.

This happens when the Color Calibration CAT is active and the White Balance module has been changed from the default (camera reference - either of the two light bulb icons). If you want to change the white balance with the White Balance module, either disable Color Calibration or, if you want to use one of the other tabs in Color Calibration, set CAT adaptation to *none (bypass)*, but be aware that the chromatic adaptation transform (CAT) done by Color Calibration is more powerful and accurate than traditional white balance and should be preferred.

For technical reasons the old White Balance module is still required when using the Color Calibration CAT, which is why both are active by default.

### <a name="faq-save"></a>How do I save my changes?<a href="#faq-save" class="anchor" title="Link to this FAQ entry">¶</a>
You don't have to. Everything you do is immediately saved. You can just quit darktable and go on editing later. Once you are done you have to _export_ your final image using the export module.

### <a name="faq-scene-referred">I keep seeing the terms display-referred and scene-referred. What do they mean?<a href="#faq-scene-referred" class="anchor" title="Link to this FAQ entry">¶</a>
The manual has [a short explanation](https://docs.darktable.org/usermanual/stable/en/overview/workflow/process/#scene-referred-workflow-a-new-approach).

[This article](https://pixls.us/articles/darktable-3-rgb-or-lab-which-modules-help/) explains them in more detail and the reasons behind darktable moving to a scene-referred workflow. Note that it was written for darktable 3.0, so some of the specific recommendations for which modules to use are no longer relevant.

Elle Stone has an article [here](https://ninedegreesbelow.com/photography/display-referred-scene-referred.html) that explains them in a more general way.

### <a name="faq-docs"></a>This confuses me. Is there a manual?<a href="#faq-docs" class="anchor" title="Link to this FAQ entry">¶</a>
Yes, [here](https://docs.darktable.org/usermanual/stable/en/). You might also want to read through the [blog section](/blog/) of this website.

### <a name="faq-forums"></a>I have read the manual and I'm still confused. Where can I get more help?<a href="#faq-forums" class="anchor" title="Link to this FAQ entry">¶</a>
The best place is the [Pixls.us discussion forum](https://discuss.pixls.us/). There you can get help with both editing and technical issues. It is also a good place to get help with other open-source graphics software.

There are also a number of video tutorials. You can find a list of some of them at the bottom of the [resources page](/resources/).


## <a name="faq-general"></a>General<a href="#faq-general" class="anchor" title="Link to this FAQ entry">¶</a>

### <a name="faq-spelling"></a>So, I have seen a bunch of different ways to spell *darktable*. Which one is right?<a href="#faq-spelling" class="anchor" title="Link to this FAQ entry">¶</a>
There is only one way, and that is "darktable". All lower case, in one word, except when starting a sentence.

### <a name="faq-contact"></a>What's the best way to contact the developers/report bugs?<a href="#faq-contact" class="anchor" title="Link to this FAQ entry">¶</a>
For issues/bugs, please use [GitHub Issues](https://github.com/darktable-org/darktable/issues). For more general help and discussion there's the [discuss.pixls.us](https://discuss.pixls.us/) forum. For fast discussions and short questions it's best to visit us in one of the IRC or Matrix channels, which are listed on the [contact page](/contact/).

### <a name="faq-deprecated-module"></a>My favourite module has been removed from darktable. What happened and can I get it back?<a href="#faq-deprecated-module" class="anchor" title="Link to this FAQ entry">¶</a>
Occasionally an old module may be deprecated and become unavailable for new edits. However, this only happens if there are quality or technical issues with that module and a suitable replacement is available.

If, for some reason, you really want to continue using it, you can open an old edit using that module and create a style, which you can then apply to new edits. But, as said, there are good reasons for why it was deprecated, so you're encouraged to use the replacement instead.

### <a name="faq-sigill"></a>darktable crashes with SIGILL. What's up?<a href="#faq-sigill" class="anchor" title="Link to this FAQ entry">¶</a>
Due to the large number of mathematically intense operations which the Image Operators (IOPs) perform, the minimum requirement for a CPU to run darktable is one which supports SSE2. If your cpu does not support SSE2 more than fifteen years after the feature's introduction, then it really is time to upgrade. Please see [the Wikipedia page](https://en.wikipedia.org/wiki/SSE2) for more details on SSE2-capable CPUs.

### <a name="faq-tethering"></a>I attached and turned on my camera, but it doesn't show up in darktable, what's wrong?<a href="#faq-tethering" class="anchor" title="Link to this FAQ entry">¶</a>
If the camera in question is supported by `libgphoto2`, then the most likely cause is that some other process is blocking the device.

If you're using Linux, check that your desktop environment hasn't auto-mounted it.

In case of Mac OS X, there's PTPCamera daemon which starts for every attached camera, so you must kill it before you can use the camera in darktable. Either run `killall PTPCamera` or implement more automated solution like described at the bottom of this page: [https://micro-manager.org/wiki/GPhoto](https://micro-manager.org/wiki/GPhoto).

On Windows the situation is a little more complicated. libgphoto2 doesn't work with the default Windows drivers used for connecting them via USB. For tethering to work (in general for libgphoto2 and libusb to work):

* Use [this program](http://zadig.akeo.ie/) to install USB driver on Windows for your camera
* Follow [the description](https://github.com/pbatard/libwdi/wiki/Zadig).
* When you run it, replace the current Windows camera driver with WinUSB driver.
* Start darktable after replacing the driver.

In rare cases that might break other software accessing the camera though! If you experience this, you can roll back, and remove the WinUSB driver following [this description](https://github.com/pbatard/libwdi/wiki/FAQ#Help_Zadig_replaced_the_driver_for_the_wrong_device_How_do_I_restore_it) – but then your camera won't work with darktable.

### <a name="faq-external-deps"></a>So, darktable uses gphoto2 for tethering. Are there any more third party projects influencing what works in darktable?<a href="#faq-external-deps" class="anchor" title="Link to this FAQ entry">¶</a>
Yes, there are two libraries we heavily rely on:

* **exiv2** is used for reading metadata from image files. If something isn't shown correctly in the [image information](https://docs.darktable.org/usermanual/stable/en/module-reference/utility-modules/shared/image-information/) panel on the left side then please check with the command line tool `exiv2` and report any problems upstream on [their bug tracker](https://github.com/Exiv2/exiv2/issues)&nbsp;– there isn't much we can do to fix those things ourselves.
* **lensfun** is used for lens correction. If the [lens correction](https://docs.darktable.org/usermanual/stable/en/module-reference/processing-modules/lens-correction/) module isn't showing your camera or lens, or a wrong one, then please report that to [those folks](https://github.com/lensfun/lensfun).


## <a name="faq-linux"></a>Linux<a href="#faq-linux" class="anchor" title="Link to this FAQ entry">¶</a>

### <a name="faq-red-borders"></a>After updating my system I suddenly see red borders and giant buttons everywhere!<a href="#faq-red-borders" class="anchor" title="Link to this FAQ entry">¶</a>
darktable uses GTK3 to create its GUI. We make heavy use of styling to change the look to what you are used to. Unfortunately there were several incompatible changes in the past with how GTK3 handles that. As a result darktable needs to be compiled for the same version of the library as what it's being used with later. Otherwise you risk GTK3 not supporting the stylesheet darktable uses. When you see those red borders that's exactly what's happening.

* Most of the time this happens when using third party package repos like Pascal's PPA on Ubuntu. When upgrading the base system the PPA gets disabled while the old darktable package is still installed. Just make sure to re-enable it, point it to the right distro release version and update darktable. That should fix the problem.
* If you compiled darktable yourself make sure to remove both the installed files as well as your build/ folder before re-compiling.
* If you use your system's official darktable package you should file a bug report against the distribution and ask them to build a new package.


## <a name="faq-windows"></a>Windows<a href="#faq-windows" class="anchor" title="Link to this FAQ entry">¶</a>
darktable is developed for Linux, but it was ported to build on Windows. The [MSYS2](https://www.msys2.org/) URCT environment is used to compile the program. Nightly builds are performed in github to ensure the program builds under Windows against the current master code. If you experience problems, please check the next few known issues below specific to the Windows port. If you don't find your answer or believe that you have found a new bug, please report it through our [bug tracking](https://github.com/darktable-org/darktable/issues) system.

### <a name="faq-windows-locations"></a>Install file locations<a href="#faq-windows-locations" class="anchor" title="Link to this FAQ entry">¶</a>
The install of darktable creates the following folders:
* `C:\Program files\darktable\` - the program files to run darktable
* `C:\Users\<username>\AppData\Local\darktable`- configuration (darktablerc.txt), databases (data.db and library.db), styles, and backups files are stored here. If the user manual references `.config/darktable/` , it means this location on Windows.

### <a name="faq-windows-opencl"></a>How does the OpenCL support in darktable work on Windows?<a href="#faq-windows-opencl" class="anchor" title="Link to this FAQ entry">¶</a>
The Windows port of darktable fully supports OpenCL with all the performance benefits, assuming you have a GPU with appropriate OpenCL drivers installed. Popular NVIDIA and AMD GPUs are working fine, but please note that in some cases the default drivers which are installed/updated by Windows Update do not necessarily contain the OpenCL driver. The best solution is typically to install the driver directly from the GPU manufacturers (like) [NVIDIA drivers](http://www.nvidia.com/Download/index.aspx?lang=en-us) or [AMD drivers](http://support.amd.com/en-us/download)), and check the OpenCL support in the driver first.

* You can always run an OpenCL test by launching `C:\Program Files\darktable\bin\darktable-cltest.exe` from a command line window, this will give you detailed information on your current OpenCL status.

### <a name="faq-windows-print"></a>I cannot see the Print module in the Windows version. How can I print my images?<a href="#faq-windows-print" class="anchor" title="Link to this FAQ entry">¶</a>
The darktable Windows packaging can not print. The Print module in darktable is using [CUPS](https://en.wikipedia.org/wiki/CUPS) on all operating systems, but that is not available on Windows. This means there was no easy way to port that functionality, and it will require further efforts to find a proper solution for printing in the Windows version as well. Until that time you can use your favorite image printing software separately to print the exported images.

### <a name="faq-windows-config"></a>I read in the manual about changing some configuration setting, which supposed to be located in the user config directory. Where is the config file in the Windows version?<a href="#faq-windows-config" class="anchor" title="Link to this FAQ entry">¶</a>
The configuration file of darktable is located at `C:\Users\[username]\AppData\Local\darktable\darktablerc`. If you change it please use a text editor which can handle Unix line endings, like Notepad++ or similar.

### <a name="faq-windows-language"></a>I have started darktable and its user interface is Finnish/Italian/Urdu/etc. How can I change the language of the user interface to English?<a href="#faq-windows-language" class="anchor" title="Link to this FAQ entry">¶</a>
By default darktable uses your operating system's language and if a localization is available in that language it will start using that localization for the user interface. You can override that and switch to an English user interface in multiple ways:

* You can launch darktable using the command line `darkable --conf ui_last/gui_language=C`
* You can change the darktable shortcut in the Start Menu and append `--conf ui_last/gui_language=C` to the Target field
* You can change this setting in the configuration file itself. Open with an editor the configuration file of darktable `C:\Users\[username]\AppData\Local\darktable\darktablerc`, find the line `ui_last/gui_language=` and modify it to `ui_last/gui_language=C`. Please use a text editor which can handle Unix line endings, like Notepad++ or similar

### <a name="faq-windows-logs"></a>I read a lot of information in the manual to turn on some debug settings, but I cannot see any debug information. Where can I find those debug logs?<a href="#faq-windows-logs" class="anchor" title="Link to this FAQ entry">¶</a>
The Windows version of **darktable (up to and including release 4.8.1**) by default logs its debug information to the following places (*This is a hidden folder in Windows, therefore copy and paste the link to windows explorer for access*):

Windows 10:
        `C:\Users\[username]\AppData\Local\Microsoft\Windows\INetCache\darktable\darktable-log.txt`

Windows 7:
        `C:\Users\[username]\AppData\Local\Microsoft\Windows\Temporary Internet Files\darktable\darktable-log.txt`


Since **darktable 5.0** the default location is:
        `C:\Users\[username]\Documents\Darktable\darktable-log.txt`

### <a name="faq-windows-unicode"></a>I export my image with a filename which contains some non-English characters, and it's not working perfectly, what can I do?<a href="#faq-windows-unicode" class="anchor" title="Link to this FAQ entry">¶</a>
Windows handles path names very differently than Unix-like systems. One of the biggest challenges of porting to Windows was making sure that path and file name handling works both on original Unix-like operating systems and also on Windows. While we have tested the Windows port with various Unicode path and file names, it still can happen that it won't work in all cases, mostly due to external libraries used by darktable. In such cases you can fall back using plain ASCII characters in path and file names, but please also file a [bug report](https://github.com/darktable-org/darktable/issues).

### <a name="faq-windows-bugs"></a>I was working with darktable and it suddenly just crashed! What should I do?<a href="#faq-windows-bugs" class="anchor" title="Link to this FAQ entry">¶</a>
Don't panic, sometimes it happens. If you can reproduce the crash, please file a [bug report](https://github.com/darktable-org/darktable/issues), and send the so called "backtrace" file as well. You can find the location of this backtrace file in the folder where the crash dialog indicates. Generating a log of the crash can also aid in discovering the cause. The simplest way is to start Windows Command Prompt (cmd), navigate to `C:\Program files\darktable\bin` and start darktable via `darktable.exe -d common` or `darktable -d opencl` or `darktable -d perf` or to see all the options `darktable -h`. The log file will be generated in the hidden path listed above.
        
### <a name="faq-windows-issues"></a>Known Windows issues<a href="#faq-windows-issues" class="anchor" title="Link to this FAQ entry">¶</a>
* OpenCL will speed up the processing in darktable. Sometimes Windows 11 preinstalls an OpenCL Compatibility app and it causes faults in darktable. Uninstall the OpenCL Compatibility from Windows or start darktable using `darktable --disable-opencl`.

* Windows 11 Pro security blocks installs. To resolve, go to Windows Security > App & Browsers Control > Exploit Protection Settings > Force Randomization and Set the Force Randomization for images (Mandatory ASLR) to "Off", and reboot Windows.

## <a name="faq-flatpak"></a>Flatpak<a href="#faq-flatpak" class="anchor" title="Link to this FAQ entry">¶</a>

### <a name="faq-flatpak-locations"></a>Where are the darktable files in flatpak?<a href="#faq-flatpak-locations" class="anchor" title="Link to this FAQ entry">¶</a>
The darktable files live at: `~/.var/app/org.darktable.Darktable`

### <a name="faq-flatpak-terminal"></a>How do I start darktable from terminal?<a href="#faq-flatpak-terminal" class="anchor" title="Link to this FAQ entry">¶</a>
To start darktable from terminal use: `flatpak run org.darktable.Darktable`. You can also invoke options like: `flatpak run org.darktable.Darktable -d perf`
    
## <a name="faq-mac"></a>Mac<a href="#faq-mac" class="anchor" title="Link to this FAQ entry">¶</a>
darktable is developed for Linux, but it was ported to build on Mac. If you experience problems, please check the next few known issues below specific to the Mac port. If you don't find your answer or believe that you have found a new bug, please report it through our [bug tracking](https://github.com/darktable-org/darktable/issues) system.


## Very Old Versions
These questions are probably not affecting many people these days, but we kept them for historical reasons.

### <a name="faq-old-presets"></a>My auto-applied presets aren't enabled for pictures imported before upgrade to version 1.1 (or higher), what's happening?<a href="#faq-old-presets" class="anchor" title="Link to this FAQ entry">¶</a>
This is intended. In the pre-1.1 era, modules that were enabled by default didn't get recorded in the history stack, which meant that changing these presets would retroactively change your pictures. It was decided that this is totally broken behaviour and since darktable version 1.1 auto-enabled modules for newly imported pictures are saved in history stack. However this change left all old photos without any user-defined auto-applied presets enabled. To fix this you will have to manually edit them. We suggest making a style out of preset, filtering photos to which it should apply using collect module, then selecting all in resulting collection and applying the style, repeat for every needed preset.

### <a name="faq-demosaic"></a>What happened to the demosaic module in darkroom? How can I select more demosaicing algorithms?<a href="#faq-demosaic" class="anchor" title="Link to this FAQ entry">¶</a>
We moved the demosaicing into our internal pixel pipeline. The benefit is that it is faster and more accurate. The downside is that we have to implement the demosaicing algorithms ourselves. Since the differences are really small with real world photos we didn't bother to port more than PPG and AMaZE. If anyone feels the need for more choice we will gladly accept patches.
