---
Title: install
Date: 2017-09-20T16:48:38-06:00
author: smn
wordpress_id: 118
lede: lede-install.jpg
lede_author: <a href="https://jo.dreggn.org/home/">jo</a>
weight: 400
menu: ["main", "footer"]
---

<div style="display:flex;flex-direction: row;justify-content:space-evenly;">
<div style="text-align: center;">
  <h2>Source Code</h2>
  <p>
  <a href="https://github.com/darktable-org/darktable/releases/download/release-3.6.0/darktable-3.6.0.tar.xz">darktable-3.6.0.tar.xz</a>
  </p>
</div>
<div style="text-align: center;">
  <h2>Windows</h2>
  <p><a href='https://github.com/darktable-org/darktable/releases/download/release-3.6.0/darktable-3.6.0.1-win64.exe' title='Microsoft Windows'>darktable-3.6.0.1-win64.exe</a></p>
</div>
<div style="text-align: center;">
  <h2>macOS</h2>
  <p><a href='https://github.com/darktable-org/darktable/releases/download/release-3.6.0/darktable-3.6.0.3.dmg' title='macOS'>darktable-3.6.0.3.dmg</a></p>
  <p><a href="#macos">installation notes</a></p>
</div>
</div>

<h1 id="linux">Linux/Unix Binary Packages</h1>

## From Your Package Manager

If your unix-like operating system is capable of running a graphical session, darktable is likely available. Check your package manager or software center.

## OBS

The [OBS](https://build.opensuse.org/) allows packagers to provide packages for multiple Linux distributions.

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

## Universal Package Formats

* [flatpak](https://www.flathub.org/apps/details/org.darktable.Darktable)

<h2 id='macos'>macOS</h2>

This bundle supports macOS versions starting with 10.7 (Lion) running on 64 bit Intel architecture.

What to do with dialog saying *"darktable" can't be opened because it was not downloaded from the Mac App Store*:

  * Locate darktable in Applications folder (or wherever you installed it) using Finder
  * Do "Open" via context menu
  * You will be presented with similar-looking dialog, but this time there will be second button allowing you to run the application
  * After that you will be able to start darktable without this trick (well, until you update it, then you will have to do above steps again)

or you can prevent this from happening by running `xattr -d com.apple.quarantine ~/Downloads/darktable*.dmg` command before mounting the image (or `xattr -dr com.apple.quarantine /Applications/darktable.app` after installing).

### macOS Package Managers

MacPorts:

    sudo port install darktable +quartz

Homebrew:

    brew install --cask darktable
