---
author: houz
comments: true
date: 2015-03-31 23:30:28+00:00
layout: post
link: http://www.darktable.org/2015/04/introducing-the-darktable-app-store/
slug: introducing-the-darktable-app-store
title: Introducing the darktable app store
wordpress_id: 3630
categories:
- announcement
- blog
- development
- news
- upcoming feature
---

Today we are happy to announce a big new feature that we will not only ship with the big 2.0 release later this year but also with our next point release, 1.6.4, which is due in about a week: even more darkroom modules!

One of the big strengths of darktable has always been its varied selection of modules to tweak your image. However, that has also been one of the main points of criticism: too much, too many and too complicated to grasp. To make it easier for the user to deal with the flood of tools darktable has had the “[more modules](http://www.darktable.org/usermanual/ch03s03s08.html.php)” list since many years. It changed its appearance a few times, we added module categories, allowed to select favorite modules, and all of that has proven to be useful. Thus there have always been people that approached us with great new ideas for new modules, especially since we moved to [GitHub](https://github.com/darktable-org/darktable) a while ago with its powerful Pull Request system, yet we couldn't accept many of them. Some were not that great codewise, some didn't really fit our product vision – and then there were some that looked nice and certainly benefited some users, but we felt it wasn't generic enough to justify polluting our module list even more. Of course this was a bad situation, after all these people invested quite some time into providing us with a new feature that we turned down. No one likes to waste their time.

[caption id="attachment_3631" align="alignright" width="309"][![In the default state the new dialog doesn't clutter the gui](https://www.darktable.org/wp-content/uploads/2015/03/screenshot01.png)](https://www.darktable.org/wp-content/uploads/2015/03/screenshot01.png) In the default state the new dialog doesn't clutter the gui[/caption]

After initial discussions about this topic at last year's [LGM in Leipzig](http://libregraphicsmeeting.org/2014/) we started working on a solution later that year and now we feel confident to present you the new module store. Think of it as an in-game app store (for all you gamers out there), or Firefox' Add-On system. Instead of bloating the list of modules shipped with darktable you can now easily browse for exciting new features from within the darkroom GUI, installing new modules on the fly (or uninstall them if you don't like the result), and even see previews of the module's effect on the currently opened image. We are certain that you will like this.

Who will also like it are module developers. Writing new image modules has always been quite easy: clone the darktable sources, create one new C file and add it to the CMake system. But that was only the first part, after all you wanted to allow people to use your work in the end. So you either had to convince us to include your module into the official darktable release (with the problems outlined above), or provide a patched version of darktable for people to compile themselves. In theory you could also have provided a binary package or just the module compiled into a shared library for people to just copy to their install directory, but we have never seen anyone taking that route. With our new module system this will become easier. Instead of creating a patched version of darktable you can now make use of our Module Developers Package which contains all the required header files and a CMake stub to quickly compile your module into a shared library that can be used with a stock installation of darktable. And since we will release these files under a LGPL license you could even write non-free modules. Once you are happy you can submit your code for us to review (this step is still manual to prevent malicious code being shipped) and once we approved it everyone can install the module.

[caption id="attachment_3632" align="alignleft" width="309"][![Currently there is just the one module in store. More to come!](https://www.darktable.org/wp-content/uploads/2015/03/screenshot02.png)](https://www.darktable.org/wp-content/uploads/2015/03/screenshot02.png) Currently there is just the one module in store. More to come![/caption]

All of the things described until now are implemented already and will be part of the next releases. Once it has proven to be working reliably we also plan to allow developers to make some money with their work as an incentive to attract more and better developers to our community. We are currently evaluating what payment models would work best, at the moment PayPal looks like a strong contender, but we are open for suggestions.

In case you are curious how it's implemented, it is based on the [GHNS](http://ghns.freedesktop.org/) system that is already used by [KDE](http://kde-look.org/) and others, and might eventually also be merged with the styles you can find on [http://dtstyle.net/](http://dtstyle.net/). On the server side there is a continuous integration system ([Jenkins](http://jenkins-ci.org/) in our case) that recompiles everything whenever something got changed, taking care of the different target architectures and operating systems with their dependencies. And if you don't want to wait for the release just try a development build, the code is merged and ready to be tested. As a first example we moved the new “[color reconstruction](http://www.darktable.org/2015/03/color-reconstruction/)” module from the regular darktable installation to the store.

PS: Thou shalt not believe what got posted on the Internet on April 1st.
