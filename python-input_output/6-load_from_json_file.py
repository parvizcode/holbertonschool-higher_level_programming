#!/usr/bin/python3
"""
Bu modül, JSON dosyasından Python objesi oluşturan fonksiyonu içerir.
"""

import json


def load_from_json_file(filename):
    """
    Verilen JSON dosyasını okuyup Python veri yapısına dönüştürür.

    Args:
        filename (str): JSON formatındaki dosya adı.

    Returns:
        object: Dosyada bulunan JSON objesinin Python karşılığı.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
