from .steganography import Steganography
from PIL import Image


class BMPSteganography(Steganography):
    """
    Класс для стеганографии в BMP изображениях.
    """

    @staticmethod
    def embed_text(image_path: str, text: str, output_path: str = None) -> str:
        """
        Внедрение текста в BMP изображение.

        Args:
            image_path (str): Путь к исходному изображению.
            text (str): Текст для внедрения.
            output_path (str, optional): Путь для сохранения изображения с внедренным текстом.
                Если не указан, то используется путь исходного изображения с суффиксом "_stego".

        Returns:
            str: Путь к изображению с внедренным текстом.
        """
        image = Image.open(image_path)
        width, height = image.size

        text += chr(0)
        binary_text = ''.join(format(ord(char), '08b') for char in text)

        max_bytes = width * height * 3 // 8
        if len(binary_text) > max_bytes:
            raise ValueError("Недостаточно места в изображении для внедрения текста.")

        data = list(image.getdata())
        data_iterator = iter(data)
        modified_data = []

        for i in range(0, len(binary_text), 3):
            pixel = list(next(data_iterator))

            for j in range(3):
                if i + j < len(binary_text):
                    bit = binary_text[i + j]
                    if bit == '0':
                        pixel[j] &= ~1
                    else:
                        pixel[j] |= 1

            modified_data.append(tuple(pixel))

        modified_data.extend(data_iterator)

        output_image = Image.new(image.mode, image.size)
        output_image.putdata(modified_data)

        if output_path is None:
            output_path = f"{image_path.split('.')[0]}_stego.{image_path.split('.')[-1]}"

        output_image.save(output_path)

        return output_path

    @staticmethod
    def extract_text(image_path: str) -> str:
        """
        Метод для извлечения текста из BMP изображения.

        Args:
            image_path (str): Путь к BMP изображению с внедренным текстом.

        Returns:
            str: Извлеченный текст.
        """
        image = Image.open(image_path)

        binary_data = ''
        for pixel in image.getdata():
            r, g, b = pixel[:3]
            binary_data += str(r & 1) + str(g & 1) + str(b & 1)

        binary_blocks = [binary_data[i:i + 8] for i in range(0, len(binary_data), 8)]

        extracted_text = ''
        for block in binary_blocks:
            if len(block) == 8:
                char = chr(int(block, 2))
                if char == chr(0):
                    break
                extracted_text += char

        return extracted_text
