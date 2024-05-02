import argparse
from cipher.cipher_factory import CipherFactory
from steganography.steganography_factory import SteganographyFactory


def create_parser() -> argparse.ArgumentParser:
    """
    Создает парсер аргументов командной строки.

    Returns:
        argparse.ArgumentParser: Парсер аргументов.
    """

    parser = argparse.ArgumentParser(description="Encrypt/Decrypt messages and perform steganography.")

    parser.add_argument('--mode', choices=['encrypt', 'decrypt', 'embed', 'extract'], required=True,
                        help='Mode of operation.')

    parser.add_argument('--method', choices=['caesar', 'vigenere', 'vernam'], help='Encryption method')
    parser.add_argument('--key', type=str,
                        help='Key to use for encryption/decryption. Optional for decrypting Caesar cipher.')

    parser.add_argument('--message', type=str, help='Text for encryption/embedding'
                                                    '(The file with the encryption text can be entered via --input)')

    parser.add_argument('--input', type=str, help='Path to the image for steganography or text file for encryption')
    parser.add_argument('--output', type=str, help='Output file or message result.')

    return parser


def encryption_way(args: argparse.Namespace) -> str:
    """
    Шифрование/дешифрование текста.

    Args:
        args (argparse.Namespace): Объект, содержащий аргументы командной строки.

    Returns:
        str: Результат шифрования/расшифрования.

    Raises:
        ValueError: Если аргументы не соответствуют требованиям.
    """
    cipher_factory = CipherFactory()
    cipher = cipher_factory.create_cipher(args.method)

    data = args.message
    if args.input is not None:
        with open(args.input, 'r') as f:
            data = f.read()

    if args.mode == 'encrypt':
        if not args.key:
            raise ValueError("No key provided")
        result = cipher.encrypt(data, args.key)

    elif args.mode == 'decrypt':
        if not args.key and args.method == 'caesar':
            print("No key provided, attempting to break Caesar cipher using frequency analysis...")
            result = cipher.break_cipher(data)

        elif not args.key:
            raise ValueError("No key provided")

        else:
            result = cipher.decrypt(data, args.key)

    return result


def steganography_way(args: argparse.Namespace) -> str:
    """
    Выполняет стеганографию: встраивание/извлечение текста из изображения.

    Args:
        args (argparse.Namespace): Аргументы командной строки.

    Returns:
        str: Извлеченный текст/путь к измененному изображению.
    """

    if not args.message:
        raise ValueError('No image provided')

    steg_factory = SteganographyFactory()
    steganography = steg_factory.create_steganography(args.method)

    if args.mode == 'embed':
        if not args.message:
            raise ValueError("Empty message")

        output_path = steganography.embed_text(args.input, args.message, args.output)
        print('New image:', output_path)

    elif args.mode == 'extract':
        result = steganography.extract_text(args.input)

    return result


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.mode in ['encrypt', 'decrypt']:
        result = encryption_way(args)
    else:
        result = steganography_way(args)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
    else:
        print(result)


if __name__ == "__main__":
    main()
