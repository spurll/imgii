#!/usr/bin/env python3


from setuptools import setup


setup(
    name='imgii',
    packages=['imgii'],
    version='0.2',
    description='Very simple conversion of images to text.',
    url='https://github.com/spurll/imgii',
    download_url='https://github.com/spurll/imgii/tarball/0.2',
    author='Gem Newman',
    author_email='spurll@gmail.com',
    license='CC BY-SA 4.0',
    install_requires=['requests', 'pillow'],
    keywords=['ascii', 'image'],
    entry_points = {'console_scripts': ['imgii = imgii:main']},
    zip_safe=False
)
