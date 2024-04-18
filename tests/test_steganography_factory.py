import unittest
from src.steganography.steganography_factory import SteganographyFactory
from src.steganography.bmp_steganography import BMPSteganography
from src.steganography.jpg_steganography import JPGSteganography


class TestSteganographyFactory(unittest.TestCase):
    def test_create_bmp_steganography(self):
        steganography = SteganographyFactory.create_steganography('bmp')
        self.assertIsInstance(steganography, BMPSteganography)

    def test_create_png_steganography(self):
        steganography = SteganographyFactory.create_steganography('png')
        self.assertIsInstance(steganography, BMPSteganography)

    def test_create_jpg_steganography(self):
        steganography = SteganographyFactory.create_steganography('jpg')
        self.assertIsInstance(steganography, JPGSteganography)

    def test_create_unsupported_format(self):
        with self.assertRaises(ValueError):
            SteganographyFactory.create_steganography('unsupported')
