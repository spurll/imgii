#!/usr/bin/env python3


from setuptools import setup


setup(
    name='imgii',
    version='0.1.3',
    description='Very simple conversion of images to text.',
    url='https://github.com/spurll/imgii',
    author='Gem Newman',
    author_email='spurll@gmail.com',
    license='CC BY-SA 4.0',
    packages=['imgii'],
    install_requires=['requests', 'pillow'],
    entry_points = {'console_scripts': ['imgii = imgii:main']},
    zip_safe=False
)
