author: houz
comments: true
date: 2011-03-26 22:11:10+00:00
layout: post
link: http://www.darktable.org/2011/03/why-gimp-doesn%e2%80%99t-play-well-with-darktable/
slug: why-gimp-doesnt-play-well-with-darktable
title: Why GIMP doesn’t play well with darktable
wordpress_lede: gimp.png
wordpress_id: 460
tags: development




Every now and then the question arises why we don’t have a button in darktable to open the current image in [GIMP](http://www.gimp.org/). Everytime I answer more or less the same.




The arguments of those requesting the button are along the line of “$PROGRAM has it, so it shouldn’t be hard to do” and “I really need to do some small retouching, so it would save me lots of time”.




Well, to understand why we don’t have it I have to stress two features of darktable. First of all, every action is done non-destructive. What that means is that you never edit the actual data in your RAW file, but “record” a list of actions (the history in darkroom mode and the XMP files) which shall be executed to get the final image. This list can be changed afterwards without negative side effects since those actions can just be recomputed. The second nice thing in darktable is that we work with high bit depths (32 bit floating point) to get the best possible result.




Let’s have a look at GIMP next. None of the operations (with a few exceptions like layer creation, …) are non-destructive, and about bit depth in GIMP has been written enough.




“What are the consequences?” you might wonder. Well, we would have to export the image and tell GIMP to open it, since plain image files is the only common language these two applications speak. That’s easy. However, what happens if you want to change the processing in darktable afterwards (remember, non-destructive editing)? All your work in GIMP is useless now.




There is hope though. GIMP is currently moving to gegl as the new underlying core. This will bring two features (besides others): non-destructive editing and high bit depths. Sounds familiar? Once that is about to happen we can resurrect the use of gegl in darktable (we actually had it once, but it didn’t work well). Having all our processing as gegl operators it should be straight forward to hand all of the darktable processing over to gimp which can carry on with editing the file and passing the result back to darktable. At no point in this process we would lose control over the result as anything can be tweaked later on and has the best possible quality.




Until then, it doesn’t make sense to ask for passing an image over to GIMP (or any other image manipulation program for that matter) as it would be a [sink](http://en.wikipedia.org/wiki/Sink_%28computing%29) in our pipeline.




One last thing: I love GIMP, use it all the time and think these guys (and gals) are doing a great job. They have about the same number of developers as we have, while their code base is several orders of magnitude bigger.






