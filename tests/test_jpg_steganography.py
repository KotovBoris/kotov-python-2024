import os
import unittest
from src.steganography.jpg_steganography import JPGSteganography


class TestJPGSteganography(unittest.TestCase):
    def setUp(self):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.input_jpg_path = os.path.join(project_root, 'assets', 'input_image.jpg')
        self.text = "This is a secret message."
        self.output_path = os.path.join(project_root, 'assets', 'output_image.jpg')

    def test_embed_extract_jpg(self):
        output_path = JPGSteganography.embed_text(self.input_jpg_path, self.text)
        self.assertTrue(os.path.exists(output_path))

        extracted_text = JPGSteganography.extract_text(output_path)
        self.assertEqual(extracted_text, self.text)

        os.remove(output_path)

    def test_embed_with_output_path(self):
        JPGSteganography.embed_text(self.input_jpg_path, self.text, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

        os.remove(self.output_path)

    def test_extract_from_empty_image(self):
        extracted_text = JPGSteganography.extract_text(self.input_jpg_path)
        self.assertEqual(extracted_text, '')
