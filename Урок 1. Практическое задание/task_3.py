"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, наj пример, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

from random import randit


# Первый вариант N(nlog(n))

def sorted_1(base_company):
    list_from_dict = list(base_company.items())
    list_from_dict.sort(key=lambda i: i[1], reverse=True)
    for i in range(3):
        print(f"{list_from_dict[i][0]}: {list_from_dict[i][1]}")


# Второй вариант O(n)
def sorted_2(base_company):
    input_max = {}
    list_d = dict(base_company)
    for i in range(3):
        maximum = max(lsit_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]


sorted_1(base_company)
sorted_2(base_company)



