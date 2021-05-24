---
author: houz
comments: true
date: 2011-07-17 21:56:43+00:00
layout: post
link: /2011/07/that-other-os/
slug: that-other-os
title: "That other OS"
lede: windoos.jpg
wordpress_id: 321
tags:
  - development
---
The last time I posted to this blog it was my April Fool’s Joke about a file manager (which happened to be just an embedded shell). Since a few people didn’t like that at all I want to assure you that this is no joke at all. However, if you are a Windows user and feel easily offended, then stop reading now.

Still here? Great. I managed to compile darktable for Windows.

It took me about two days of hacking to have our code in a shape which is eaten by mingw (I cross-compiled under Debian). That was the easy part.

The hard part is the question “Shall I commit it to git?”. Code wise it’s only a really small change, but the implications might be huge. I remember when GIMP was suddenly available for Windows (yes, I’m that old). At first it was unstable. Then it matured. And now, well, let me phrase it this way: I strongly believe that porting GIMP to windows was the biggest mistake these guys ever made. Followed by no longer adding an alpha channel to new layers. Maintaining a code base which none of the developers can run, test or debug is a nightmare. Even more if the users have not the slightest clue what’s going on. With Linux users you can give the advice to run gdb and generate a backtrace. Some might not know what you are talking about, yet it’s not too hard to give simple instructions. Have fun doing that with a Windows user. They are a bunch of consumers which only take what you give them. And since they know that, they are really good in demanding everything while giving back nothing. That’s an attitude I don’t like. Don’t believe me? Go looking at support forums for GIMP. It’s hell.

The next problem with Windows is the lack of package managers. While Linux has tons of different flavours, nowadays most of them come with a working package management. That makes it easy to distribute a program and keep it up to date. Well, Windows recently introduced some means of online updates for third party software, but that’s beyond our scope. So in the end we would need to have our own installer, bundle all the needed libraries, maybe add some automated checking for new versions, you name it.

Then, what are the benefits from adding Windows to the pool of supported platforms you might ask? The standard answer always given is “you get so many new users”. Well, yeah. So what? Do they pay me? No. Do they support me coding the program? Hardly. Do they promote our software? Yes, to other Windows users which generate noise, too. Sorry, a valid argument looks different.

At the end of the day it all boils down to the question whether we want to follow the route GIMP and other open source software went. While I don’t think we should take the burden of providing installers or even binaries, I guess adding support for compilation doesn’t hurt too much. After all darktable also builds on Macs. And don’t get me started on Mac users. ;-)

Discuss.
