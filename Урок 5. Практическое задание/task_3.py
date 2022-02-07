"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""


from collections import deque
from timeit import timeit

# Заполнение списка
some_lst = [i for i in range(10 ** 5)]

# Заполнение очереди
some_deque = deque([i for i in range(10 ** 5)])

n = 10 ** 4


# append
def append_list(some_lst):
    for i in range(n):
        some_lst.append(i)
    return some_lst


# append
def append_deque(some_deque):
    for i in range(n):
        some_deque.append(i)
    return some_deque


# pop
def pop_list(some_lst):
    for i in range(n):
        some_lst.pop()
    return some_lst


# pop
def pop_deque(some_deque):
    for i in range(n):
        some_deque.pop()
    return some_deque


# extend
def extend_list(some_lst):
    for i in range(n):
        some_lst.extend([1, 2, 3])
    return some_lst


# extend
def extend_list(some_deque):
    for i in range(n):
        some_deque.extend([1, 2, 3])
    return some_deque



# insert
def appendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, i)
    return some_lst


# appendleft
def appendleft_deque(some_deque):
    for i in range(n):
        some_deque.appendleft(i)
    return some_deque


# pop
def popleft_list(some_lst):
    for i in range(n):
        some_lst.pop(i)
    return some_lst


# popleft
def popleft_deque(some_deque):
    for i in range(n):
        some_deque.popleft()
    return some_deque


# insert
def extendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, [1, 2, 3])
    return some_lst


# extend
def extendleft_deque(some_deque):
    for i in range(n):
        some_deque.extendleft([1, 2, 3])
    return some_deque



def get_elem_list(some_lst):
    for i in range(n):
        some_lst[i] = i
    return some_lst


def get_elem_deque(some_deque):
    for i in range(n):
        some_deque[i] = i
    return some_deque

