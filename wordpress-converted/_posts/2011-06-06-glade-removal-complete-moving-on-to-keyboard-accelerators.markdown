---
author: bieber
comments: true
date: 2011-06-06 21:33:37+00:00
layout: post
link: http://www.darktable.org/2011/06/glade-removal-complete-moving-on-to-keyboard-accelerators/
slug: glade-removal-complete-moving-on-to-keyboard-accelerators
title: Glade Removal Complete, Moving on to Keyboard Accelerators
wordpress_id: 444
categories:
- GSoC
---



As of last week, the removal of libglade from Darktable is functionally complete.  The gladefile has been deleted, along with all references to libglade in the code and the Cmake files.  Some refactoring may still be ideal, and I’ll be rearranging some code in my free time, but the task is basically completed.  Now it’s time to move on to handling keyboard shortcuts.

My plan is to make all keyboard accelerators in Darktable application-wide, so that the user won’t have to worry about the current focus when entering a shortcut.  There will be mode-specific shortcuts, but nothing module specific.  Instead of entering the specific key to use for the shortcut, code registering shortcuts will now instead make an entry in a table with a name for the shortcut and a default key to use, which may be remapped by the user.  Remapping will be handled in a tab of the preferences dialog, in similar fashion to the keyboard shortcuts dialog in GIMP.

To actually accomplish this task, I’ve been pleased to discover that GTK+ has two classes, [GtkAccelGroup](http://developer.gnome.org/gtk/2.24/gtk-Keyboard-Accelerators.html) and [GtkAccelMap](http://developer.gnome.org/gtk/2.24/gtk-Accelerator-Maps.html), which support the notion of an accelerator mapping table that I’ve been planning to implement.  The GtkAccelGroup connects accelerator paths (which may look like, for instance, “<Darktable>/lt/setrating1″) to callback functions, and they can be attached to a window to activate the accelerators in the group.  The global GtkAccelMap, meanwhile, maps the accelerator paths to actual keypresses, and it can be saved, loaded, and modified at runtime to change the keyboard accelerators.  In the context of Darktable, we’ll have four accelerator groups: global, lighttable, darkroom, and capture.  The view-specific groups will be detached/attached to the main window depending on the currently active view, while the global group will remain attached whenever the application is running.  The new tab in the preferences dialog will then allow the user to remap the keys in the global GtkAccelMap.

These classes seem to be exactly what I’m looking for, although the documentation on them is a little bit sparse.  To get a good feel for them I’ll spend the next day or so experimenting with them in a tiny project to make sure I understand just what I’m doing, and then I can move on to implementing the new shortcut system in Darktable.  I’ll probably start by replacing Darktable’s existing keyboard shortcut registration system with one that uses the GtkAccelGroup method, and then from there I can move on to creating the user interface to allow user remapping of the shortcuts.


