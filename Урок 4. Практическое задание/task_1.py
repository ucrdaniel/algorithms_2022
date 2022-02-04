"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


#упрощенный вид
#время выполнения сократилось из-за сокращения перебираемых элементов
def func_2(nums):
    new_arr = []
    for i in range(0, len(nums), 2):
        new_arr.append(i)
    return new_arr

"""
Замеры:
"""

# 10000
NUMS = [el for el in range(10000)]
print(
    timeit(
        "func_1(NUMS[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "func_2(NUMS[:])",
        globals=globals(),
        number=1000))


# 100000
NUMS = [el for el in range(100000)]
print(
    timeit(
        "func_1(NUMS[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "func_2(NUMS[:])",
        globals=globals(),
        number=1000))
