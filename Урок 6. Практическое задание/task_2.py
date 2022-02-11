"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""


from memory_profiler import profile


@profile
def wrapper(input_number):
    def func(numb, reversed_number=''):
        if numb == 0:
            return reversed_number
        else:
            digit = numb % 10
            return func(numb // 10, reversed_number + str(digit))

    return func(input_number)


number = 1234567890

print(f'Перевернутое число: {wrapper(number)}')