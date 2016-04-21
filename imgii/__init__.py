#!/usr/bin/env python3

# Written by Gem Newman. This work is licensed under the MPL2 License.


import requests
from PIL import Image
from argparse import ArgumentParser
from colorama import Fore


CHARS = ' .-=;+*#@%'
BLOCKS = ' ░▒▓█'

COLOR_MAP = {
    (0, 0, 0): Fore.BLACK,
    (1, 0, 0): Fore.RED,
    (0, 1, 0): Fore.GREEN,
    (0, 0, 1): Fore.BLUE,
    (1, 1, 0): Fore.YELLOW,
    (1, 0, 1): Fore.MAGENTA,
    (0, 1, 1): Fore.CYAN,
    (1, 1, 1): Fore.WHITE,
}


def image_to_ascii(
    image_file, width=80, scale=2, invert=False, url=False, chars=CHARS,
    color=False
):
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
        image = image.resize((width, height))
        greyscale = image.convert('L')

        text = []
        pixels = greyscale.getdata()

        if color:
            colors = list(map(ansi_color, image.getdata()))

    # Assign a character to represent each pixel.
    for i, pixel in enumerate(pixels):
        if (i > 0) and (i % width == 0):
            text.append('\n')

        index = int(pixel * n_chars / 256)

        if color and i > 0 and colors[i - 1] != colors[i]:
            text.append(colors[i])

        text.append(chars[index if not invert else n_chars - 1 - index])

    if color: text.append(Fore.RESET)

    return ''.join(text)


# Could perhaps be improved by using a blend of fore/back for ranges that fall
# between the available ANSI colours.
def ansi_color(rgb):
    # Scale and round to determine which colours are primarily involved.
    if max(rgb) > 0:
        rgb = tuple(round(x / max(rgb)) for x in rgb)

    return COLOR_MAP[rgb]


def main():
    parser = ArgumentParser(description='Converts images to ASCII.')
    parser.add_argument('image', help='The filename or URL of the image.')
    parser.add_argument('-w', '--width', help='The character output width.',
                        type=int, default=80)
    parser.add_argument('-s', '--vertical-scale', help='The factor to use when'
                        ' scaling to account for rectangular ASCII characters.'
                        ' Defaults to 2.', type=float, default=2)
    parser.add_argument('-u', '--url', help='Interpret IMAGE as a URL instead '
                        'of as a local file. (If this flag is omitted, imgii '
                        'will attempt to guess.)', action='store_true')
    parser.add_argument('-i', '--invert', help='Invert the image.',
                        action='store_true')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--chars', help='The character set to use, from '
                       'darkest to lightest. Default: {}%'.format(CHARS),
                       default=CHARS)
    group.add_argument('-b', '--blocks', help='Use the following Unicode block'
                       ' elements: {}'.format(BLOCKS), action='store_true')
    args = parser.parse_args()

    print(
        image_to_ascii(
            args.image, args.width, args.vertical_scale, args.invert, args.url,
            args.chars if not args.blocks else BLOCKS
        )
    )


if __name__ == '__main__':
    main()
