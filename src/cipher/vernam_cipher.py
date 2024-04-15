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

        Raises:
            ValueError: Если передан ключ неверной длины.
        """

        if len(data) != len(key):
            raise ValueError("Длина ключа должна совпадать с длиной данных.")

        encrypted_data = ""
        for char, key_char in zip(data, key):
            encrypted_data += chr(ord(char) ^ ord(key_char))
        return encrypted_data

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
