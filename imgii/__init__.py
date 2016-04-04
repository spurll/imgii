# Written by Gem Newman. This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.


import argparse, requests
from PIL import Image


CHARS = '%@#*+=-:. '
N_CHARS = len(CHARS)


def image_to_ascii(image_file, width=80, scale=2, invert=False, url=False):
    if url:
        r = requests.get(image_file, stream=True)
        r.raw.decode_content = True    # Handles spurious encoding.
        image_file = r.raw

    image = Image.open(image_file)
    x, y = image.size
    height = int(y * width / (x * scale))
    image = image.resize((width, height)).convert('L')

    text = []
    pixels = list(image.getdata())

    for i, pixel in enumerate(pixels):
        if (i > 0) and (i % width == 0):
            text.append('\n')

        index = int(pixel * N_CHARS / 256)
        text.append(CHARS[index if not invert else N_CHARS - 1 - index])

    return "".join(text)
