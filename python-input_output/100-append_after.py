#!/usr/bin/python3
"""
append_after fonksiyonu:
Belirli bir string içeren satırlardan sonra bir metin ekler.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Bir dosyada, search_string içeren her satırdan sonra new_string ekler.

    Args:
        filename (str): Dosya adı
        search_string (str): Aranacak string
        new_string (str): Eklenecek string
    """
    lines = []
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
