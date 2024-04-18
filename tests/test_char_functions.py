import unittest
from src.cipher.char_functions import alphabet, alphabet_index, shift_char


class TestCharFunctions(unittest.TestCase):
    def test_alphabet_english_lower(self):
        self.assertEqual(alphabet('a'), ('a', 26))
        self.assertEqual(alphabet('z'), ('a', 26))

    def test_alphabet_english_upper(self):
        self.assertEqual(alphabet('A'), ('A', 26))
        self.assertEqual(alphabet('Z'), ('A', 26))

    def test_alphabet_russian_lower(self):
        self.assertEqual(alphabet('а'), ('а', 32))
        self.assertEqual(alphabet('я'), ('а', 32))

    def test_alphabet_russian_upper(self):
        self.assertEqual(alphabet('А'), ('А', 32))
        self.assertEqual(alphabet('Я'), ('А', 32))

    def test_alphabet_other(self):
        self.assertEqual(alphabet('1'), ('1', 1))
        self.assertEqual(alphabet('#'), ('#', 1))

    def test_alphabet_index_english(self):
        self.assertEqual(alphabet_index('a'), 0)
        self.assertEqual(alphabet_index('z'), 25)

    def test_alphabet_index_russian(self):
        self.assertEqual(alphabet_index('а'), 0)
        self.assertEqual(alphabet_index('я'), 31)

    def test_shift_char_english(self):
        self.assertEqual(shift_char('a', 1), 'b')
        self.assertEqual(shift_char('z', 1), 'a')
        self.assertEqual(shift_char('A', 26), 'A')

    def test_shift_char_russian(self):
        self.assertEqual(shift_char('а', 1), 'б')
        self.assertEqual(shift_char('я', 1), 'а')
        self.assertEqual(shift_char('А', 32), 'А')

    def test_shift_char_with_large_key(self):
        self.assertEqual(shift_char('a', 52), 'a')  # English loop
        self.assertEqual(shift_char('а', 64), 'а')  # Russian loop
