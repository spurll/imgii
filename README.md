imgii
=====

Python package that provides very simple conversion of images to ASCII.

![Photo](/screenshots/photo.jpg?raw=true)
![ASCII](/screenshots/ascii.png?raw=true)

![Firefox Logo](/screenshots/firefox-logo.png?raw=true)
![Firefox Block](/screenshots/firefox-block.png?raw=true)

Usage
=====

Testing
-------

Run `python3 test/runtests.py`.

You may see warnings related to unclosed file handles. This is a result of the
way Pillow handles files, and there doesn't seem to be much to be done about it.

Installation
------------

Install via pip with `pip3 install imgii` or download the source and run
`setup.py install`.

Requirements
------------

* requests
* pillow
* colorama

Basic Usage
-----------

In Python:

```python
>>> from imgii import image_to_ascii
>>> image = image_to_ascii('image.png')
>>> print(image)
```
Here's the relevant function declaration:

```python
image_to_ascii(image_file, output_width=None, console_width=None, scale=2, invert=False, url=False, chars=CHARS, color=False)
```

From the console:

```bash
$ imgii image.png
```

You can view the available flags by passing `-h`.

### Image Size

By default, `imgii` will attempt to scale the image appropriately based on the
size of your console. You may also specify the console width with the
`console_width` argument.

Alternatively, you may manually specify the output width of the image (in
characters) by passing the `output_width` argument. (Note that this may result
in small images being stretched.)

By default, images are also scaled under the assumption that output characters
are twice as tall as they are wide (as this is true for most terminals). This
can be undone by passing `scale=1`.

### External URLs

Any image identifier beginning with `http://` or `https://` is assumed to be a
web URL. An external URL can also be displayed by passing `url=True`.

### Colour

If you're displaying the image in a light terminal with dark text (that is to
say: if you're a monster), you may also want to pass `invert=True`.

Some basic ANSI colour support is also provided, but it's kind of hit-or-miss.
Pass `color=True` to try it out.

### Character Sets

Two character sets are available by default:

1. `imgii.CHARS` is the default ASCII character set.
2. `imgii.BLOCKS` is an alternate character set using a limited number of
   Unicode [block elements](https://en.wikipedia.org/wiki/Block_Elements).

Custom character sets are also supported, and may be passed in with the `chars`
argument.

Bugs and Feature Requests
=========================

Feature Requests
----------------

* Improve colour support with the extended colour space.

Known Bugs
----------

* Not really a bug, but keep in mind that some common Terminal fonts don't fully
  support the Unicode block character set

Other Tools
===========

There is at least one other image-to-text conversion tool available on PyPI, but
it was broken when I needed it. ¯\\\_(ツ)\_/¯

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/).

Remember: [GitHub is not my CV](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/).
