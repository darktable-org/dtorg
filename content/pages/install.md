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


<h2 id='ubuntu'>Ubuntu packages</h2>
![ubuntu]({filename}/images/OS/ubuntu.jpg)

Ubuntu comes with darktable packages. You can install them with

    sudo apt-get install darktable

If you need a newer version than what is included in your distribution, check out the <a href="#3rdparty">third party packages</a> section.


<h2 id='fedora'>Fedora packages</h2>
![fedora]({filename}/images/OS/fedora.jpg)

Fedora ships with darktable. A simple command should be enough.

    # dnf install darktable

If you need a newer version than what is included in your distribution, check out the <a href="#3rdparty">third party packages</a> section.

<h2 id='opensuse'>openSUSE packages</h2>
![opensuse]({filename}/images/OS/opensuse.jpg)

openSUSE ships with darktable. A simple `zypper install darktable` should be enough.

If you need a newer version than what is included in your distribution, check out the <a href="#3rdparty">third party packages</a> section.

<h2 id='arch'>Arch Linux</h2>
![arch]({filename}/images/OS/arch.jpg)

    $ pacman -S darktable

* thx to chressie for this, arch _is_ non-ancient :)

<h2 id='gentoo'>Funtoo/Gentoo Linux</h2>
![gentoo]({filename}/images/OS/gentoo.jpg)

darktable is in portage!

    # emerge darktable
    $ darktable

<h2 id='rhel'>RHEL / Scientific Linux / Centos</h2>
![scientificlinux]({filename}/images/OS/scientificlinux.jpg)

    # yum install epel-release
    # yum install darktable

<h2 id='debian'>Debian</h2>
![debian]({filename}/images/OS/debian.png)

(Of course) there is a darktable package in the Debian repositories.

darktable can be installed by running

    sudo apt-get install darktable

If you need a newer version than what is included in your distribution, check out the <a href="#3rdparty">third party packages</a> section.

<h2 id='solaris'>Solaris</h2>
![opensolaris]({filename}/images/OS/opensolaris.png)

The darktable Solaris packages are provided and maintained by James. You can find his website here with all the packages provided: <https://www.jmcpdotcom.com/blog/category/darktable/>.

He has both the [darktable packages](https://www.jmcpdotcom.com/Packages/) and a [dependency package](https://www.jmcpdotcom.com/Packages/dt-deps.p5p.gz) in case this is the first time you are installing darktable on your system.


<h2 id='freebsd'>FreeBSD</h2>
![freebsd]({filename}/images/OS/freebsd.png)

darktable is available in the FreeBSD Ports Collection. It can be installed, pre-compiled, from the standard package repository.

To install darktable on your system, run

    # pkg install graphics/darktable

<h2 id='windows'>Microsoft Windows</h2>
![Microsoft Windows]({filename}/images/OS/windows.png)

  * Read the Windows version specific section [in the FAQ]({filename}/pages/about/faq.md) first.
  * Download the [latest Windows installer for darktable](https://github.com/darktable-org/darktable/releases/download/release-3.2.1/darktable-3.2.1-win64.exe).
  * Run it and install darktable.

<h2 id='macos'>macOS</h2>
![macosx]({filename}/images/OS/macosx.jpg)

  * Download the [latest DMG disk image for darktable](https://github.com/darktable-org/darktable/releases/download/release-3.2.1/darktable-3.2.1.dmg)
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

### macOS Homebrew

darktable can be installed through Homebrew:

    brew cask install darktable


<h1 id="3rdparty">third party packages and PPAs</h1>

## OBS

The [OBS](https://build.opensuse.org/) allows packagers to provide packages for multiple distributions.

Right now the darktable packages listed below are built for the following Linux distributions:

Right now this means for the stable package:

* Debian 9, 10, Next aka Testing
* Fedora  29, 30, 31, Rawhide
* openSUSE 15.0, 15.1, Tumbleweed
* Ubuntu 18.04, 19.04, 19.10, 20.04 (only latest release, not snapshot from stable release branch)

For master we build for the following distributions because of missing required packages in older distributions:

* Debian 9, 10, Next aka Testing
* Fedora   29, 30, 31, Rawhide
* openSUSE 15.0, 15.1, Tumbleweed
* Ubuntu 18.04, 19.04, 19.10, 20.04

The available packages are:

* [latest release](https://software.opensuse.org/download.html?project=graphics:darktable&package=darktable)
* [snapshots from the stable release branch](https://software.opensuse.org/download.html?project=graphics:darktable:stable&package=darktable)
* [snapshots from the master branch](https://software.opensuse.org/download.html?project=graphics:darktable:master&package=darktable)


## Backports for Debian

A description on how to enable the backports repository can be found here: <https://backports.debian.org/Instructions/>

<h1 id="source">Install from source</h1>

## Prerequisites
![bee]({attach}bee.jpg)

  * *nix (tested: Debian, Ubuntu, Arch Linux, Funtoo, Gentoo, Fedora, Macintosh OS X with Macports)
  * We strongly recommend using a **64bit operating system**!
  * Required packages: `libsqlite3, libjpeg, libpng, libpugixml, rawspeed (supplied), gtk+-3, cairo, lcms2, exiv2, tiff, curl, gphoto2, dbus-glib, fop, openexr, libsoup2.4`
  * Required: gcc >= 5.0


# Current release from source
![leaves1]({filename}/images/OS/leaves1.jpg)

* Grab the [latest source tarball](https://github.com/darktable-org/darktable/releases/tag/release-3.2.1) (recent version: darktable 3.2.1)&nbsp;– make sure to use the .tar.xz file and not the auto generated .zip or .tar.gz!
* Install the dependencies. For details see the link below.
* Unpack:

        $ tar xvf darktable-3.2.1.tar.xz && cd darktable-3.2.1

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
