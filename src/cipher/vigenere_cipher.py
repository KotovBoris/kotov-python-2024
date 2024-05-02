from .cipher_strategy import CipherStrategy
from .char_functions import shift_char, alphabet_index


class VigenereCipher(CipherStrategy):
    """
    Класс для шифрования и дешифрования данных с помощью алгоритма Виженера.
    Реализует интерфейс CipherStrategy.
    """

    @staticmethod
    def encrypt(data: str, key: str) -> str:
        """
        Шифрование данных алгоритмом Виженера.

        Args:
            data (str): Данные для шифрования.
            key (str): Ключ шифрования (строка).

        Returns:
            str: Зашифрованные данные.
        """
        return VigenereCipher._translate(data, key, 'encrypt')

    @staticmethod
    def decrypt(data: str, key: str) -> str:
        """
        Дешифрование данных алгоритмом Виженера.

        Args:
            data (str): Зашифрованные данные для дешифрования.
            key (str): Ключ шифрования (строка).

        Returns:
            str: Расшифрованные данные.
        """
        return VigenereCipher._translate(data, key, 'decrypt')

    @staticmethod
    def _translate(data: str, key: str, method: str) -> str:
        """
        Перевод текста с использованием ключевого слова по алгоритму Виженера.

        Args:
            data (str): Исходный текст.
            key (str): Ключевое слово.
            method (str): 'encrypt' или 'decrypt', в зависимости от требуемого действия.

        Returns:
            str: Преобразованный текст.

        Raises:
            ValueError: Пустой ключ.
        """
        if len(key) == 0:
            raise ValueError("Empty key")

        translated = []

        for i in range(len(data)):
            key_index = alphabet_index(key[i % len(key)])
            new_char = shift_char(data[i], key_index if method == 'encrypt' else -key_index)
            translated.append(new_char)

        return ''.join(translated)
