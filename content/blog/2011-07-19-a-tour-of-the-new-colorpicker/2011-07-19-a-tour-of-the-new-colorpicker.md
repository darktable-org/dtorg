author: bieber
comments: true
date: 2011-07-19 21:25:12+00:00
layout: post
link: http://www.darktable.org/2011/07/a-tour-of-the-new-colorpicker/
slug: a-tour-of-the-new-colorpicker
title: A Tour Of The New Colorpicker
wordpress_id: 432
tags: GSoC

For my third GSOC task, I’ve replaced Darktable’s old bottom-bar colorpicker with a new one one that acts as a module in darktable mode. The new picker adds some features over the old version, which some of you will hopefully find helpful. Specifically, we have four new additions:



	
  * You can now choose point or area color picking modes.

	
  * I’ve added a simple storage system for color samples.

	
  * The big new addition is live samples, which will allow you to mark an area or point in your image and keep updated as the color at that location changes.

	
  * When picking, the image histogram will only display the area or point that you have selected.


Now, lets take a quick tour of the new interface. This is more or less what you should see initially.

![](http://www.darktable.org/wp-content/uploads/2011/09/emptypicker.png)

The big button at top left will always update to show the color you have picked. The combo-box on the top row allows you to choose between point and area selection mode, and the toggle button next to it turns color picking on and off. The combobox immediately below these allows you to select your preferred statistic in area selection mode: you can choose to view the mean, minimum, or maximum color over the selected area. The final option in this section is the color space selector, which allows you to view your color coordinates in either the RGB or Lab color space. The label underneath it shows your currently selected color in text. The next section allows you to store simple color samples.

![](http://www.darktable.org/wp-content/uploads/2011/09/history.png)

The row of buttons under the “static history” heading allows you to store up to five picked colors at a time. To save you currently picked color, just click on one of the buttons and it will replace whatever color was previously in that button. If you roll your mouse over one of the buttons, the color will display in a label underneath the buttons as text, represented in whatever color space you’re currently set to pick in. The final section of the color picker interface allows you to add live samples.

![](http://www.darktable.org/wp-content/uploads/2011/09/samples.png)

If you click the “add” button at the top right of the “live samples” section, Darktable will mark your current color picker point or area as a live sample, and display an entry for it. Using the controls to the left of the add button, you can change the color space and statistic (for area selections) that you want to show up for your live samples. As you modify the image, both the color swatch and the textual representation for each live sample will update to always mirror the current color at its location. You can, of course, remove a live sample by clicking the “remove” button to the right. Clicking the “display sample areas on image” checkbox will mark each of your live samples on the current image in blue.

![](http://www.darktable.org/wp-content/uploads/2011/09/points-300x200.png)

In addition, rolling your mouse over the color swatch for a live sample will highlight its area on the canvas in red, to distinguish it from the others. You can use this to make certain you remember just where each color sample is in the image.

The final change to the colorpicker should make itself apparent whenever you start to use it: when you select a point or an area with the colorpicker, the image histogram will update itself to reflect only the portion of the image within that selection. If you ever want to view a histogram representation of just a small portion of the image, you can do so by switching to the area selection mode and selecting it with the colorpicker. In point selection mode, you can use this feature to see just where along the scale your selected point falls.

Hopefully these changes and additions to the colorpicker interface will prove beneficial to Darktable’s users, and I welcome any comments, criticisms or suggestions regarding my work. This week I’ll now be starting my final official task, which is the addition of a levels view to the tone curve module. With any luck, I’ll have at least the GTK control itself functional by the end of the week.
