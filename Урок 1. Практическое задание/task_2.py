"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

from random import randit


# Сложность первого алгоритма O(n^2)
def list_min_f(lst):
    for i in lst:
        is_min = True
        for j in lst:
            if i > j:
                is_min = False
        if is_min:
            return i


# Сложность второго алгоритма O(n)
def list_min_s(lst):
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value


lst1 = [randit(0, 100 ) for i in range(20)]
print(lst1)
print(list_min_s(lst1))
print(list_min_f(lst1))




