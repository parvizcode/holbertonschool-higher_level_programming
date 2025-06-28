#!/usr/bin/python3
"""
Student sınıfı tanımı ve JSON uyumlu sözlük çıktısı metodu.
"""


class Student:
    """ Öğrenci sınıfı """

    def __init__(self, first_name, last_name, age):
        """ Nesne örnekleme (init)

        Args:
            first_name (str): Öğrencinin adı
            last_name (str): Öğrencinin soyadı
            age (int): Öğrencinin yaşı
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Nesnenin dictionary (JSON uyumlu) temsili.

        Returns:
            dict: Öğrencinin attribute'ları
        """
        return self.__dict__.copy()
