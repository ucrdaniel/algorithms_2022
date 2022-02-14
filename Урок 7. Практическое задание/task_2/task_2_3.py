"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""


from random import randint
from timeit import timeit


def another_way(lst_obj):
    temp_list = lst_obj
    for i in range(len(lst_obj) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "another_way(orig_list[:])",
        globals=globals(),
        number=100))

m = 100
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "another_way(orig_list[:])",
        globals=globals(),
        number=100))

m = 1000
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "another_way(orig_list[:])",
        globals=globals(),
        number=100))
