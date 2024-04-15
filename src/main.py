import argparse
from cipher.cipher_factory import CipherFactory
from steganography.steganography_factory import SteganographyFactory


def main():
    # print("test")

    parser = argparse.ArgumentParser(description="Encrypt/Decrypt messages and perform steganography.")

    # Общие аргументы для шифрования/дешифрования
    parser.add_argument('--mode', choices=['encrypt', 'decrypt', 'embed', 'extract'], required=True,
                        help='Mode of operation.')
    parser.add_argument('--method', choices=['caesar', 'vigenere', 'vernam', 'bmp', 'png'], required=True,
                        help='Encryption method or steganography type.')
    parser.add_argument('--key', type=str,
                        help='Key to use for encryption/decryption. Optional for decrypting Caesar cipher.')
    parser.add_argument('--input', type=str, required=True, help='Input file or message.')
    parser.add_argument('--output', type=str, help='Output file or message result.')

    args = parser.parse_args()

    if args.mode in ['encrypt', 'decrypt']:
        cipher_factory = CipherFactory()
        cipher = cipher_factory.create_cipher(args.method)

        with open(args.input, 'r') as f:
            data = f.read()

        if args.mode == 'encrypt':
            if not args.key:
                raise ValueError("Encryption requires a key.")
            encrypted_data = cipher.encrypt(data, int(args.key))
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(encrypted_data)
            else:
                print(encrypted_data)

        elif args.mode == 'decrypt':
            if not args.key and args.method == 'caesar':
                print("No key provided, attempting to break Caesar cipher using frequency analysis...")
                decrypted_data = cipher.break_cipher(data)
            elif not args.key:
                raise ValueError("Decryption requires a key.")
            else:
                decrypted_data = cipher.decrypt(data, args.key)

            if args.output:
                with open(args.output, 'w') as f:
                    f.write(decrypted_data)
            else:
                print(decrypted_data)

    elif args.mode in ['embed', 'extract']:
        steg_factory = SteganographyFactory()
        steganography = steg_factory.create_steganography(args.method)

        if args.mode == 'embed':
            if not args.key:
                raise ValueError("Embedding text requires text to embed.")
            steganography.embed_text(args.input, args.key)

        elif args.mode == 'extract':
            extracted_text = steganography.extract_text(args.input)
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(extracted_text)
            else:
                print(extracted_text)


if __name__ == "__main__":
    main()
