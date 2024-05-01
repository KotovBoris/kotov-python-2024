![Coverage](./coverage.svg)

# Описание проекта:

Консольное приложение, способное шифровать/дешифровать текст.

# Стек технологий и используемые библиотеки:

- Python 3
- Библиотека argparse для обработки аргументов командной строки
- Библиотека Pillow для работы с изображениями

# Реализуемый функционал:

- Шифрование и дешифрование файлов различными методами (выбор режима и передача путей к файлам реализована с помощью аргументов командной строки)
  Поддерживаемые алгоритмы шифрования:
  1) **Шифр Цезаря:** Простой алгоритм сдвига символов на определенное количество позиций.
  2) **Шифр Виженера:** Полиалфавитный шифр, основанный на использовании ключевого слова для определения сдвига каждого символа исходного текста.
  3) **Шифр Вернама:** Симметричный метод шифрования, использующий операцию XOR и ключ, имеющий ту же длину, что и исходный текст.
  
- Автоматический взлом шифра Цезаря методами частотного анализа

- Стеганография: внедрение и извлечение текста в/из картинки формата bmp, jpg, png (пути к исходному и итоговому изображениям передаются в качестве аргументов командной строки)

# Архитектура:

### Алгоритм работы приложения:
1. Ввод аргументов командной строки
2. Проверка корректности аргументов (существование файлов, выбор режима работы)
3. В зависимости от выбранного режима работы выполняется соответствующая операция: шифрование, дешифрование или стеганография.
4. Результат записывается в файл

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
- `embed_text(image_path: str, text: str) -> str`: Внедрение текста в BMP/PNG изображение.
- `extract_text(image_path: str) -> str`: Извлечение текста из BMP/PNG изображения.

#### `JPGSteganography`

- **Наследуется от `Steganography`.**
- `embed_text(image_path: str, text: str) -> str`: Внедрение текста в JPG изображение.
- `extract_text(image_path: str) -> str`: Извлечение текста из JPG изображения.

# Покрытие тестами

### Coverage report: 99%

[coverage.py v7.4.4](https://coverage.readthedocs.io/en/7.4.4), created at 2024-04-18 04:08 +0300

| Module                                                                                         | statements | missing | excluded | coverage |
| ---------------------------------------------------------------------------------------------- | ---------- | ------- | -------- | -------- |
| [src\__init__.py](d_145eef247bfb46b6___init___py.html)                                         | 0          | 0       | 0        | 100%     |
| [src\cipher\__init__.py](d_4964dd438bd0ea48___init___py.html)                                  | 0          | 0       | 0        | 100%     |
| [src\cipher\caesar_cipher.py](d_4964dd438bd0ea48_caesar_cipher_py.html)                        | 35         | 0       | 0        | 100%     |
| [src\cipher\char_functions.py](d_4964dd438bd0ea48_char_functions_py.html)                      | 12         | 0       | 0        | 100%     |
| [src\cipher\cipher_factory.py](d_4964dd438bd0ea48_cipher_factory_py.html)                      | 14         | 0       | 0        | 100%     |
| [src\cipher\cipher_strategy.py](d_4964dd438bd0ea48_cipher_strategy_py.html)                    | 10         | 2       | 0        | 80%      |
| [src\cipher\vernam_cipher.py](d_4964dd438bd0ea48_vernam_cipher_py.html)                        | 10         | 0       | 0        | 100%     |
| [src\cipher\vigenere_cipher.py](d_4964dd438bd0ea48_vigenere_cipher_py.html)                    | 19         | 0       | 0        | 100%     |
| [src\steganography\__init__.py](d_cfffa53b4a781d44___init___py.html)                           | 0          | 0       | 0        | 100%     |
| [src\steganography\bmp_steganography.py](d_cfffa53b4a781d44_bmp_steganography_py.html)         | 47         | 0       | 0        | 100%     |
| [src\steganography\jpg_steganography.py](d_cfffa53b4a781d44_jpg_steganography_py.html)         | 31         | 0       | 0        | 100%     |
| [src\steganography\steganography.py](d_cfffa53b4a781d44_steganography_py.html)                 | 10         | 2       | 0        | 80%      |
| [src\steganography\steganography_factory.py](d_cfffa53b4a781d44_steganography_factory_py.html) | 11         | 0       | 0        | 100%     |
| [tests\test_bmp_steganography.py](d_a44f0ac069e85531_test_bmp_steganography_py.html)           | 26         | 0       | 0        | 100%     |
| [tests\test_caesar_cipher.py](d_a44f0ac069e85531_test_caesar_cipher_py.html)                   | 55         | 0       | 0        | 100%     |
| [tests\test_char_functions.py](d_a44f0ac069e85531_test_char_functions_py.html)                 | 35         | 0       | 0        | 100%     |
| [tests\test_cipher_factory.py](d_a44f0ac069e85531_test_cipher_factory_py.html)                 | 18         | 0       | 0        | 100%     |
| [tests\test_jpg_steganography.py](d_a44f0ac069e85531_test_jpg_steganography_py.html)           | 22         | 0       | 0        | 100%     |
| [tests\test_steganography_factory.py](d_a44f0ac069e85531_test_steganography_factory_py.html)   | 18         | 0       | 0        | 100%     |
| [tests\test_vernam_cipher.py](d_a44f0ac069e85531_test_vernam_cipher_py.html)                   | 28         | 0       | 0        | 100%     |
| [tests\test_vigenere_cipher.py](d_a44f0ac069e85531_test_vigenere_cipher_py.html)               | 26         | 0       | 0        | 100%     |
| Total                                                                                          | 427        | 4       | 0        | 99%      |

[coverage.py v7.4.4](https://coverage.readthedocs.io/en/7.4.4), created at 2024-04-18 04:08 +0300

(в steganography.py и cipher_strategy.py по 80%, т.к. это абстрактные классы с pass-ами)
