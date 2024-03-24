# Описание проекта:

Консольное приложение, способное шифровать/дешифровать текст.
# Реализуемый функционал:

- Шифрование и дешифрование файлов шифрами Цезаря, Виженера и Вернама.
- Автоматический взлом шифра Цезаря методами частотного анализа
- Режим выбирается и путь к файлам передается с помощью аргументов командной строки.
- Стеганография: внедрение и извлечение текста в/из картинки формата bmp, jpg, png.
# Архитектура:
### Классы для шифрования:

#### `CipherStrategy` (абстрактный класс)

- `encrypt(data: str, key: str) -> str`: Абстрактный метод для шифрования данных.
- `decrypt(data: str, key: str) -> str`: Абстрактный метод для дешифрования данных.

#### `CipherFactory`

- `create_cipher(cipher_type: str) -> CipherStrategy`: Метод для создания объекта шифрования в зависимости от типа шифра.

#### `CaesarCipher`

- **Наследуется от `CipherStrategy`.**
- `encrypt(data: str, key: int) -> str`: Шифрование данных алгоритмом Цезаря.
- `decrypt(data: str, key: int) -> str`: Дешифрование данных алгоритмом Цезаря.
- `break_cipher(data: str) -> str`: Взлом шифра Цезаря методом частотного анализа.

#### `VigenereCipher`

- **Наследуется от `CipherStrategy`.**
- `encrypt(data: str, key: str) -> str`: Шифрование данных алгоритмом Виженера.
- `decrypt(data: str, key: str) -> str`: Дешифрование данных алгоритмом Виженера.

#### `VernamCipher`

- **Наследуется от `CipherStrategy`.**
- `encrypt(data: str, key: str) -> str`: Шифрование данных алгоритмом Вернама.
- `decrypt(data: str, key: str) -> str`: Дешифрование данных алгоритмом Вернама.

### Классы для стеганографии:

#### `Steganography` (абстрактный класс)

- `embed_text(image_path: str, text: str) -> str`: Абстрактный метод для внедрения текста в изображение.
- `extract_text(image_path: str) -> str`: Абстрактный метод для извлечения текста из изображения.

#### `SteganographyFactory`

- `create_steganography(image_format: str) -> Steganography`: Метод для создания объекта стеганографии в зависимости от формата изображения.

#### `BMPSteganography`

- **Наследуется от `Steganography`.**
- `embed_text(image_path: str, text: str) -> str`: Внедрение текста в BMP изображение.
- `extract_text(image_path: str) -> str`: Извлечение текста из BMP изображения.

#### `PNGSteganography`

- **Наследуется от `Steganography`.**
- `embed_text(image_path: str, text: str) -> str`: Внедрение текста в PNG изображение.
- `extract_text(image_path: str) -> str`: Извлечение текста из PNG изображения.

#### `JPGSteganography`

- **Наследуется от `Steganography`.**
- `embed_text(image_path: str, text: str) -> str`: Внедрение текста в JPG изображение.
- `extract_text(image_path: str) -> str`: Извлечение текста из JPG изображения.
