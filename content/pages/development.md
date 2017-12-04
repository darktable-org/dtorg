Title: development
Date: 2017-09-21T14:55:35-06:00
author: smn
link: http://www.darktable.org/development/
wordpress_id: 404
lede: lede-development.jpg

<div class="subnav">
    <a href="https://darktable.org/redmine/projects/darktable/wiki">developer's wiki</a>
    <a href="https://darktable.org/redmine/projects/darktable/issues">bug tracker</a>
    <a href="https://github.com/darktable-org/darktable">browse code</a>
</div>

# Contributing ...
![mushroom]({attach}mushroom.jpg)

If you feel like contributing to this project, here are a few suggestions.

## ...&nbsp;in terms of testing:

Just use it! And afterwards let us know how you like it. Send your _bug reports_, _feature requests_, _suggestions_ or just your personal opinion to our [mailing list]({filename}/pages/contact.md#how-to-get-in-contact). You can file a bug to our [bug tracker](https://darktable.org/redmine/projects/darktable/issues) as well&nbsp;– but maybe you want to discuss it first (on IRC or mailing list).

If you found a bug or managed to crash darktable, please submit a _helpful backtrace_! Instructions are below.

## ...&nbsp;in terms of translations:

If you want to _translate_ darktable into your language (in case it didn't already happen) we have a short introduction how to do that. You can find that file in our git repository, it's called [TRANSLATORS](https://github.com/darktable-org/darktable/blob/master/doc/TRANSLATORS).

You can find a list of the currently included languages on the [features page]({filename}/pages/about/features.md).

## ...&nbsp;a color matrix for your camera:

You can help us by providing a _color matrix_ for your specific camera. Color matrices are specifications on how camera native color is transformed into something that an end user might like, and ideally will be correct when viewed on a calibrated display. Read more about this in Pascal's [detailed blog post](https://encrypted.pcode.nl/blog/2010/06/28/darktable-camera-color-profiling/) or watch his [screencast](https://encrypted.pcode.nl/blog/2010/09/06/darktable-camera-color-profiling-screencast/).


# Coding
![firering]({attach}firering.jpg)

Write image operation _modules_! Submit _patches_! Help to track down bugs by supplying _backtraces_!

## How to produce a backtrace:

Pascal recorded a detailed [screencast](https://encrypted.pcode.nl/blog/2010/08/31/contributing-backtraces/) describing the procedure. For convenience here are the minimal steps:

    $ cmake ..
    $ make && sudo make install
    $ gdb darktable
    ... crash dt here ...
    (gdb) set pagination off
    (gdb) set logging file gdb.txt
    (gdb) set logging on
    (gdb) thread apply all bt full

Post the backtrace written to `gdb.txt` along with your bugreport. Or even better: Try a few prints and figure out what seems to be the problem. Best: Fix it and supply a patch!

## How do I start working on darktable using git?

First of all you have to clone the repository, so create a folder somewhere and cd into it. Then clone the source code by typing:

    $ git clone git://github.com/darktable-org/darktable.git
    $ cd darktable

Another option is to [fork](https://help.github.com/articles/fork-a-repo/) our repository on [github](https://github.com/darktable-org/darktable) to your personal account. If you do so you can send us [pull requests](https://help.github.com/articles/about-pull-requests/) instead of patches (see below).

Secondly, you really should put your _name and email_ in your .git/config, so it will appear in darktable's git log:

    $ git config --global user.name "alfons"
    $ git config --global user.email "user@domain.tld"

## What do I need to know to contribute code?

We have several different branches in our repository. Most of them are either branches for new major features that have to mature before they can go into the master branch or personal branches for developers.

If you plan to make major changes, code new features or add another module it's best to discuss them first (on IRC or the development mailinglist, see [here]({filename}/pages/contact.md) for more information). This has several advantages:

  * You can be sure we like your idea and are willing to include this in darktable (because we don't want some features others might find useful ...)
  * You can get information about work-in-progress&nbsp;– maybe we already started with that feature in some branch but can't finish it for some reason (lack of time is frequently mentioned)
  * We know about you coding that specific feature and can help if you have questions.
  * Especially for the "I want to contribute a new module" case: we don't like cluttering darktable with 100s of modules with just one use case. Most of our modules are so powerful that you can't determine the full functionality at a glance. So maybe your feature already exists?

## Now, tell me how to contribute patches ...

For bug fixes and "minor" enhancements (minor mostly in terms of code and complexity) you should always work on our master branch. This is the main developing branch for darktable and the one to become the next major release version. If your patch is also valuable for the currently maintained stable branch (so darktable-2.4.x) it will be cherry-picked to that branch by one of the developers (make sure to remind us if we forget to do so). This applies mostly to bug fixes and small usability enhancements (like a changed sorting order of list items, for example).

Supplied patches will always be reviewed by a core developer. "Review" does not mean a formal process but more a "that patch looks okay to me, I push it ...". In most cases you will be informed whether your patch has been pushed to the main repository or not. In the latter case you should get information on why we didn't want your patch and what to change so you can get it pushed. Please be patient if your patches don't get reviewed immediately, we are all quite busy (and darktable is a spare time project for all of us). If you hear nothing for two weeks you might want to bump us again&nbsp;– some things do just get lost in a flood of emails.

To work in the master branch you have switch to this branch with

    $ git checkout master

If you want to contribute fixes which are specific to another branch (let's say you're working on geolocation) checkout that specific branch first. You can print a list of all available branches with

    $ git branch -a # List all branches
    $ git branch -r # List remote branches only
    $ git checkout geo

If you want to play with the code, or occasionally want to supply small patches, you should create a local branch from the one you want to work on (here: master)

    $ git checkout master
    $ git checkout -b mybranch

Your personal local branch can be updated using

    $ git pull
    $ git checkout mybranch
    $ git rebase master

Small patches can be sent through the mailing list or attached to a ticket in the bug tracker. If you send them to the mailing list please make sure to attach them as MIME attachment, not inline. That makes it easier to apply the patch. If you are working with a cloned repository on github you just can commit your changes to your github repository and notify us about them by sending a pull request. To get formatted patches from your (local) branch against the original branch do:

    $ git checkout mybranch
    $ git format-patch origin/master

_Note:_ git format-patch writes your preferred or detected name and email address in the From: line of the patch. This is why it's good to have your preferred username and email in your .git/config file.

## So again: supplying a patch&nbsp;– fast forward

Supplying a patch from your local branch to current, possibly changed master branch:

    $ git checkout -b mybranch
    # ... make your important changes ...
    $ git commit -a
    $ git pull
    $ git rebase master
    $ git format-patch origin/master

[_git format-patch_ will create a file named similarly to 0001-First-Line-of-Commit-comment in your current directory unless you specify `-t /path/to/write/to`].
