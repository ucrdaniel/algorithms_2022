"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from time import time

n = 10 ** 5


def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} '
              f'составило {end - start}')
        return result

    return timer


@time_decorator
def fill_list_append(lst, num):
    """Заполняет список"""
    for i in range(num):
        lst.append(i)  # Сложность операции O(1)


some_list = []
fill_list_append(some_list, n)
print('_' * 100)


@time_decorator
def fill_list_insert(lst, num):
    """Заполняет список"""
    for i in range(num):
        lst.insert(0, i)  # Сложность операции O(n)


some_list = []
fill_list_insert(some_list, n)
print('_' * 100)


@time_decorator
def fill_dict(dct, num):
    """Заполняет словарь"""
    for i in range(num):  # Операция заполнения словаря занимает меньше
        # времени, так как он представляет из себя хеш-таблицу
        dct[i] = i


some_dict = {}
fill_dict(some_dict, n)
print('_' * 100)



@time_decorator
def change_list(lst):
    for i in range(10000):
        lst.pop(i)
    for j in range(1000):
        lst[j] = lst[j + 1]


change_list(some_list)
print('_' * 100)




@time_decorator
def change_dict(dct):
    for i in range(10000):
        dct.pop(i)
    for j in range(1001, 2002):
        dct[j] = 'fill'


change_dict(some_dict)
print('_' * 100)

