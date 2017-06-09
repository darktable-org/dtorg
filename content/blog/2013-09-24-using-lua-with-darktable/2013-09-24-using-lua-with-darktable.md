author: boucman
comments: true
date: 2013-09-24 08:22:05+00:00
layout: post
link: http://www.darktable.org/2013/09/using-lua-with-darktable/
slug: using-lua-with-darktable
title: Using Lua with darktable
wordpress_lede: img_0057.jpg
wordpress_id: 3036
tags: upcoming

The next major release of darktable will contain multiple features that have been discussed on this blog and that will make it more powerful than ever. These new features will allow you to process your images in new and creative ways.

However there is one new feature in the upcoming darktable release that is more about Digital Assets Management and simplifying your workflow: Lua scripting.

<!-- more -->

Lua is a scripting language that is commonly used to add scripting capabilities to programs. It is a programming language that is particularly simple to learn.

This post will give you a brief introduction to Lua in darktable. It is not intended to teach you Lua but to show what Lua will allow you to do and get you to read one of the multiple tutorials on Lua that you will find on the web.

The following tutorial will only work with the latest master branch and if Lua was enabled at compile time.


# Writing a Lua hello world


When darktable starts it will run a single Lua script called _luarc_ within your configuration directory. This file probably doesn't exist, so create it and add the following lines in it:

    
    dt = require "darktable"
    dt.print("Hello World!")


The first line tells the Lua engine to load all darktable specific functionalities in a variable called _dt_.

The second line tells Lua to display a control message (a small window in the middle of the main area) and display the string "Hello World!" in it.

Now start darktable. You should see that small window once the darktable window appears. Congratulation, you have run your first Lua script.


# Reloading a directory on startup


That was fun, but let's do something useful for a change.

A common way to organize images is to store them all in subdirectories of a common image directory. A commonly requested feature on the darktable mailing list is to teach darktable about this structure and re-scan that directory on startup. Let's do that.

This time put the following lines in your _luarc_ file

    
    dt = import "darktable"
    dt.storage.import("<<em>path to your directory></em>")


And you should automatically reload the directory on startup.

If it doesn't work, check any message printed by Lua on the console. This is where you will usually see syntax errors and runtime errors.


# Making this script a little bit more configurable


Ok, this is nice but we can improve it a little. Writing the path in the script is not very flexible and it would be much better to be able to set the path in darktable's configuration menu. Let's do that.

    
    dt = require "darktable"
    dt.preferences.register("myScript","load_directory","string","Image directory","A directory that will be automatically reloaded on startup","")
    
    dt.database.import(dt.preferences.read("myScript","load_directory","string"))


This works… but with a twist. There is an error in the console because the directory isn't found. Before fixing this, let's analyze the code above.

_dt.preferences.register_ will add a new preference in the Lua tab of the preference menu.



	
  * The first two parameters are a script name and the name of the preference. These two strings are invisible to the user and will uniquely identify the preference.

	
  * The next parameter is the type of the preference. In our case it is a simple string, so we use _"string"_ here.

	
  * The parameter after that is the text of the preference as it will appear in the preference menu.

	
  * Then comes a tooltip that will be displayed when the user hovers over the text box.

	
  * And last is the default value to report when someone attempts to read the preference and the user hasn't set it yet. It is also used to reset the preference when the user double-clicks on the preference label in the preference menu.


After that, we read the preference (using the script name and the preference name to identify the preference we want to read) and call _dt.database.import_ to do the real job for us.

The default value for our preference is the empty string, and this is causing the problem we see in the console. Lua uses exceptions to report errors. This tutorial won't explain exactly what an exception is, but we need to catch it before it goes up to the console and do something about it. Here we will just catch all exceptions and not do anything, since an unknown directory is not really a problem.

Let's replace the line importing the directory with the following line:

    
    pcall(dt.database.import,dt.preferences.read("myScript","load_directory","string"))


Note that we don't call _dt.database.import_ directly. We pass that function as a parameter to pcall. pcall will catch all exceptions and report them as its own result (which we ignore here).

That's good enough for importing… let's do something a bit different


# Playing with the selection and shortcuts


Another common request on the darktable mailing list is to have a way to select images easily according to some criteria. The detail depends on the person asking and the particular workflow needed. Let's look at a  way to do that with Lua.

First a little feature to make the darktable selection more handy

    
    dt = require "darktable"
    local bounce_buffer = {}
    
    local function callback()
        bounce_buffer = dt.gui.selection(bounce_buffer)
    end
    dt.register_event("shortcut",callback,"switch the current selection with a temporary buffer")


The second line creates a local variable called _bounce_buffer_ and initializes it to an empty array.

The next block of code (until the _end_ keyword) defines a function called _callback_. This function will switch the current selection and the content of the _bounce_buffer_ variable.

To do that it uses a function called _dt.gui.selection _. This function will return the current selection and will set the selection to its first parameter. An empty array represents the empty selection.

Last, the call to _dt.register_event_ tells darktable to register a new event (here a _shortcut_) and call a function (here _callback_) when that event happens. The last argument is particular to shortcut events, it's the label for the shortcut in the shortcut menu.

Now that the code is in place, you will see an entry for this action in the _lua_ section of the shortcut page of the preference window. Set a shortcut, select a couple of images and try it out. Pretty handy.


#  Selecting images with a given color label


That's nice, but let's try something different. When I use darktable, each color label has a precise meaning for me and I tend to want to quickly select all images with a given color label. The following code allows me to define a shortcut to do just that.

    
    dt = import "darktable"
    table = import "table"
    
    local function callback()
       local selection = {}
       for _,image in ipairs(dt.database) do
          if image.red then
             table.insert(selection,image)
          end
       end
       dt.gui.selection(selection)
    end
    
    dt.register_event("shortcut",callback,"select all red images")


With what we know already, this code should be quite readable. The big difference is the new _callback_ function. This one will loop through all our images and build a list of those images before passing that list to _dt.gui.selection_.


# Exporting our images as a mosaic


To finish our little journey into Lua, let's use Lua to build a new way to export images.

We will use GraphicsMagick to create a mosaic image out of our current selection.

GraphicsMagick has an all-purpose command line tool that has the following (simplified) syntax

    
    gm montage <input files…> output_file


We will integrate this into the existing export user interface so we can use darktable to easily created a tiled image of all the exported images.

The following code will do that for us:

    
    local function merge_images(storage,image_table)
        dt.print_error("Will try to stitch now")
        command = "gm montage "
        for _,v in pairs(image_table) do
            command = command..v.." "
        end
        command = command..dt.configuration.tmp_dir.."/darktable_export.png"
        os.execute(command)
    
        dt.print("Stitching saved to "..dt.configuration.tmp_dir.."/darktable_export.png")
    end
    
    dt.register_storage("mosaic","mosaic generator",nil,merge_images)


Most of this code should be understandable at this point. The only new functions are
_os.execute_ and _dt.register_storage_.

_os.execute_ is a standard Lua function that will take a string as a parameter and run the corresponding command.

_dt.register_storage_ will add a new storage implemented in Lua. Storages are the different methods that darktable can use to store images (facebook, picasa, e-mail or simply as files on the local computer).



	
  * The first parameter is a unique name for the storage.

	
  * The second parameter is the name as it will appear inside darktable.

	
  * The third parameter is a function to be called once for each image. We don't use it here so we set it to _nil_.

	
  * The last parameter is a function to be called once all images have been exported. This is where we do the real job.


With this code in your _luarc_ and GraphicsMagick installed, you should have a new entry in the export module allowing you to export the selection and generate a composite image out of it.

Simple isn't it?


# Conclusion


We have only scratched the surface of the Lua language and what can be done with it in darktable, but I hope this article has given you some ideas of new stuff to do using this nice new feature.

If you are interested, you can find the Lua reference manual [here](http://www.lua.org/manual/5.2/manual.html).

darktable's Lua interface is documented [here](http://darktable.org/redmine/projects/darktable/wiki/LuaAPI).
