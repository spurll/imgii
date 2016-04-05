# Written by Gem Newman. This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.


import requests
from PIL import Image


CHARS = ' .-=;+*#@%'


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
    image = Image.open(image_file)
    x, y = image.size
    height = int(y * width / (x * scale))
    image = image.resize((width, height)).convert('L')

    text = []
    pixels = list(image.getdata())

    # Assign a character to represent each pixel.
    for i, pixel in enumerate(pixels):
        if (i > 0) and (i % width == 0):
            text.append('\n')

        index = int(pixel * n_chars / 256)
        text.append(chars[index if not invert else n_chars - 1 - index])

    return "".join(text)
