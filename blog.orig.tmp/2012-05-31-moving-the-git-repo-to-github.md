author: jcsogo
comments: true
date: 2012-05-31 13:24:17+00:00
layout: post
link: http://www.darktable.org/2012/05/moving-the-git-repo-to-github/
slug: moving-the-git-repo-to-github
title: Moving the git repo to github [done]
wordpress_id: 1707
tags: announcement, infrastructure, darktable, download, fork, git, github, move, remote, repository

**Update: **the [git repository](http://github.com/darktable-org/darktable) officially resides in github now.

Today we are moving our git repo from sf.net to github, as it was agreed in the [developer meeting](http://darktable.org/redmine/projects/darktable/wiki/Dev_Meeting_Agenda) that took place yesterday. This will happen **today 22:00 - 23:00 CEST**

_What should I do now?_

Depends on the role you play in the project.



	
  1. You have commit rights into current [sf.net](http://sf.net) repository: please open an account in github if you don't have any and make me know it. I will give you those permits there, but do not push there for now, your changed will be lost.

	
  2. You don't have commit rights but regularly contribute back patches to darktable: please consider doing a [fork](http://help.github.com/fork-a-repo/) of our repo in github and make a branch there for your patches. Later on make a [pull request](http://help.github.com/send-pull-requests/) to let us know that we should pull from your branch.

	
  3. If you make some patches, but not in a regular way, you can also benefit of having your own fork...  it will allow to publish your changes, access them from remote places, and have a backup place for your repo in case of disaster.

	
  4. You only track the repo. Wait until the switch is made and follow the instructions in this post.





_What is going to happen just before the switch?_

We are going to disable push rights of the people in [sf.net](http://sf.net), so nothing is pushed there, and we are going to make a mirror to github, enabling in that moment the rights to push to github._ What should I do when the switch is made?_When things are in place, you have to set your repo to point to the right place. To do that  the command is (I suppose that origin is pointing to [sf.net](http://sf.net), if not, change the name):

git remote set-url origin git@github.com:darktable-org/darktable.git
or
git remote set-url origin git://[github.com/darktable-org/darktable.git](http://github.com/darktable-org/darktable.git)






Depending if you have a github account or not (and if you have commit rights). You can also use https to read and write to the repo using [https://USERNAME@github.com/darktable-org/darktable.git](https://USERNAME@github.com/darktable-org/darktable.git)2. Now, calling 'git fetch' or 'git pull'  should connect to the repository held in GitHub.







_Will be [sf.net](http://sf.net) repo deleted?_

A hook will be set so it pushes changes for a time to [sf.net](http://sf.net) repo, while the transition is completed. After several months, it will be removed, but by default do not count that repo as being canonical any more.I am sure this change will engage more people in sending patches and contributing code to darktable. And we need your time, skills, and ideas.
