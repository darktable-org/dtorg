Title: install
Date: 2017-09-20T16:48:38-06:00
author: smn
wordpress_id: 118
lede: lede-install.jpg
lede_author: <a href="https://jo.dreggn.org/home/">jo</a>

# Choose your OS:

<p class="chooseos">
<a href='#ubuntu' title='Ubuntu'><img class='chooseos' alt="ubuntu" src="{filename}/images/OS/ubuntu.jpg"></a>
<a href='#fedora' alt='Fedora'><img class='chooseos' alt="fedora" src="{filename}/images/OS/fedora.jpg"></a>
<a href='#opensuse' title='openSUSE'><img class='chooseos' alt="opensuse" src="{filename}/images/OS/opensuse.jpg"></a>
<a href='#arch' title='Arch'><img class='chooseos' alt="arch" src="{filename}/images/OS/arch.jpg"></a>
<a href='#gentoo' title='Funtoo/Gentoo'><img class='chooseos' alt="gentoo" src="{filename}/images/OS/gentoo.jpg"></a>
<a href='#rhel' title='RHEL 6 / SL 6 / CentOS 6'><img class='chooseos' alt="macosx" src="{filename}/images/OS/scientificlinux.jpg"></a>
<a href='#macos' title='macOS'><img class='chooseos' alt="macosx" src="{filename}/images/OS/macosx.jpg"></a>
<a href='#debian' title='Debian'><img class='chooseos' alt="debian" src="{filename}/images/OS/debian.png"></a>
<a href='#solaris' title='Solaris'><img class='chooseos' alt="opensolaris" src="{filename}/images/OS/opensolaris.png"></a>
<a href='#freebsd' title='FreeBSD'><img class='chooseos' alt="freebsd" src="{filename}/images/OS/freebsd.png"></a>
<a href='#windows' title='Microsoft Windows'><img class='chooseos' alt="windows" src="{filename}/images/OS/windows.png"></a>
</p>

<style>
p.chooseos {
    text-align: center;
}
img.chooseos {
    margin-right: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0px 5px 10px -3px #666;
}
</style>


...&nbsp;or get the latest stable source package and build it yourself, look what to do if you are running OSX or Windows or get the hot new stuff from our git repository.


# Prerequisites
![bee]({attach}bee.jpg)

  * *nix (tested: Debian, Ubuntu, Arch Linux, Funtoo, Gentoo, Fedora, Macintosh OS X with Macports)
  * We strongly recommend using a **64bit operating system**!
  * Required packages: `libsqlite3, libjpeg, libpng, libpugixml, rawspeed (supplied), gtk+-3, cairo, lcms2, exiv2, tiff, curl, gphoto2, dbus-glib, fop, openexr, libsoup2.4`
  * Optional: gcc >= 4.6


<h2 id='ubuntu'>Ubuntu packages</h2>
![ubuntu]({filename}/images/OS/ubuntu.jpg)

We provide several PPAs to add to your Ubuntu installation:

  * For stable releases add the [Darktable Release PPA](https://launchpad.net/~pmjdebruijn/+archive/darktable-release).
  * If you are adventurous and are willing to deal with problems from time to time add the [Darktable Unstable PPA](https://launchpad.net/~pmjdebruijn/+archive/darktable-unstable). Don't use this PPA if you do time critical work with darktable!
  * Follow the instructions on the Launchpad PPA page.
  * Then search for "darktable" in the Software Center of Synaptic Package Manager and install it.
  * You will find it under "Applications/Graphics/Darktable Photography Workflow Software"

If you want to have nice packages on debian you can rebuild the PPA sources for debian: Download `darktable_$VERSION.orig.tar.gz` and `darktable_$VERSION.debian.tar.gz` from one of the PPAs.

    $ sudo apt-get install debhelper dpkg-dev fakeroot
    $ sudo apt-get build-dep darktable
    $ tar zxvf darktable_$VERSION.orig.tar.gz
    $ cd darktable-$VERSION
    $ tar zxvf ../darktable_$VERSION.debian.tar.gz
    $ dpkg-buildpackage -rfakeroot


<h2 id='fedora'>Fedora packages</h2>
![fedora]({filename}/images/OS/fedora.jpg)

Fedora ships with darktable. A simple command should be enough.

    # dnf install darktable

* If you are adventurous and are willing to deal with problems from time to time add the [Darktable 2.2 Snapshot repository](https://software.opensuse.org/download.html?project=home%3Adarix%3Adarktable%3Astable-2.2&package=darktable). Don't use this repository if you do time critical work with darktable!
* And lastly, there is is a repository for [nightly builds](https://software.opensuse.org/download.html?project=home%3Adarix%3Adarktable%3Amaster&package=darktable). Don't use this repository unless you understand what git master means!

If you want to build darktable from the source on Fedora, here are the build dependencies:

    # dnf install intltool atk-devel cairo-devel exiv2-devel fontconfig-devel freetype-devel libgomp gtk2-devel libjpeg-turbo-devel libtiff-devel lcms2-devel lensfun-devel libpng-devel libsq3-devel libstdc++-devel libxml2-devel OpenEXR-devel libcurl-devel libgphoto2-devel dbus-glib-devel libgnome-keyring-devel fop librsvg2-devel flickcurl-devel cmake libsoup-devel gcc-c++ colord-devel saxon libsecret-devel lua lua-devel GraphicsMagick openjpeg-devel json-glib-devel libwebp-devel SDL-devel


<h2 id='opensuse'>openSUSE packages</h2>
![opensuse]({filename}/images/OS/opensuse.jpg)

openSUSE ships with darktable. A simple `zypper install darktable` should be enough.

* If you want the latest stable version you can use [darktable from the Graphics Repository](https://software.opensuse.org/download.html?project=graphics&package=darktable).
* If you are adventurous and are willing to deal with problems from time to time add the [Darktable 2.0 Snapshot repository](https://software.opensuse.org/download.html?project=home%3Adarix%3Adarktable%3Astable-2.2&package=darktable). Don't use this repository if you do time critical work with darktable!
* And lastly, there is is a repository for [nightly builds](https://software.opensuse.org/download.html?project=home%3Adarix%3Adarktable%3Amaster&package=darktable). Don't use this repository unless you understand what git master means!


<h2 id='arch'>Arch Linux</h2>
![arch]({filename}/images/OS/arch.jpg)

    $ pacman -S darktable

* thx to chressie for this, arch _is_ non-ancient :)

<h2 id='gentoo'>Funtoo/Gentoo Linux</h2>
![gentoo]({filename}/images/OS/gentoo.jpg)

darktable is in portage!

    # emerge darktable
    $ darktable

<h2 id='rhel'>RHEL 6 / SL 6 / Centos 6</h2>
![scientificlinux]({filename}/images/OS/scientificlinux.jpg)

Only darktable-1.0.5 can be provided for these distributions due to restrictions on the Glib version available. Still, try it out, 1.0 has many nice features already and most of the hardware support has been ported back by Pascal&nbsp;– that's where the .5 comes from.

  * install the linuxtech.repo config file if you don't have it already:

        su - root
        cd /etc/yum.repos.d/
        wget http://pkgrepo.linuxtech.net/el6/release/linuxtech.repo

  * install darktable:

        yum --enablerepo=linuxtech-testing install darktable


<h2 id='macos'>macOS</h2>
![macosx]({filename}/images/OS/macosx.jpg)

  * Download the [latest DMG disk image for darktable](https://github.com/darktable-org/darktable/releases/download/release-2.2.5/darktable-2.2.5.dmg)
  * Mount the thing
  * Pull the darktable icon into applications folder
  * Good luck :)

This bundle supports macOS versions starting with 10.7 (Lion) running on 64 bit Intel architecture.

What to do with dialog saying *"darktable" can't be opened because it was not downloaded from the Mac App Store*:

  * Locate darktable in Applications folder (or wherever you installed it) using Finder
  * Do "Open" via context menu
  * You will be presented with similar-looking dialog, but this time there will be second button allowing you to run the application
  * After that you will be able to start darktable without this trick (well, until you update it, then you will have to do above steps again)

or you can prevent this from happening by running `xattr -d com.apple.quarantine ~/Downloads/darktable*.dmg` command before mounting the image (or `xattr -dr com.apple.quarantine /Applications/darktable.app` after installing).

### macOS MacPorts

darktable can be installed through MacPorts:

    sudo port install darktable +quartz


<h2 id='debian'>Debian</h2>
![debian]({filename}/images/OS/debian.png)

(Of course) there is a darktable package in the Debian repositories. The current stable version _Stretch_ still has darktable 2.2.1 packaged, but version 2.2.5 is available through the backports. This is also what already landed in _Buster_. See package description here: <https://packages.debian.org/stable/darktable>.

darktable can be installed just by running

    sudo apt-get install darktable

A description on how to enable the backports repository can be found here: <https://backports.debian.org/Instructions/>


<h2 id='solaris'>Solaris</h2>
![opensolaris]({filename}/images/OS/opensolaris.png)

The darktable Solaris packages are provided and maintained by James. You can find his website here with all the packages provided: <https://www.jmcpdotcom.com/blog/category/darktable/>.
He has both the [darktable packages](https://www.jmcpdotcom.com/Packages/) and a [dependency package](https://www.jmcpdotcom.com/Packages/dt-deps.p5p.gz) in case this is the first time you are installing darktable on your system.


<h2 id='freebsd'>FreeBSD</h2>
![freebsd]({filename}/images/OS/freebsd.png)

darktable is packaged and compiled for FreeBSD, the binary package can be found here:
<https://ftp.freebsd.org/pub/FreeBSD/ports/packages/graphics/>.

To install darktable on your system, run

    # pkg_add -r darktable

and have fun.

<h2 id='windows'>Microsoft Windows</h2>
![Microsoft Windows]({filename}/images/OS/windows.png)

  * Download the [latest Windows installer for darktable](https://github.com/darktable-org/darktable/releases/download/release-2.4.0/darktable-2.4.0-win64.exe).
  * Run it and install darktable.
  * Read the Windows version specific section [in the FAQ]({filename}/pages/about/faq.md) first.
  * Read [this blog post]({filename}/news/2017-08-30-darktable-for-windows/2017-08-30-darktable-for-windows.md) to learn about the currrent state of the Windows port.


# Current release from source
![leaves1]({filename}/images/OS/leaves1.jpg)

* Grab the [latest source tarball](https://github.com/darktable-org/darktable/releases/tag/release-2.4.0) (recent version: darktable 2.4.0)&nbsp;– make sure to use the .tar.xz file and not the auto generated .zip or .tar.gz!
* Install the dependencies. For details see the link below.
* Unpack:

        $ tar xvf darktable-2.4.0.tar.xz && cd darktable-2.4.0

* Then either do

        $ ./build.sh

* or, manually:

        $ mkdir build && cd build/
        $ cmake -DCMAKE_BUILD_TYPE=Release ..
        $ make -j5
        # make install
        $ darktable

  * In order to get darktable displayed along with your other applications you need to set a symlink:

        $ ln -s /opt/darktable/share/applications/darktable.desktop /usr/share/applications/darktable.desktop

For a more complete set of instructions for different distributions have a look at [our Wiki](https://redmine.darktable.org/projects/darktable/wiki/Building_darktable_22).

# git version
![fire]({filename}/images/OS/fire.jpg)

_First a word of warning_: Using the development version of darktable might be risky in that it can break anytime, kill your edits, eat your kittens or do other nasty things. It is also not guaranteed that XMP sidecars written by a development version will work with a release version. It is also quite certain that any older version of darktable will **NOT** be able to read the database once a development build updated it to the latest schema. So for your own safety and our sanity, do make backups of your XMP files as well as your `library.db` and `data.db` (by default it is in `~/.config/darktable/`) **BEFORE** upgrading to the self compiled git version. That being said, it should be quite safe to actually use it and never go back, so all of this might be no issue for you at all. Just keep in mind that **IF** you ever want to go back it might be hard.

Be sure to have all the build dependencies installed. You can find a list of them here. If you don't have it already, install git from your distribution's repositories. For Ubuntu:

    $ sudo apt-get install git

### Cloning for the first time

    $ cd
    $ git clone git://github.com/darktable-org/darktable.git

The cloned files from the git repository are now stored in $HOME/darktable.

### Getting rawspeed submodule

    $ cd $HOME/darktable
    $ git submodule init
    $ git submodule update

### Building with build.sh

    $ ./build.sh

The files get prepared to be installed in /opt. If you want to install at another place, you have to type:

    ./build.sh --prefix /path/to/install


After the build process finished you can install darktable:

    cd build && sudo make install

### Updating existing git-files

    $ cd $HOME/darktable
    $ git pull

### Building manually

    $ mkdir $HOME/darktable/build
    $ cd $HOME/darktable/build
    $ cmake -DCMAKE_BUILD_TYPE=Release ..

### make and install

    $ cd $HOME/darktable/build
    $ make
    $ sudo make install

### Starting the program

    $ darktable

Let's rock!
