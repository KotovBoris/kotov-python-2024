from .caesar_cipher import CaesarCipher
from .vigenere_cipher import VigenereCipher
from .vernam_cipher import VernamCipher


class CipherFactory:
    """
    Фабричный класс для создания объектов шифрования.
    """

    @staticmethod
    def create_cipher(cipher_type: str):
        """
        Создает объект шифрования в зависимости от типа шифра.

        Args:
            cipher_type (str): Тип шифра ('caesar', 'vigenere' или 'vernam').

        Returns:
            CipherStrategy: Объект шифрования, реализующий интерфейс CipherStrategy.

        Raises:
            ValueError: Если передан неподдерживаемый тип шифра.
        """
        cipher_type = cipher_type.lower()
        if cipher_type == 'caesar':
            return CaesarCipher()
        elif cipher_type == 'vigenere':
            return VigenereCipher()
        elif cipher_type == 'vernam':
            return VernamCipher()
        else:
            raise ValueError(f'Unsupported cipher type: {cipher_type}')