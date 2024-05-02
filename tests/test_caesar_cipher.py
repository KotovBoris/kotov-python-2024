import unittest
from src.cipher.caesar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(CaesarCipher.encrypt('abc', '1'), 'bcd')
        self.assertEqual(CaesarCipher.encrypt('ABC', '1'), 'BCD')

    def test_decrypt_basic(self):
        self.assertEqual(CaesarCipher.decrypt('bcd', '1'), 'abc')
        self.assertEqual(CaesarCipher.decrypt('BCD', '1'), 'ABC')

    def test_encrypt_with_large_key(self):
        self.assertEqual(CaesarCipher.encrypt('abc', '27'), 'bcd')
        self.assertEqual(CaesarCipher.encrypt('ABC', '27'), 'BCD')

    def test_decrypt_with_large_key(self):
        self.assertEqual(CaesarCipher.decrypt('bcd', '27'), 'abc')
        self.assertEqual(CaesarCipher.decrypt('BCD', '27'), 'ABC')

    def test_encrypt_with_negative_key(self):
        self.assertEqual(CaesarCipher.encrypt('bcd', '-1'), 'abc')
        self.assertEqual(CaesarCipher.encrypt('BCD', '-1'), 'ABC')

    def test_decrypt_with_negative_key(self):
        self.assertEqual(CaesarCipher.decrypt('abc', '-1'), 'bcd')
        self.assertEqual(CaesarCipher.decrypt('ABC', '-1'), 'BCD')

    def test_break_cipher_simple(self):
        encrypted = CaesarCipher.encrypt('theee quick brown fox jumps oveeer the lazy dog', '5')
        self.assertIn('the', CaesarCipher.break_cipher(encrypted))

    def test_break_cipher_no_alpha(self):
        plaintext = '365198!-+-4537/][````'
        encrypted = CaesarCipher.encrypt(plaintext, '5')
        self.assertEqual(plaintext, CaesarCipher.break_cipher(encrypted))

    def test_encrypt_with_non_alpha_characters(self):
        self.assertEqual(CaesarCipher.encrypt('hello, world!', '3'), 'khoor, zruog!')
        self.assertEqual(CaesarCipher.encrypt('123', '3'), '123')
        self.assertEqual(CaesarCipher.encrypt('!!!', '3'), '!!!')

    def test_decrypt_with_non_alpha_characters(self):
        self.assertEqual(CaesarCipher.decrypt('khoor, zruog!', '3'), 'hello, world!')
        self.assertEqual(CaesarCipher.decrypt('123', '3'), '123')
        self.assertEqual(CaesarCipher.decrypt('!!!', '3'), '!!!')

    def test_encrypt_empty_string(self):
        self.assertEqual(CaesarCipher.encrypt('', '3'), '')

    def test_decrypt_empty_string(self):
        self.assertEqual(CaesarCipher.decrypt('', '3'), '')

    def test_encrypt_mixed_characters(self):
        self.assertEqual(CaesarCipher.encrypt('Python 3.8!', '5'), 'Udymts 3.8!')

    def test_decrypt_mixed_characters(self):
        self.assertEqual(CaesarCipher.decrypt('Udymts 3.8!', '5'), 'Python 3.8!')

    def test_encrypt_decrypt_russian_with_non_alpha(self):
        data = "Привет, мир! 123"
        key = 5
        encrypted = CaesarCipher.encrypt(data, key)
        self.assertEqual(encrypted, "Фхнзкч, снх! 123")
        decrypted = CaesarCipher.decrypt(encrypted, key)
        self.assertEqual(decrypted, data)

    def test_break_cipher_russian_mixed_case(self):
        data = "тыжщэ жъж юуйц надлйц хсбочфитлйц вфмппппппл, еб гьржк шбя! 123"
        decrypted = CaesarCipher.break_cipher(data)
        self.assertEqual(decrypted, "съешь еще этих мягких французских булоооооок, да выпей чаю! 123")
