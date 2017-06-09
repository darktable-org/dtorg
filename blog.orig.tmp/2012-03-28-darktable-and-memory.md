author: upegelow
comments: true
date: 2012-03-28 16:11:48+00:00
layout: post
link: http://www.darktable.org/2012/03/darktable-and-memory/
slug: darktable-and-memory
title: Darktable and Memory
wordpress_id: 1425
tags: blog, 32-bit, 64-bit, bugfixes, memory, skull, tutorial

## or “How to drive away the evil skull”


At all times main memory was one of the most limited resources in computing. Although from 20 years to now the memory setup of a typical desktop PC has increased by a factor of several thousands (from less than a megabyte to a few gigabytes), we still need to consider how to efficiently handle that resource.

The reason of course lies in the increasing demands of modern applications. Today it might be darktable which is the single most challenging software to hit the boundaries of your system.

A simple calculation makes this clear. If you have a 20MPx image, DT for precision reasons will store this internally as a 4 × 32-bit floating point cell for each pixel. Each full image of this size will need about 300MB of memory. As we want to process the image, we will at least need two buffers for each module – one for input and one for output. If we have a more complex module, its algorithm might additionally require several intermediate buffers of the same size. Without further optimization, anything between 600MB and 3GB would be needed only to store and process image data. On top we have darktable’s code segment, the code and data of all dynamically linked system libraries, and not to forget further buffers where darktable stores intermediate images for quick access during interactive work (mip map cache). All in all darktable would like to see a minimum of about 4GB to run happily.


## Total system memory


From what I said before, it is evident that your computer needs a sane memory setup to properly run darktable. We suggest that you have a least 4GB of physical RAM plus 4 to 8GB of additional swap space installed. The latter is required, so that your system can swap out temporarily unneeded data to disk in order to free physical RAM.

Theoretically you could also run darktable with lower amounts of physical RAM and balance this with enough swap space. However, you should be prepared that your system could then heavily go into “thrashing” action, as all too many memory accesses require your system to read or write data pages from/to hard disk. We have positive reports that this functions well for several users, but it still might get extremely slow for others …


## Available address space


Besides the total amount of system memory there is another limiting factor: the available address space of your hardware architecture. How much memory can be addressed by a process depends on the number of address bits your CPU offers. For a CPU with 32-bit address registers, this is 2^32 bytes, which makes a total of 4GB. This is the absolute upper limit of memory that can be used by a process and it constitutes a tight situation for darktable as we have seen above.

Darktable’s escape route is called tiling. Instead of processing an image in one big chunk, we split the image into smaller parts for every processing step (module). This will still require one full input and output buffer, but intermediate buffers can be made small enough to have everything fit into the hardware limits.


## Memory fragmentation


Unfortunately this is not the full story yet. There is an effect called memory fragmentation, which can and will hit software that needs to do extensive memory management. If such a program allocates 5 times 300MB at a time and frees it again, that memory should normally be available for one big 1.5GB allocation afterwards. This however is often not the case. The system’s memory allocator might no longer see this area as one contiguous 1.5GB block but as a row of 300MB areas. If there is no other free area of 1.5GB available, the allocation would fail. During a program run this mechanism will take away more and more of the larger memory blocks in favor of smaller ones. Darktable 1.0 introduces a caching algorithm to address this problem. It pre-allocates blocks of memory and makes them available on request.


## Further Limitations


And as if this were not challenging enough, there are further things that might limit your access to memory. On some older boards you need to activate BIOS option “memory remapping” in order to have all physically installed memory enabled. In addition if you are on a 32-bit OS you will probably need a kernel version that has “Physical Address Extension” (PAE) enabled. This is often but not always the case for Linux. Many distributions deliver different kernels, some with and some without PAE activated; you need to choose the right one. A typical sign that one of these topics are not setup correctly is system command free (1) not reporting all of your installed physical RAM; for example you have 4GB on your board, but your kernel is only seeing 3GB or less. You need to consult the manual of your BIOS and the information about your Linux variant for further help.


## Setting up darktable on 32-bit systems


As we’ve seen 32-bit systems are difficult environments for darktable. Still many users are successfully running DT on them, if the basic requirements in terms of total system memory and the topics mentioned in the paragraphs above are addressed properly.

There are several adjustment parameters to get it running. If you make a fresh install, DT will detect your system and set conservative values by default. However, if you upgrade DT from an older version (e.g. coming from 0.9.3 and going to 1.0), chances are you have unfavorable settings in your preferences. The consequences might be DT aborting due to allocation failures or – very typically – DT not being able to properly import a new film roll. As a frequent symptom you get skulls displayed instead of thumbs for many of your pictures.

[![](http://www.darktable.org/wp-content/uploads/2012/03/skull.jpeg)](http://www.darktable.org/2012/03/darktable-and-memory/skull/)

Take a minute to optimize the preference settings in this case. You will find them under “core options” in DT’s preference dialog. You might also find these parameters as configuration variables in $HOME/.config/darktable/darktablerc and edit them there.

[![](http://www.darktable.org/wp-content/uploads/2012/03/memory_options.jpeg)](http://www.darktable.org/2012/03/darktable-and-memory/memory_options/)

Here is a short explanation of the relevant parameters and their proposed settings.

_“number of background threads”_

(parameter in darktablerc: worker_threads)

This parameter defines the maximum number of threads that are allowed in parallel when importing film rolls or doing other background stuff. For obvious reasons on 32-bit systems you can only have one thread eating resources at a time. So you need set this parameter to 1; anything higher will kill you. For the same reason you also must set the number of parallel export threads to 1.

_“host memory limit (in MB) for tiling”_

(parameter in darktablerc: host_memory_limit)

This parameter tells DT how much memory (in MB) it should assume as available to store image buffers during module operations. If an image can not be processed within these limits in one chunk, tiling will take over and process the image in several parts, one after the other. Set this to the lowest possible value of 500 as a starting point. You might experiment later whether you can increase it a bit in order to reduce the overhead of tiling.

_“minimum amount of memory (in MB) for a single buffer in tiling”_

(parameter in darktablerc: singlebuffer_limit)

This is a second parameter that controls tiling. It sets a lower limit for the size of intermediate image buffers in megabytes. The parameter is needed to avoid excessive tiling in some cases (for some modules). Set this parameter to a low value of 8. You might tentatively increase it to 16 later.

_“memory in bytes to use for mipmap cache”_

(parameter in darktablerc: cache_memory)

This controls how many thumbnails (or mip maps) can be stored in memory at a time. As a starting point set this to something like 256MB (give the number in bytes). _[Remark: in a previous version of this blog I recommended to start with 32MB. This was a bit too optimistic, as it would not be sufficient to store the thumbs even of a moderately sized film roll.  A lot of thumb reprocessing would be the consequence.]_

To avoid the problem of memory fragmentation during longer runs of darktable, the new caching scheme frontloads the memory costs and allocates this cache once at the beginning. Some Linux kernels use over-committing memory allocation, which means you don't immediately pay for all of the memory in terms of RSS (resident set size, the non-swapped physical memory), but in any case you pay for the address space. As explained before, this poses a problem for 32-bit systems and will at first sight appear as a regression over the (terribly slow, but that's another story) 0.9.3-style cache. In the long run however, this is all memory that's ever going to be allocated for thumbnails, so if we can successfully grab this portion once, we are relieving a lot of pressure on fragmentation for long sessions.


## Darktable on 64-bit systems


There's not much to be said here. Of course also 64-bit systems require a sufficient amount of main memory. So the 4GB plus swap recommendation holds true. On the other hand, 64-bit architectures do not suffer from the specific 32-bit limitations like small address space and fragmentation madness.

Any modern Intel or AMD 64-bit CPU will have an available address space in the range of several Terabytes. The word “modern” is relative in this context: all AMD and Intel CPUs introduced since 2003 and 2004, respectively, offer a 64-bit mode. Linux 64-bit has been available since many years.

All relevant Linux distributions give you the free choice to install a 32-bit or a 64-bit version with no added costs. You can even run old 32-bit binaries on a 64-bit Linux. The only thing you need to do: invest some time into the migration. In the end we strongly recommend to move to a 64-bit version of Linux. There isn't much good reason, not to make this step.
