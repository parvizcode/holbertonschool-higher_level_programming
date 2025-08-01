#!/usr/bin/python3
"""
Pascal üçgeni fonksiyonu
"""


def pascal_triangle(n):
    """
    n satırlık Pascal üçgenini liste olarak döner.

    Args:
        n (int): Satır sayısı

    Returns:
        list[list[int]]: Pascal üçgeni
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
