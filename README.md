
# darktable-web

This is a repository for testing migrating [darktable.org][] to [Pelican][].

[darktable.org]: http://darktable.org
[Pelican]: https://blog.getpelican.com/


## Front Page

Content for the front page by priority at the moment:

* Project name + description
* Screenshots
* 3-4 features to highlight


## News/Blog

These are two distinct things, possibly merge them but get a consensus from the dt team what they want.


## Tools

Pelican uses Python.
This is set up using:

```
$ python --version
Python 2.7.13

$ pelican --version
3.6.3
```

Additionally, some extra modules should be available:

* PIL/pillow  
 `$ pip install pillow`
* python-twitter  
 `$ pip install python-twitter`

To build the site:
```bash
$ pelican -s pelicanconf.py
```
