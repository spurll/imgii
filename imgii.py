#!/usr/bin/env python

# Written by Gem Newman. This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.


import argparse
from imgii import image_to_ascii


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Converts images to ASCII.')
    parser.add_argument('image', help='The filename or URL of the image.')
    parser.add_argument('-w', '--width', help='The character output width.',
                        type=int, default=80)
    parser.add_argument('-s', '--vertical-scale', help='The factor to use when'
                        ' scaling to account for rectangular ASCII characters.'
                        ' Defaults to 2.', type=float, default=2)
    parser.add_argument('-c', '--chars', help='The character set to use, from '
                        'darkest to lightest.', default=None)
    parser.add_argument('-u', '--url', help='Interpret IMAGE as a URL instead '
                        'of a local file.', action='store_true')
    parser.add_argument('-i', '--invert', help='Invert the image.',
                        action='store_true')
    args = parser.parse_args()

    print(
        image_to_ascii(
            args.image, args.width, args.vertical_scale, args.invert, args.url,
            args.chars
        )
    )
