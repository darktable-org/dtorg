author: jo
comments: true
date: 2011-10-22 06:31:42+00:00
layout: post
link: http://www.darktable.org/2011/10/a-new-caching-backend/
slug: a-new-caching-backend
title: a new caching backend
wordpress_lede: cache.jpg
wordpress_id: 774
tags: blog, development

since i probably tend to make this more technical than any reader would like to, here's the take home message:

* much faster import of folders
* much faster thumbnail creation for first-time images
* much improved scalability wrt concurrency
* much improved scalability wrt total number of images in your database (should be good up to around 500 million images)
* much improved robustness (no more deleting ~/.cache/darktable/mipmaps all the time, yay)

## some context:

darktable's light table mode shows you your image collection in arbitrary order and filtered by arbitrary queries to the underlying database. that means that there is quite some uncertainty about which thumbnails you are going to need in the next second. so we rely on a caching mechanism that stores a few thumbnails, regenerates them as needed, and evicts not so frequently used thumbnails from the cache.

this cache worked okay, but not great in darktable <= 0.9.x. look-up times were O(log(N)) in the number of images, and i'm not going to write about the insertion times, because it's embarrassing. also it has been designed around libraw in the early days of dt, years ago.

## what changed?

since then several things happened. first, our userbase has grown, and so did their image collections. this means you would actually feel a significant slowdown when inserting more than 10k images into the old cache, since it didn't scale that well. additionally, we can now use [rawspeed](https://sh0dan.blogspot.com/2009/02/introducing-rawspeed.html) to load most of our images (can't overstress the awesomeness of this, cheers to klaus post). this change, together with some crucial changes to our pipeline (demosaicing is now done in our hands, and only on a region of interest, and only if you're zoomed in at all) brought down image loading times from like 8 seconds to 500ms.

## the new architecture

given the new circumstances, a couple of involved and backwards design decisions could be redone. we had all kinds of strange hacks to reverse-engineer a downsampled raw image from the embedded jpg thumbnail to quickly create a processed preview and things i'm not even willing to tell. all that is now gone, we just directly load the full raw, it's fast enough!

changing this opened the opportunity to completely rewrite the caching backend using a hashtable, giving us O(1) performance for all operations. it turned out that [hopscotch hashing](https://www.cs.tau.ac.il/~liortzaf/papers/disc2008_submission_98.pdf) would give us good performance even for very high fill rates, would maximize cpu cache hit rates during lookups, and allows for great concurrent access, almost lock-free (just a few custom spin locks via CAS for each segment of the table).

also this cache is based on one-time memory allocation (well, not entirely true for the full images, but same idea anyways): we do one big aligned mem alloc at startup and free it all at the end. the cache will give the thumbnail producers a small chunk of data when they need it. this avoids the issue of memory fragmentation, that lead to astronomically high memory usage in the past.

on top of the hash table, we have read/write locks and a least recently used list to evict unused data from the caches. we allow multiple concurrent readers and one exclusive writer. these constraints are now sharply enforced, so you don't even get a non-const pointer if you don't have write access.

## caching image structs

besides the obvious thumbnail caching, we also cache image structs, holding stuff like star ratings, exif data, filename. this helps reduce the pressure on disk accesses, which have been a major bottleneck in the past. this is about updating sql tables as well as writing stuff to xmp sidecars. both of these things are now only done when you drop the write lock from an image struct you got from the cache, contributing to fast import times.

## embedded thumbnails, revisited

we've been using libraw's feature to access the embedded thumbnail in a raw file in the past, in many ways as mentioned above. with the new, faster, simplified architecture, it was a 5min job to put that back in for images you're viewing for the first time in darktable. that greatly speeds up the perceived import time, as thumbnails show up much faster. on the downside, these are what your camera gave you. which means not color managed, no control over demosaicing or anything else. so there will be occasional surprises when entering darkroom mode ... which is why there still is the setting in prefs that allows you to switch off this low quality shortcut.

## when can i get it?

well, you don't just yet. it's in our next-gen branch, post-0.9. you can check that out and help us debug a lot of issues we still have there. at this stage, i wouldn't quite recommend it for production use. help debugging/fixing is always appreciated, but if you go there, expect some rough edges. in any case, expect the next big version of dt to be much faster!
