#!/usr/bin/python3
"""
Bu modül, verilen metni belirtilen dosyaya yazma işlemini gerçekleştirir.
"""


def write_file(filename="", text=""):
    """
    Verilen dosya adına, verilen metni yazar.

    Args:
        filename (str): Yazılacak dosyanın adı.
        text (str): Dosyaya yazılacak metin.

    Returns:
        int: Yazılan karakter sayısı.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
