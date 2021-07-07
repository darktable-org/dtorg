HUGO_VERSION = 0.78.2

-include .env
export

#
# Hugo installation
#

.PHONY: install-mac
install-mac:
	curl -sSL https://github.com/gohugoio/hugo/releases/download/v$(HUGO_VERSION)/hugo_extended_$(HUGO_VERSION)_macOS-64bit.tar.gz \
  	| sudo tar -v -C /usr/local/bin -xz \
    && sudo chmod 755 /usr/local/bin/hugo \
    && /usr/local/bin/hugo version

.PHONY: install-linux
install-linux:
	curl -sSL https://github.com/gohugoio/hugo/releases/download/v$(HUGO_VERSION)/hugo_extended_$(HUGO_VERSION)_Linux-64bit.tar.gz \
  	| sudo tar -v -C /usr/local/bin -xz \
    && sudo chmod 755 /usr/local/bin/hugo \
    && /usr/local/bin/hugo version

rename:
	cd content/blog && find -type f -name "*.md" -execdir mv -v {} index.md \;

firstline:
	cd content/blog && find -type f -name "*.md" -exec sed -i '1 i\---' {} +

secondline: #shell only
	cd content/blog && find -type f -name "*.md" -exec sed -i '0,/^$/{s/^$/---/}' {} > index.md +

.PHONY: server
server:
	rm -rf public && hugo server --renderToDisk