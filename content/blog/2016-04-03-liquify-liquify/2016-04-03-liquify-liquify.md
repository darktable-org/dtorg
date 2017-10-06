author: pascalobry
comments: true
date: 2016-04-03 08:09:43+00:00
layout: post
link: http://www.darktable.org/2016/04/liquify-liquify/
slug: liquify-liquify
title: Liquify, liquify?
wordpress_lede: liquify-1.png
wordpress_id: 4038
tags: blog, upcoming feature

Most modules in darktable are working on changing pixels color, lightness, etc. Few modules are moving pixels and when they do they are doing it in a very constraint way like to rotate, fix the lens' distortions or remove spots.

The liquify module offer more ways to move pixels around by applying some free style distortions to parts of the image. There is three tools to help doing that:



	
  * point

	
  * line

	
  * curve


![liquify-0](https://www.darktable.org/wp-content/uploads/2016/04/liquify-0.png)

Each tool is based on nodes. A point is given by a single node, a line
or curve by a set of nodes which defines the path.

Next to the count, in order we have the following tools:



	
  * hide/show the warps

	
  * the **point** tool

	
  * the **line** tool

	
  * the **curve** tool

	
  * the node edit tool


Let's see what a node does:

![liquify-1](https://www.darktable.org/wp-content/uploads/2016/04/liquify-1-494x320.png)



	
  * **center** : with the central point, it is possible to drag this point with the mouse to move it around

	
  * **radius** : the radius describes the area of the applied effect, that is the distortion occurs only inside this radius. It is possible to increase the radius using the small dot on the circle.

	
  * **strength vector** : the vector starting from the center describes the direction of the distortion and the strength. The strength depends on the length of the vector.


The point, line and curve tools are all based on nodes as described above. That is, a line is a set of nodes linked together for example.


# Point Tool


A point is formed by a single node. In a point the strength vector
has three different modes which are toggled using ctrl-click over the
strength vector itself.



	
  * **linear** : the linear mode make the distortion linear inside the circle. Starting from the opposite side of the strength vector and following the strength vector direction. This is the default mode.

	
  * **radial growing** : in this mode the strength vector effect is radial, starting with a strength of 0% in the center and growing when going away from the center.



	
  * ![liquify-4](https://www.darktable.org/wp-content/uploads/2016/04/liquify-4-494x322.png)**radial shrinking** : in this mode the strength vector effect is radial, starting with a strength of 100% in the center and shrinking when going away from the center.


![liquify-3](https://www.darktable.org/wp-content/uploads/2016/04/liquify-3-494x320.png)

Furthermore it is possible to set the feathered effect by clicking on the center of the circle.

![liquify-2](https://www.darktable.org/wp-content/uploads/2016/04/liquify-2-494x322.png)



	
  * **default** : linear from the center to the radius

	
  * **feathered** : two control circles are displayed and can be used to feather the strength of the effect.




# Line Tool


![liquify-5](https://www.darktable.org/wp-content/uploads/2016/04/liquify-5-494x321.png)

A line is a set of point. The points are linked together, the effect is interpolated by a set of strength vectors.

It is possible to add a control point on a line by ctrl-click on a segment.

A right-click on a segment will remove the shape completely.

A ctrl-alt-click on a segment will change it to a curve segment.


# Curve Tool


![liquify-6](https://www.darktable.org/wp-content/uploads/2016/04/liquify-6-494x322.png)

A curve is a set of point. The points are linked together, the effect is interpolated as a bezier curve by a set of strength vectors.

It is possible to add a control point on a line by ctrl-click on a segment.

A right-click on a segment will remove the shape completely.

A ctrl-alt-click on a segment will change it to a line segment.

It is possible to change the way the points of the curve are linked together by using ctrl-click on the center. There is four modes which correspond to different way of handling the two bezier curve points:



	
  * **autosmooth** : control points are always giving a smooth curve, this is the default mode in which the control points are not displayed (as automatically computed).

	
  * **cups** : control points can be moved independently.

	
  * **smooth** : control points are always giving a smooth curve

	
  * **symmetrical** : control points are always moved together


Finally, note that at any moment it is possible to right-click on the image to show or hide the liquify controls.

We feel that such tool will be quite handy in Studio photography, but not only.
