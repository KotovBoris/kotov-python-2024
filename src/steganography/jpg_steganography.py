from .steganography import Steganography
from PIL import Image


class JPGSteganography(Steganography):
    """
    Класс для стеганографии в JPG изображениях.
    """

    @staticmethod
    def embed_text(image_path: str, text: str, output_path: str = None) -> str:
        """
        Внедрение текста в JPG изображение.

        Args:
            image_path (str): Путь к исходному изображению.
            text (str): Текст для внедрения.
            output_path (str, optional): Путь для сохранения изображения с внедренным текстом.
                Если не указан, то используется путь исходного изображения с суффиксом "_stego".

        Returns:
            str: Путь к изображению с внедренным текстом.
        """

        if output_path is None:
            output_path = f"{image_path.split('.')[0]}_stego.jpg"

        image = Image.open(image_path)
        message_bytes = text.encode('utf-8')
        exif_data = image.getexif()

        tag_id = None
        for i in range(65000, 66000):
            if i not in exif_data:
                tag_id = i
                break

        exif_data[tag_id] = message_bytes
        image.save(output_path, exif=exif_data)

        return output_path

    @staticmethod
    def extract_text(image_path: str) -> str:
        """
        Извлечение текста из JPG изображения.

        Args:
            image_path (str): Путь к изображению с внедренным текстом.

        Returns:
            str: Извлеченный текст.
        """
        image = Image.open(image_path)
        exif_data = image.getexif()

        message_bytes = None
        for tag_id in exif_data:
            if 65000 <= tag_id <= 66000:
                message_bytes = exif_data[tag_id]
                break

        if message_bytes is not None:
            message = message_bytes.decode('utf-8')
            return message
        else:
            return ''
