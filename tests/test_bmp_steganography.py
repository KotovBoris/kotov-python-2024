import os
import unittest
from src.steganography.bmp_steganography import BMPSteganography


class TestBMPSteganography(unittest.TestCase):
    def setUp(self):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.input_bmp_path = os.path.join(project_root, 'assets', 'input_image.bmp')
        self.input_png_path = os.path.join(project_root, 'assets', 'input_image.png')
        self.output_png_path = os.path.join(project_root, 'assets', 'output_image.png')
        self.text = "This is a secret message."

    def test_embed_extract_bmp(self):
        output_path = BMPSteganography.embed_text(self.input_bmp_path, self.text)
        self.assertTrue(os.path.exists(output_path))

        extracted_text = BMPSteganography.extract_text(output_path)
        self.assertEqual(extracted_text, self.text)

        os.remove(output_path)

    def test_embed_extract_png(self):
        output_path = BMPSteganography.embed_text(self.input_png_path, self.text, self.output_png_path)
        self.assertTrue(os.path.exists(output_path))

        extracted_text = BMPSteganography.extract_text(output_path)
        self.assertEqual(extracted_text, self.text)

        os.remove(output_path)

    def test_embed_long_text(self):
        long_text = "This is a very long secret message that should not fit into the image." * 9999
        with self.assertRaises(ValueError):
            BMPSteganography.embed_text(self.input_bmp_path, long_text)
