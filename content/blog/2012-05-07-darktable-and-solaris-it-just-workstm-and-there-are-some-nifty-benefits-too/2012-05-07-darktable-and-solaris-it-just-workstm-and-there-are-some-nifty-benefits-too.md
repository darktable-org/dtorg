author: McBofh
comments: true
date: 2012-05-07 23:57:08+00:00
layout: post
link: http://www.darktable.org/2012/05/darktable-and-solaris-it-just-workstm-and-there-are-some-nifty-benefits-too/
slug: darktable-and-solaris-it-just-workstm-and-there-are-some-nifty-benefits-too
title: 'Darktable and Solaris: It Just Works(tm) .... and there are some nifty benefits
  too'
wordpress_lede: supermoon-ss.jpg
wordpress_id: 1475
tags: blog, DTrace, port, Solaris

I'm the self-appointed maintainer of Darktable on [Solaris](http://www.oracle.com/us/products/servers-storage/solaris/solaris11/overview/index.html), which is a fairly easy gig to keep on top of.

Here's why that is so: Darktable's codebase is very portable. It's not riddled with operating system-specific assumptions; it uses standard C (with some C++), and apart from the OpenCL support every prerequisite library is buildable on Solaris with gcc or g++. I'd prefer to use [Oracle Solaris Studio](http://www.oracle.com/us/products/servers-storage/solaris/studio/overview/index.html) because that's my work compiler, but there's no great incentive for me to beat up on all the prerequisites to make them behave.

To date I've contributed more by way of packaging metadata and bug updates than code changes and I like that. If you're curious, I [wrote a blog post](http://www.jmcpdotcom.com/blog/2012/03/14/how-to-build-a-package-archive-for-darktable/) about how to generate a new Darktable package in the [Solaris 11 IPS](http://hub.opensolaris.org/bin/view/Project+pkg/) format.

My plans for future Solaris involvement are chiefly around how we scale to larger memory configurations (specifically, the mipmap cache) and our database usage - with [DTrace](http://dtrace.org/blogs/about/#awards) I can see very clearly how long queries and updates are taking in real time. While the command line debug flags are handy, they do slow down interactive operation with printing output to a file.

For instance, on my system (dual-core/dual-processor 3.0GHz Opteron cpus with 32Gb ram, 512Mb nVidia framebuffer with a development build of a successor to Solaris 11), the gui response when I'm typing in a characters from a tag is (subjectively) awful. To get an idea of how awful, I added a new tag to a photo I took last night of the SuperMoon:


    
    
    $ dtrace -n'pid517::dt_tag_new:entry{self->traced = 1; self->timestamp = vtimestamp; self->tag=copyinstr(arg0); self->tagid= (int)arg1;}' \
    -n'pid517::dt_tag_new:return/self->traced/ {self->traced = 0; printf("dt_tag_new(%s, %d) took  %d nsec", self->tag, self->tagid, vtimestamp - self->timestamp);}' 
    dtrace: description 'pid517::dt_tag_new:entry' matched 1 probe
    dtrace: description 'pid517::dt_tag_new:return' matched 1 probe
    
    CPU     ID                    FUNCTION:NAME
      3 167336                dt_tag_new:return dt_tag_new(clouds, 134506508) took  9226022 nsec
    



[![](http://www.darktable.org/wp-content/uploads/2012/05/supermoon-ss-494x300.jpg)](http://www.darktable.org/2012/05/darktable-and-solaris-it-just-workstm-and-there-are-some-nifty-benefits-too/supermoon-ss/)

That's a fairly simple one-liner for a very simple use-case. It's a bit of a worry that it took 9 milliseconds (thankyou to the commenters below for picking up my error with the order of magnitude) for that function to return. Now that I've got some hard data I can get started with drilling down into what the possible causes are, using the analytical troubleshooting system (an implementation of [Kepner-Tregoe's Problem Solving and Decision Management](http://www.kepner-tregoe.com/TheKTWay/WorkingWithKT-TeachYou-PSDM.cfm) methodology) which I was taught while working at (the late) Sun Microsystems.

Looking through the code for dt_tag_new, I think we've got the possibility of some small optimisations. I've been trying out the idea of keeping the tags and tagxtag tables in memory and updating the on-disk versions using a SQLite3 trigger. However.... more investigation is needed. I'll be using Dtrace to help me see what works best.



Solving little things like that is where I think I can bring most to this project, and where having Solaris as a tier-1 development platform becomes very useful.


Self-promotion: when I blog about Darktable, I post at [http://www.jmcpdotcom.com/blog/category/darktable/](http://www.jmcpdotcom.com/blog/category/darktable/).
