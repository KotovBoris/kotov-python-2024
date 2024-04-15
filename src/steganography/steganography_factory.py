from .bmp_steganography import BMPSteganography


class SteganographyFactory:
    """
    Фабричный класс для создания объектов стеганографии.
    """

    @staticmethod
    def create_steganography(image_format: str):
        """
        Создает объект стеганографии в зависимости от формата изображения.

        Args:
            image_format (str): Формат изображения ('bmp', 'png' или 'jpg').

        Returns:
            Steganography: Объект стеганографии, реализующий интерфейс Steganography.

        Raises:
            ValueError: Если передан неподдерживаемый формат изображения.
        """
        image_format = image_format.lower()
        if image_format == 'bmp' or image_format == 'png':
            return BMPSteganography()

        else:
            raise ValueError(f'Unsupported image format: {image_format}')