"""
Задача 35
В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
Найдите это число.
test_data = [["3 4 5 6 7 9 10 11 12", 8],
             ["3 4 6 7 8 9 10 11 12", 5],
             ["1 3", 2]]
"""
import my_Lib as my
from functools import reduce


def get_data_file(name_file):
    with open(name_file, 'r', encoding='utf8') as f:
        l_str = f.readlines()
    return l_str


def recurrent(els):
    el_i0, el_i1 = els
    print(el_i0, el_i1)
    return "" if el_i1 == el_i0 + 1 else el_i0 + 1


'''
=====================================================================================
Основное тело программы:
# ====================================================================================
'''

if __name__ == '__main__':

    print('Ищем недостающие элементы в последовательностях чисел, записанных в файле')

    name_file = "file_35.txt"
    l_series = list(map(lambda el: el.replace("\n", ""), get_data_file(name_file)))

    print(l_series, type(l_series))
    exit()

    els_missing = reduce(recurrent, zip(l_series[:-1], l_series[1:]))



