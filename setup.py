#!/usr/bin/env python


from setuptools import setup


setup(name='imgii',
      version='0.1.2',
      description='Very simple conversion of images to text.',
      url='https://github.com/spurll/imgii',
      author='Gem Newman',
      author_email='spurll@gmail.com',
      license='CC BY-SA 4.0',
      packages=['imgii'],
      install_requires=['requests', 'pillow'],
      zip_safe=False)
