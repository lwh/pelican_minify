# pelican_minify

An HTML minification plugin for
[Pelican](http://pelican.readthedocs.org/en/latest/), the static site generator.

[Code on github](https://github.com/lwh/pelican_minify) 
[Code on gitlab](https://gitlab.com/lwh/pelican_minify) 

This is a modified version of [pelican-minify](https://github.com/rdegges/pelican-minify/) [https://github.com/rdegges/pelican-minify/](https://github.com/rdegges/pelican-minify/)

## Install

To install it, copy it into your pelican plugins folder.

```bash
$ pip install htmlmin
```


## Usage

To use `pelican_minify`, you need to make only a single change to your
`pelicanconf.py` or `publishconf.py` (preferred).

Update your `PLUGINS` list, and add `pelican_minify` to the list, eg:

``` python
# publishconf.py

# ...

PLUGINS = ['abc','pelican_minify','123']

# ...
```

The next time you build your site, `pelican_minify` will automatically
minify your Pelican pages after they've been generated.

`pelican_minify` can also be configured by setting `MINIFY` to a hash containing
[parameters to htmlmin](https://htmlmin.readthedocs.org/en/latest/reference.html#htmlmin.minify), eg:

``` python
# pelicanconf.py

# ...

MINIFY = {
  'remove_comments': True,
  'remove_all_empty_space': True,
  'remove_optional_attribute_quotes': False
}

# ...
```

# Changelog

*v1.1  2019-09-27*
* Removed python2 string handling code
* Removed joblib, no parallel building

*v1.0: 2017-05-21*
* first update renamed from minify to avoid conflicts
* changed from public domain to same license as Pelican
