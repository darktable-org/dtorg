author: bieber
comments: true
date: 2011-06-25 21:15:19+00:00
layout: post
link: http://www.darktable.org/2011/06/darktable%e2%80%99s-new-keyboard-shortcut-system/
slug: darktable%e2%80%99s-new-keyboard-shortcut-system
title: Darktable’s New Keyboard Shortcut System
wordpress_id: 420
tags: GSoC

It took longer than I expected thanks to some unforeseen twists and turns, but the new keyboard accelerator system is basically finished.  There may still be some need for minor bug fixes and string changes (in particular, the new translation system needs to be tested out), but by and large everything that needs to be in place is, and next week I plan to start working on changes to the color picker module.  Now that the accelerator interface is stable, lets take a little tour of it.

![](http://www.darktable.org/wp-content/uploads/2011/09/Screenshot-darktable-preferences-300x163.png)

If you enter the preferences dialog now, you’ll see a new tab on the right hand side.  This tab has a tree view which displays every keyboard accelerator registered in the system, organized into groups that you can expand and contract.  Double-clicking on an entry will allow you to remap it, and pressing backspace will clear a keyboard accelerator.  You can use the buttons below the tree-view to export your shortcut bindings to a file, import another set of shortcut bindings from a file, or reset everything to the default values.

As you remap keys, the system will also automatically delete any conflicting keybindings.  The rules for this are somewhat nuanced, as a shortcut may be usable throughout the entire program, or only in one of the views (darkroom, lighttable, capture, and filmstrip).  Global shortcuts, obviously, will conflict with shortcuts in any other group.  Lighttable shortcuts, however, will only conflict with other lighttable shortcuts (other than globals).  Darkroom and capture shortcuts will conflict with shortcuts from their own group or shortcuts from the filmstrip, because the filmstrip can appear in either of those views.

Basically, you can map the same key to multiple shortcuts as long as there’s no way they could feasibly activate at the same time.  This means that you’re more than welcome to set a key to mean one thing in lighttable mode and another in darkroom mode.  You can also map shortcuts to keys without any modifiers (for instance, just the ‘l’ key to switch to lighttable mode), as Darktable deactivates keyboard shortcuts whenever focus is on a text entry widget.

Another helpful feature (at the suggestion of boucman on IRC) is that every darkroom module has a “show” accelerator in the dialog box, which is empty by default.  You can define these shortcuts for modules which you use frequently.  When activated,  they will show the module in question and bring it to focus.

The accelerator interface should also translate the accelerator names, once the strings have been translated.  I’ve added a script to the build process which splits all of the accelerator paths up into their component parts and gets them recognized by intl-tool for translation, so if you build my branch and then generate a .pot file, the new accelerator strings should be there.  I’d appreciate confirmation from any translators who can get this to work successfully.

