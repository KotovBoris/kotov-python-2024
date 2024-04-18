from .cipher_strategy import CipherStrategy


class VernamCipher(CipherStrategy):
    """
    Класс для шифрования и дешифрования данных с помощью алгоритма Вернама.
    Реализует интерфейс CipherStrategy.
    """

    @staticmethod
    def encrypt(data: str, key: str) -> str:
        """
        Шифрование данных алгоритмом Вернама.

        Args:
            data (str): Исходные данные для шифрования.
            key (str): Ключ для шифрования.

        Returns:
            str: Зашифрованные данные.
        """

        extended_key = (key * (len(data) // len(key) + 1))[:len(data)]
        ciphertext = ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(data, extended_key))

        return ciphertext

    @staticmethod
    def decrypt(data: str, key: str) -> str:
        """
        Дешифрование данных алгоритмом Вернама.

        Args:
            data (str): Зашифрованные данные для дешифрования.
            key (str): Ключ для дешифрования.

        Returns:
            str: Расшифрованные данные.

        Raises:
            ValueError: Если передан ключ неверной длины.
        """

        return VernamCipher.encrypt(data, key)
