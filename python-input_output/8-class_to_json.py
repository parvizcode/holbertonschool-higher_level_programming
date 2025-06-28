#!/usr/bin/python3
"""
Bu modül, verilen objenin __dict__ özniteliğini döner,
objedeki tüm nitelikler JSON uyumlu basit veri tiplerinden oluşur.
"""


def class_to_json(obj):
    """
    Bir sınıf örneğinin sözlük temsili (JSON uyumlu) döner.

    Args:
        obj: Sınıf örneği (instance)

    Returns:
        dict: Objeye ait attribute'ların isim ve değerlerini içeren sözlük.
    """
    return obj.__dict__.copy()
