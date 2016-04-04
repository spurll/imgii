imgii
=====

Python package that provides very simple conversion of images to ASCII.

Usage
=====

Installation
------------

Run `setup.py`.

Requirements
------------

* requests
* pillow

Basic Usage
-----------

```python
>>> from imgii import image_to_ascii
>>> image = image_to_ascii('Image.png')
>>> print(image)
```

By default, images are scaled to assume that output characters are twice as tall
as they are wide (as this is true for most terminals). This can be undone by
passing `scale=1`.

Images from an external URL can also be displayed by passing `url=True`. (Any
image identifier beginning with `http://` or `https://` is assumed to be a URL.)

If you're displaying the image in a dark terminal with light text (that is to
say: if you're not a monster), you may also want to pass `invert=True`.

```python
>>> image = image_to_ascii('http://cdn-01.belfasttelegraph.co.uk/incoming/article31552045.ece/82fe0/ALTERNATES/w620/US%20Monkey%201550.jpg', invert=True, url=True)
```

Here's the relevant function declaration:

```python
image_to_ascii(image_file, width=80, scale=2, invert=False, url=False)
```

A command-line interface is also provided. Run `imgii.py --help` for details.

Bugs and Feature Requests
=========================

Feature Requests
----------------

* Add optional support for UTF-8 characters to provide better coverage
* Add colour support

Known Bugs
----------

None

Other Tools
===========

There is at least one other image-to-text conversion tool available on PyPI, but
it was broken when I needed it. ¯\\\_(ツ)\_/¯

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

Remember: [GitHub is not my CV.](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/)
