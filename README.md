imgii
=====

Python package that provides very simple conversion of images to ASCII.

Usage
=====

Testing
-------

Run `python3 test/runtests.py`.

You may see warnings related to unclosed file handles. This is a result of the
way Pillow handles files, and there doesn't seem to be much to be done about it.

Installation
------------

Run `setup.py install`.

Requirements
------------

* requests
* pillow

Basic Usage
-----------

In Python:

```python
>>> from imgii import image_to_ascii
>>> image = image_to_ascii('image.png')
>>> print(image)
```

From the console:

```bash
$ imgii image.png
```

By default, images are scaled to assume that output characters are twice as tall
as they are wide (as this is true for most terminals). This can be undone by
passing `scale=1`.

Images from an external URL can also be displayed by passing `url=True`. (Any
image identifier beginning with `http://` or `https://` is assumed to be a URL.)

If you're displaying the image in a light terminal with dark text (that is to
say: if you're a monster), you may also want to pass `invert=True`.

```python
>>> image = image_to_ascii('http://cdn-01.belfasttelegraph.co.uk/incoming/article31552045.ece/82fe0/ALTERNATES/w620/US%20Monkey%201550.jpg', invert=True, url=True)
```

Here's the relevant function declaration:

```python
image_to_ascii(image_file, width=80, scale=2, invert=False, url=False, chars=CHARS)
```

Two character sets are available by default:

1. `imgii.CHARS` is the default ASCII character set.
2. `imgii.BLOCKS` is an alternate character set using a limited number of Unicode [block elements](https://en.wikipedia.org/wiki/Block_Elements).

Bugs and Feature Requests
=========================

Feature Requests
----------------

* Add colour support

Known Bugs
----------

* Not really a bug, but keep in mind that some common Terminal fonts don't fully support the Unicode block character set

Other Tools
===========

There is at least one other image-to-text conversion tool available on PyPI, but
it was broken when I needed it. ¯\\\_(ツ)\_/¯

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/).

Remember: [GitHub is not my CV.](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/)
