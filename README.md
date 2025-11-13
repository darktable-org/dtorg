
# darktable Website

Hugo source code and other artifacts used to generate the public Darktable website,
found at https://www.darktable.org/

## Get started

### With make(recomended)

Make sure you have hugo version `0.78.2` installed. You can run `make install-mac` or `make install-linux`.

Then, run `make server` and navigate to `http://localhost:1313`.

### Without make

Testing the site without `make` installed may be easier in some cases, especially on windows. On these systems, you must first [install Hugo](https://gohugo.io/installation/) manually, then run hugo server --renderStaticToDisk` and navigate to `http://localhost:1313`.