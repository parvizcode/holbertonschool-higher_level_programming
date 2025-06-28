#!/usr/bin/python3
"""
Bu modül, Python objesini JSON formatında bir dosyaya yazan fonksiyonu içerir.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Verilen Python objesini JSON olarak belirtilen dosyaya yazar.

    Args:
        my_obj: JSON'a dönüştürülebilen Python objesi.
        filename (str): Yazılacak dosyanın adı.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
