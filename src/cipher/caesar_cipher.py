from .cipher_strategy import CipherStrategy
from .char_functions import shift_char


def char_frequency(data: str) -> dict:
    """
    Возвращает частоту встречаемости символов в тексте.

    Args:
        data (str): Текст для анализа.

    Returns:
        dict: Словарь с частотами символов.
    """

    data_lower = data.lower()

    frequency = {}
    for char in data_lower:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency


class CaesarCipher(CipherStrategy):
    """
    Класс для шифрования и дешифрования данных с помощью шифра Цезаря.
    Реализует интерфейс CipherStrategy.
    """

    @staticmethod
    def encrypt(data: str, key: int) -> str:
        """
        Шифрование данных алгоритмом Цезаря.

        Args:
            data (str): Данные для шифрования.
            key (int): Ключ шифрования (сдвиг).

        Returns:
            str: Зашифрованные данные.
        """

        return CaesarCipher._shift_text(data, key)

    @staticmethod
    def decrypt(data: str, key: int) -> str:
        """
        Дешифрование данных алгоритмом Цезаря.

        Args:
            data (str): Зашифрованные данные для дешифрования.
            key (int): Ключ шифрования (сдвиг).

        Returns:
            str: Расшифрованные данные.
        """

        return CaesarCipher._shift_text(data, -key)

    @staticmethod
    def break_cipher(data: str) -> str:
        """
        Взлом шифра Цезаря методом частотного анализа.

        Args:
            data (str): Зашифрованные данные для взлома.

        Returns:
            str: Вероятная расшифровка.
        """

        frequency = char_frequency(data)
        if not frequency:
            return data

        most_common = max(frequency, key=frequency.get)

        expected = 'e'  # Самая часто встречаемая буква в английском языке
        alphabet_size = 26
        if 'а' <= most_common <= 'я':
            expected = 'о'  # Самая часто встречаемая буква в русском языке
            alphabet_size = 32

        key = (ord(most_common) - ord(expected)) % alphabet_size
        return CaesarCipher.decrypt(data, key)

    @staticmethod
    def _shift_text(data: str, key: int) -> str:
        """
        Проводит сдвиг символов в тексте.

        Args:
            data (str): Исходные данные.
            key (int): Величина сдвига.

        Returns:
            str: Результат сдвига символов.
        """

        result = []
        for char in data:
            result.append(shift_char(char, key))
        return ''.join(result)
