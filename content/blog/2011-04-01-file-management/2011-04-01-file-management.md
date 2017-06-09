author: houz
comments: true
date: 2011-04-01 22:06:55+00:00
layout: post
link: http://www.darktable.org/2011/04/file-management/
slug: file-management
title: File management
wordpress_id: 453
tags: development

Whoever has followed the mailing lists or IRC has seen remarks that darktable lacks a feature complete file manager. Currently we only have a button which lets the user delete files from disk, but there is no way to move them, copy them, rename them, … Every time someone has shown up to suggest something beyond that we made clear that “darktable is not a file manager”. We even have a [FAQ entry](https://sourceforge.net/apps/trac/darktable/wiki/FAQ) about that.

Recently I had to edit a few older photos which happened to be on an external disk so I had to copy them to my laptop and suddenly I knew why people want to have some file management capabilities inside of their DAM software. So I decided that it was time to change the way we always reacted. First of all I had a look at other programs to see what a good interface for the task would be and if there are ready available building blocks for use inside of a GTK+ application (after all that’s the power of open source software to not reinvent the wheel all the time).

To cut a long story short, darktable now has a file manager. In lighttable mode it’s located in the right panel and offers all the power you are used to in a convenient interface which was “borrowed” from the proven classics – you can rename, copy and move files, even links are possible (if the file system supports it). Working with directories is possible, too. The same holds for simple browsing of the file system. And for those which need it there is even a little help system included.

To test this you have to build from git and have libvte-dev installed. Pascal’s PPA doesn’t have it yet as the Ubuntu build farm has a different version of that library and currently fails to build. We’ll fix that a.s.a.p.

**Update:** This is supposed to be fixed so it should compile with libvte >= 0.26, too.

**Update 2:** Of course this was an April Fool’s Joke. The so-called “file manager” was nothing but a shell and the “documentation” a tool tip mentioning a few commands like cp, ls, mv, …

![](http://www.darktable.org/wp-content/uploads/2011/09/april_fools_file_manager.png)
