import unittest
from src.cipher.cipher_factory import CipherFactory
from src.cipher.caesar_cipher import CaesarCipher
from src.cipher.vigenere_cipher import VigenereCipher
from src.cipher.vernam_cipher import VernamCipher


class TestCipherFactory(unittest.TestCase):

    def test_create_caesar_cipher(self):
        cipher = CipherFactory.create_cipher('caesar')
        self.assertIsInstance(cipher, CaesarCipher)

    def test_create_vigenere_cipher(self):
        cipher = CipherFactory.create_cipher('vigenere')
        self.assertIsInstance(cipher, VigenereCipher)

    def test_create_vernam_cipher(self):
        cipher = CipherFactory.create_cipher('vernam')
        self.assertIsInstance(cipher, VernamCipher)

    def test_create_unsupported_cipher(self):
        with self.assertRaises(ValueError):
            CipherFactory.create_cipher('unsupported')
