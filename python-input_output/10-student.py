#!/usr/bin/python3
"""
Student sınıfı, isteğe bağlı olarak attribute filtresi ile sözlük döndürür.
"""


class Student:
    """ Öğrenci sınıfı """

    def __init__(self, first_name, last_name, age):
        """ Nesne örnekleme

        Args:
            first_name (str): Ad
            last_name (str): Soyad
            age (int): Yaş
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
