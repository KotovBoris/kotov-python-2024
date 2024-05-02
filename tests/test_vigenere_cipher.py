import unittest
from src.cipher.vigenere_cipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(VigenereCipher.encrypt('ATTACKATDAWN', 'LEMON'), 'LXFOPVEFRNHR')
        self.assertEqual(VigenereCipher.encrypt('attackatdawn', 'lemon'), 'lxfopvefrnhr')

    def test_decrypt_basic(self):
        self.assertEqual(VigenereCipher.decrypt('LXFOPVEFRNHR', 'LEMON'), 'ATTACKATDAWN')
        self.assertEqual(VigenereCipher.decrypt('lxfopvefrnhr', 'lemon'), 'attackatdawn')

    def test_encrypt_with_spaces_and_punctuation(self):
        self.assertEqual(VigenereCipher.encrypt('Attack at dawn!', 'lemon'), 'Lxfopv mh oeib!')

    def test_decrypt_with_spaces_and_punctuation(self):
        self.assertEqual(VigenereCipher.decrypt('LxfoPv mh oeib!', 'lemon'), 'AttaCk at dawn!')

    def test_encrypt_with_long_key(self):
        self.assertEqual(VigenereCipher.encrypt('hello', 'averylongkeythatdoesnotrepeat'), 'hzpcm')

    def test_decrypt_with_long_key(self):
        self.assertEqual(VigenereCipher.decrypt('hzpcm', 'averylongkeythatdoesnotrepeat'), 'hello')

    def test_encrypt_empty_string(self):
        self.assertEqual(VigenereCipher.encrypt('', 'lemon'), '')

    def test_decrypt_empty_string(self):
        self.assertEqual(VigenereCipher.decrypt('', 'lemon'), '')

    def test_encrypt_decrypt_with_empty_key(self):
        with self.assertRaises(ValueError):
            VigenereCipher.encrypt('hello', '')
        with self.assertRaises(ValueError):
            VigenereCipher.decrypt('mfqrg', '')
