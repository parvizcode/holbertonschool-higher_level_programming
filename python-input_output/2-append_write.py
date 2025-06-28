#!/usr/bin/python3
"""
Bu modül, verilen metni belirtilen dosyanın sonuna ekleyen fonksiyonu içerir.
"""


def append_write(filename="", text=""):
    """
    Verilen dosyanın sonuna verilen metni ekler.

    Args:
        filename (str): Yazılacak dosyanın adı.
        text (str): Dosyaya eklenecek metin.

    Returns:
        int: Eklenen karakter sayısı.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
