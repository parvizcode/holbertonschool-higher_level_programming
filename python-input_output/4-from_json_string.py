#!/usr/bin/python3
"""
Bu modül, JSON stringini Python objesine dönüştüren fonksiyonu içerir.
"""

import json


def from_json_string(my_str):
    """
    Verilen JSON stringini Python veri yapısına dönüştürür.

    Args:
        my_str (str): JSON formatında bir string.

    Returns:
        object: JSON stringinin temsil ettiği Python veri yapısı.
    """
    return json.loads(my_str)
