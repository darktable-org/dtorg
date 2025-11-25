---
Title: meta
Date: 2017-06-16T13:50:27-06:00
Author: Pat David
lede: lede-meta.jpg
lede_author: <a href="https://houz.org/">houz</a>
weight: 3
menu: "footer"
---
This is a meta page about this website and building it.
[Pat David](https://patdavid.net) created this page for notes about building the site.



## Hugo

We're using [Hugo][] to create a static website.

[Hugo]: https://gohugo.io/ "Hugo Homepage"



## Content Classification

From a template/Hugo point of view, there are 2 major types of generated content: `pages` and `articles`.

* `pages` are static pages like [about](/about) or [install](/install).
* `articles` are timely, chronological content like [news](/news) or [blog](/blog) posts.


## Markdown

The usual markdown all works, but there are a couple of things to be aware of.


### Images

Images that will have a caption can be wrapped in a `<figure>` tag.

* If you want the image to have a caption, include a `<figcaption>` tag to wrap it.
* If you want markdown to be parsed inside these tags, add an attribute to `<figure>`, `<figure markdown="span">`

An example image, with caption, with markdown parsed in the figcaption:

```html
<figure markdown='span'>
<img src="dot-eyes.jpg" alt="ALT_TEXT">
<figcaption>
**Bolded** as well as _italics_, or even [a link](https://patdavid.net).
</figcaption>
</figure>
```

Should render as:

<figure markdown='span'>
<img src="dot-eyes.jpg" alt="ALT_TEXT" width="640" height="479">
<figcaption>**Bolded** as well as _italics_, or even [a link](https://patdavid.net).</figcaption>
</figure>

Long captions should also wrap at the max-width of the image being included automatically.

You can also use one of the utility classes to float content left or right.
You can use `u-pull-right` or `u-pull-left`:

```
<figure markdown='span' class='u-pull-right'>
<img src="dot-eyes.jpg" alt="ALT_TEXT">
<figcaption>**Bolded** as well as _italics_, or even [a link](https://patdavid.net).</figcaption>
</figure>
```

<figure markdown='span' class='u-pull-right'>
<img src="dot-eyes.jpg" alt="ALT_TEXT">
<figcaption>**Bolded** as well as _italics_, or even [a link](https://patdavid.net).</figcaption>
</figure>

In this case I have also set a `max-width: 50%;` on the `<figure>` element if you float it left or right.
If it gets too big, it's awkward to read the remaining text, and is best to just let it be a block-level element.
The rest of this paragraph is filler to demonstrate the float better.
Bacon ipsum dolor amet chicken porchetta cow short loin drumstick, capicola jerky pancetta strip steak kielbasa brisket tri-tip tail. Tenderloin ham hock shoulder prosciutto andouille picanha pork loin cow meatloaf leberkas jowl spare ribs strip steak porchetta landjaeger. Ham hock prosciutto cupim sausage, ribeye t-bone short ribs kielbasa pork chop drumstick pork loin shoulder andouille spare ribs jowl. Pork belly bacon short ribs, frankfurter tri-tip swine rump tail.

## Lede images

The old blog had ledes of size 200x100. The new one uses the aspect ratio 2.39:1 and prefers an image size of 2048x857. There is a [list of old ledes](/small_ledes.html) that we still need a big and wide version for. If you provided images for the old website it would be awesome if you could look through the list, check if any are from you and if you have them in high res, cropped to the required format. If you know that some image is from you but don't have the original any longer or prefer to not upload a high res version licensed CC-BY-SA then please tell us so we can pick some other image as a replacement.
