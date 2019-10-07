
# darktable Website

This repository holds the [Pelican][] source code of the [darktable.org][] website. Help improving the website by submitting pull-requests.

[darktable.org]: http://darktable.org
[Pelican]: https://blog.getpelican.com/

The website is a static site, pre-generated from source files using [Pelican][](Python).


## Tools

Pelican uses Python.
The site is currently built using:

```bash
$ python --version
Python 2.7.13

$ pelican --version
3.6.3

$ markdown_py --version
markdown_py 2.6.6
```

Additionally, some extra modules should be available:

* PIL/pillow  
 `$ pip install pillow`
* python-twitter  
 `$ pip install python-twitter`
* BeautifulSoup  
 `$ pip install bs4`
* Typogrify  
 `$ pip install typogrify`


## Getting Started

It's generally good practice to use a [virtual environment](https://docs.python-guide.org/dev/virtualenvs/):

```bash
$ virtualenv2 env/
$ source env/bin/activate
$ pip install -r requirements.txt
```

To build the site:
```bash
$ pelican -s pelicanconf.py
```

The entire site will then be available in the `output` directory. 
If you don't already have SimpleHTTPServer install it:

```bash
$ pip install SimpleHTTPServer
```

To serve the site via HTTP, launch:

```bash
$ cd output/ && python2 -m SimpleHTTPServer 8000
```
