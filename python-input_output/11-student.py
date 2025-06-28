#!/usr/bin/python3
"""
Student sınıfı, to_json ve reload_from_json metodları ile
nesne serileştirme ve tekrar yükleme sağlar.
"""


class Student:
    """ Öğrenci sınıfı """

    def __init__(self, first_name, last_name, age):
        """ Nesne örnekleme

        Args:
            first_name (str): Öğrencinin adı
            last_name (str): Öğrencinin soyadı
            age (int): Öğrencinin yaşı
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Nesnenin sözlük temsili.

        Args:
            attrs (list, optional): Alınacak attribute isimleri listesi.
                                    None ise tüm attribute'lar döner.

        Returns:
            dict: İstenen attribute'lar ile sözlük.
        """
        if attrs is None:
            return self.__dict__.copy()

        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result

    def reload_from_json(self, json):
        """
        Nesnenin tüm attribute'larını verilen sözlükle günceller.

        Args:
            json (dict): Attribute isimleri ve değerlerini içeren sözlük.
        """
        for key, value in json.items():
            setattr(self, key, value)
