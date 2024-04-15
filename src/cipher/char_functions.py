def alphabet(char: str) -> tuple:
    """
    Определение алфавита и его размера по букве.

    Args:
        char (str): Буква.

    Returns:
        tuple: (начальный символ алфавита, размер алфавита)
    """
    if 'a' <= char.lower() <= 'z':
        return 'a' if char.islower() else 'A', 26

    if 'а' <= char.lower() <= 'я':
        return 'а' if char.islower() else 'А', 32

    return char, 1


def alphabet_index(char: str) -> int:
    """
    Получение индекса буквы в алфавите.

    Args:
        char (str): Буква.

    Returns:
        int: Индекс в алфавите.
    """

    return ord(char) - alphabet(char)[0]


def shift_char(char: str, key_index: int) -> str:
    """
    Сдвигает букву на указанное число позиций в алфавите.

    Args:
        char (str): Буква.
        key_index (int): Сдвиг.

    Returns:
        str: Сдвинутая буква.
    """
    start, alphabet_size = alphabet(char)

    new_pos = (ord(char) - ord(start) + key_index) % alphabet_size + ord(start)
    return chr(new_pos)
