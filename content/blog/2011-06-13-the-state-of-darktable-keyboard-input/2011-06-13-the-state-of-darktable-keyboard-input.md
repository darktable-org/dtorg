author: bieber
comments: true
date: 2011-06-13 21:32:50+00:00
layout: post
link: http://www.darktable.org/2011/06/the-state-of-darktable-keyboard-input/
slug: the-state-of-darktable-keyboard-input
title: The State of darktable Keyboard Input
wordpress_id: 442
tags: GSoC



I’m about a week in on my work on darktable’s keyboard input system, and I’m hoping by the end of this week to be more or less done.  Here’s a quick look at where I am and where I’m going.

**The Current Status**

If you check out my git branch (it’s called bieber), you’ll find that so far I’ve removed all of the explicit calls to darktable’s old accelerator registration system, and replaced them with calls to gtk_accel_map_add_entry and gtk_accel_group_connect_by_path.  These functions create an entry in a global accelerator table, linking an accelerator to a path that looks something like, for instance, <Darktable>/iops/clipping/commit, rather than a specific keycode.  Other GTK function calls will later give us the ability to change the actual key mappings for these paths at runtime, so user remapping will be a breeze.  If you compile and run darktable from my branch at the moment, you’ll see a file called “testkeys” pop up in your current working directory.  This is what the GTK keybindings file looks like, at this point just auto-generated from the default key mappings specified in the source code.  Soon you’ll be able to modify this file (either directly or from an interface within Dartable’s preferences) to change your shortcut key mappings.

There are also several shortcuts throughout darktable defined by manually searching for keycodes within the key_pressed functions of different views and modules.  Some of these were easy to transition to explicit accelerators using the GTK function calls, but others are a little more sophisticated, relying on key press and key release to enter and leave some state.  For instance, the full-screen preview in the lighttable view enters when you press the ‘z’ key, and remains there as long as you hold the key down.  These shortcuts will have to remain in the key_pressed methods, but I do have a plan to make them remappable.  In the meantime, while I haven’t gotten around to adding them to the accelerator table just yet, I have gotten as far as removing them from modules and making sure that the remaining key_pressed functions operate on GTK keyvals rather than hardware keycodes, so they’ll be compatible with the accelerator map.

**Where I’m Going**

This week, I’m going to try to finish what I started last week.  Starting tonight I’ll be working on getting the key_pressed style shortcuts into the accelerator map.  While they won’t actually be using callback methods to do their work, I will make sure to query the accelerator table for the appropriate key values to use rather than just hard-coding them, as it stands now.  I will connect their accelerator paths to dummy callbacks, just because GTK will refuse to map two currently active accelerators to the same key combination, so this will keep us from running into any issues with duplicate accelerators.  I could probably get away with looking up the key values every time the key_pressed function gets executed, but for efficiency’s sake I plan to cache their values in the darktable.gui struct, and attach a callback to the global accelerator map’s “changed” signal to update them if/when they get remapped.

After that, I’ll rip out the old accelerator system, which manually compared key values on keypress to a list of registered accelerators.  I will also need to update the old accelerator blocking code, which previously just set a flag.  Now it will need to remove any attached accelerator group when a text input field receives focus, to ensure that no accelerators get activated while the user is trying to enter text.

With that groundwork laid, I’ll be ready to build the GUI for actually remapping the keys.  I plan to display them all in a treeview on a new panel of the preferences dialog, where a double-click will allow a user to remap a key.  The keybindings will be saved to a file in the data directory (probably keybindingsrc, or some similar name), which will be saved whenever keys get remapped, and loaded whenever the application starts up.  I also plan to add an import and export feature, so that users can easily save and share their keybindings.

Once I have everything working in darktable, my last planned task with regards to keyboard accelerators is to write a script, keybindings2docbook, which will convert the generated keybindings file into a table to be included in the darktable manual.  I’m open to suggestions for just how this should work, but unless I hear objections I’m thinking a command-line script in Ruby ought to do the job well enough.


