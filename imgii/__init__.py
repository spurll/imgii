#!/usr/bin/env python3

# Written by Gem Newman. This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.


import requests
from PIL import Image
from argparse import ArgumentParser


CHARS = ' .-=;+*#@%'
BLOCKS = ' ░▒▓█'


def image_to_ascii(
    image_file, width=80, scale=2, invert=False, url=False, chars=None
):
    if chars is None:
        chars = CHARS
    n_chars = len(chars)

    # Try to guess if the file is a URL, in case the user was just lazy.
    url = url or image_file.startswith(('http://', 'https://'))

    if url:
        r = requests.get(image_file, stream=True)
        r.raw.decode_content = True    # Handles spurious content encoding.
        image_file = r.raw

    # Load the image into Pillow, scale appropriately, convert to greyscale.
    with Image.open(image_file) as image:
        x, y = image.size
        height = int(y * width / (x * scale))
        image = image.resize((width, height)).convert('L')

        text = []
        pixels = list(image.getdata())
        image.close()

    # Assign a character to represent each pixel.
    for i, pixel in enumerate(pixels):
        if (i > 0) and (i % width == 0):
            text.append('\n')

        index = int(pixel * n_chars / 256)
        text.append(chars[index if not invert else n_chars - 1 - index])

    return "".join(text)


def image_to_blocks(image_file, width=80, scale=2, invert=False, url=False):
    return image_to_ascii(image_file, width, scale, invert, url, BLOCKS)


def main():
    parser = ArgumentParser(description='Converts images to ASCII.')
    parser.add_argument('image', help='The filename or URL of the image.')
    parser.add_argument('-w', '--width', help='The character output width.',
                        type=int, default=80)
    parser.add_argument('-s', '--vertical-scale', help='The factor to use when'
                        ' scaling to account for rectangular ASCII characters.'
                        ' Defaults to 2.', type=float, default=2)
    parser.add_argument('-u', '--url', help='Interpret IMAGE as a URL instead '
                        'of a local file.', action='store_true')
    parser.add_argument('-i', '--invert', help='Invert the image.',
                        action='store_true')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--chars', help='The character set to use, from '
                        'darkest to lightest.', default=None)
    group.add_argument('-b', '--blocks', help='Use block elements: ░▒▓█',
                       action='store_true')
    args = parser.parse_args()

    print(
        image_to_ascii(
            args.image, args.width, args.vertical_scale, args.invert, args.url,
            args.chars
        ) if not args.blocks else image_to_blocks(
            args.image, args.width, args.vertical_scale, args.invert, args.url
        )
    )


if __name__ == '__main__':
    main()
