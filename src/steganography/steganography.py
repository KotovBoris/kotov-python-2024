from abc import ABC, abstractmethod


class Steganography(ABC):
    """
    Абстрактный базовый класс для стеганографии.
    Определяет общий интерфейс для внедрения и извлечения текста в/из изображений.
    """

    @staticmethod
    @abstractmethod
    def embed_text(image_path: str, text: str) -> str:
        """
        Абстрактный метод для внедрения текста в изображение.

        Args:
            image_path (str): Путь к изображению, в которое будет внедрен текст.
            text (str): Текст для внедрения.

        Returns:
            str: Путь к изображению с внедренным текстом.
        """
        pass

    @staticmethod
    @abstractmethod
    def extract_text(image_path: str) -> str:
        """
        Абстрактный метод для извлечения текста из изображения.

        Args:
            image_path (str): Путь к изображению, из которого нужно извлечь текст.

        Returns:
            str: Извлеченный текст.
        """
        pass