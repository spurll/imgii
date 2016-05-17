import unittest
import os, sys

# Default to using the repository's version of the module rather than the
# installed version when running this script.
script_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(script_dir, '..'))

from imgii import image_to_ascii, BLOCKS


test_dir = os.path.dirname(__file__)
FACE = os.path.join(test_dir, 'face.jpg')
FACE_INVERT = os.path.join(test_dir, 'face_invert.jpg')
GRADIENT = os.path.join(test_dir, 'gradient.png')
GRADIENT_INVERT = os.path.join(test_dir, 'gradient_invert.png')


class Tests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(
            image_to_ascii(FACE, output_width=5, scale=1),
            '\n'.join([
                '     ',
                ' % % ',
                '     ',
                ' %%% ',
                '     '
            ])
        )

        self.assertEqual(
            image_to_ascii(GRADIENT, output_width=4, scale=1),
            '\n'.join([
                '%@*+',
                '@#+=',
                '*+-.',
                '+=. '
            ])
        )

    def test_scale(self):
        # Scale the width/height of the image.
        self.assertEqual(
            image_to_ascii(FACE, output_width=10, scale=1),
            '\n'.join([
                '          ',
                '          ',
                '  %%  %%  ',
                '  %%  %%  ',
                '          ',
                '          ',
                '  %%%%%%  ',
                '  %%%%%%  ',
                '          ',
                '          '
            ])
        )

        # Scaling chars.
        self.assertEqual(
            image_to_ascii(FACE, output_width=10, scale=2),
            '\n'.join([
                '          ',
                '  %%  %%  ',
                '          ',
                '  %%%%%%  ',
                '          '
            ])
        )

        # Default scale is 2, as text is typically twice as high as it is wide.
        self.assertEqual(
            image_to_ascii(FACE, output_width=10, scale=2),
            image_to_ascii(FACE, output_width=10)
        )

    def test_custom_chars(self):
        self.assertEqual(
            image_to_ascii(GRADIENT, output_width=4, scale=1, chars='12345'),
            '\n'.join([
                '5543',
                '5432',
                '4321',
                '3211'
            ])
        )

        self.assertEqual(
            image_to_ascii(FACE, output_width=5, scale=1, chars=BLOCKS),
            '\n'.join([
                '     ',
                ' █ █ ',
                '     ',
                ' ███ ',
                '     '
            ])
        )

        self.assertEqual(
            image_to_ascii(GRADIENT, output_width=4, scale=1, chars=BLOCKS),
            '\n'.join([
                '██▓▒',
                '█▓▒░',
                '▓▒░ ',
                '▒░  '
            ])
        )

    def test_invert(self):
        self.assertEqual(
            image_to_ascii(FACE, output_width=5, scale=1, invert=True),
            '%%%%%\n% % %\n%%%%%\n%   %\n%%%%%'
        )

        self.assertEqual(
            image_to_ascii(FACE, invert=True),
            image_to_ascii(FACE_INVERT)
        )
        self.assertEqual(
            image_to_ascii(FACE),
            image_to_ascii(FACE_INVERT, invert=True)
        )

        self.assertEqual(
            image_to_ascii(GRADIENT, invert=True),
            image_to_ascii(GRADIENT_INVERT)
        )
        self.assertEqual(
            image_to_ascii(GRADIENT),
            image_to_ascii(GRADIENT_INVERT, invert=True)
        )

if __name__ == '__main__':
    unittest.main()
