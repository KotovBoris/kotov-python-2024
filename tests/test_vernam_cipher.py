import unittest
from src.cipher.vernam_cipher import VernamCipher


class TestVernamCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        plaintext = "Hello, World!"
        key = "key"
        ciphertext = VernamCipher.encrypt(plaintext, key)
        decrypted_text = VernamCipher.decrypt(ciphertext, key)
        self.assertEqual(decrypted_text, plaintext)

    def test_encrypt_with_long_key(self):
        plaintext = "Hello, World!"
        key = "thisisalongkey"
        ciphertext = VernamCipher.encrypt(plaintext, key)
        decrypted_text = VernamCipher.decrypt(ciphertext, key)
        self.assertEqual(decrypted_text, plaintext)

    def test_encrypt_with_unicode(self):
        plaintext = "Привет, мир!"
        key = "key"
        ciphertext = VernamCipher.encrypt(plaintext, key)
        decrypted_text = VernamCipher.decrypt(ciphertext, key)
        self.assertEqual(decrypted_text, plaintext)

    def test_decrypt_with_wrong_key(self):
        plaintext = "Hello, World!"
        key = "key"
        ciphertext = VernamCipher.encrypt(plaintext, key)
        wrong_key = "wrongkey"
        decrypted_text = VernamCipher.decrypt(ciphertext, wrong_key)
        self.assertNotEqual(decrypted_text, plaintext)
