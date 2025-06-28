#!/usr/bin/python3
"""
Bu modül, bir Python objesinin JSON string gösterimini dönen fonksiyonu içerir.
"""

import json


def to_json_string(my_obj):
    """
    Verilen Python objesinin JSON string karşılığını döner.

    Args:
        my_obj: JSON olarak dönüştürülebilecek herhangi bir Python objesi.

    Returns:
        str: Objeye ait JSON string gösterimi.
    """
    return json.dumps(my_obj)
