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
  <a href="https://github.com/darktable-org/darktable/releases/download/release-4.8.0/darktable-4.8.0.tar.xz">darktable-4.8.0.tar.xz</a>
  </p>
</div>
<div style="text-align: center;">
  <h2>AppImage</h2>
  <p><a href='https://github.com/darktable-org/darktable/releases/download/release-4.8.0/darktable-4.8.0-x86_64.AppImage' title='GNU/Linux AppImage'>darktable-4.8.0-x86_64.AppImage</a></p>
</div>
<div style="text-align: center;">
  <h2>Windows</h2>
  <p><a href='https://github.com/darktable-org/darktable/releases/download/release-4.8.0/darktable-4.8.0-win64.exe' title='Microsoft Windows'>darktable-4.8.0-win64.exe</a></p>
</div>
<div style="text-align: center;">
  <h2>macOS</h2>
  <p><a href='https://github.com/darktable-org/darktable/releases/download/release-4.8.0/darktable-4.8.0-x86_64.dmg' title='macOS 13.5 on Intel'>darktable-4.8.0-x86_64.dmg</a></p>
  <p><a href='https://github.com/darktable-org/darktable/releases/download/release-4.8.0/darktable-4.8.0-arm64.dmg' title='macOS 14.0 on Apple silicon'>darktable-4.8.0-arm64.dmg</a></p>
  <p><a href='https://github.com/darktable-org/darktable/releases/download/release-4.8.0/darktable-4.8.0-arm64-macOS-13.5.dmg' title='macOS 13.5 on Apple silicon'>darktable-4.8.0-arm64-macOS-12.5.dmg</a></p>
  <p><a href="#macos" class="attention">installation notes</a></p>
</div>
</div>

Some commonly asked questions can be found in our [FAQ](/about/faq). Please read it before reporting bugs or feature requests.

<h1 id="linux">Linux/Unix Binary Packages</h1>

## From Your Package Manager

If your unix-like operating system is capable of running a graphical session, darktable is likely available. Check your package manager or software center.

## OBS (Open Build Service)

The [OBS](https://build.opensuse.org/) allows packagers to provide packages for multiple Linux distributions.

[Latest darktable release](https://software.opensuse.org/download.html?project=graphics:darktable&package=darktable) is built for the following distribution releases:

* Debian Testing
* Fedora 36, 37, Rawhide
* openSUSE Tumbleweed
* Ubuntu 23.04

[Master git branch](https://software.opensuse.org/download.html?project=graphics:darktable:master&package=darktable) is built for:

* Debian Testing
* Fedora 36, 37, Rawhide
* openSUSE Tumbleweed
* Ubuntu 22.10, 23.04

## Universal Package Formats

* [flatpak](https://www.flathub.org/apps/details/org.darktable.Darktable)

<h2 id='macos'>macOS</h2>

These bundles support macOS versions starting with 12.5 (Monterey).

### Fixing issues with macOS security settings

Depending on the version of macOS, there maybe some warnings causing darktable not to run.

#### Dialog: *"darktable" can't be opened because it was not downloaded from the Mac App Store*

Do one of the follow:

1. Locate darktable in Applications folder (or wherever you installed it) using Finder
2. Do "Open" via context menu
3. You will be presented with similar-looking dialog, but this time there will be second button allowing you to run the application
4. After that you will be able to start darktable without this trick (well, until you update it, then you will have to do above steps again)

or

1. Open the Terminal app.
2. Do one of the following:
  * If the image is not mounted, run `xattr -d com.apple.quarantine ~/Downloads/darktable*.dmg`
  * If darktable is already installed, run `xattr -dr com.apple.quarantine /Applications/darktable.app`

#### Dialog: *"darktable.app" is damaged*

1. Open the Terminal app.
2. Do one of the following:
  * If the image is not mounted, run `xattr -d com.apple.quarantine ~/Downloads/darktable*.dmg`
  * If darktable is already installed, run `xattr -dr com.apple.quarantine /Applications/darktable.app`

### macOS Package Managers

MacPorts:

    sudo port install darktable +quartz

Homebrew:

    brew install --cask darktable
