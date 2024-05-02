from abc import ABC, abstractmethod


class CipherStrategy(ABC):
    """
    Абстрактный базовый класс для стратегии шифрования.

    Определяет общий интерфейс для шифрования и дешифрования данных различными алгоритмами.
    """

    @staticmethod
    @abstractmethod
    def encrypt(data: str, key: str) -> str:
        """
        Абстрактный метод для шифрования данных.

        Args:
            data (str): Исходные данные для шифрования.
            key (str): Ключ для шифрования.

        Returns:
            str: Зашифрованные данные.
        """
        pass

    @staticmethod
    @abstractmethod
    def decrypt(data: str, key: str) -> str:
        """
        Абстрактный метод для дешифрования данных.

        Args:
            data (str): Зашифрованные данные для дешифрования.
            key (str): Ключ для дешифрования.

        Returns:
            str: Расшифрованные данные.
        """
        pass
