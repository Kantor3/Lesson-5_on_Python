"""
Задача 35
В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
Найдите это число.
test_data = [["3 4 5 6 7 9 10 11 12 14", 8],
             ["3 4 6 7 8 9 10 12 13", 5],
             ["1 3 5 7", 2]]
"""


def get_data_file(name_fil):
    with open(name_fil, 'r', encoding='utf8') as f:
        l_str = f.readlines()
    return l_str


'''
=====================================================================================
Основное тело программы:
# ====================================================================================
'''

print('Ищем недостающие элементы в последовательностях чисел, загруженных из файла.'
      '\nНедостающие элементы указаны через стрелку (->):')

name_file = "file_35.txt"
l_series = map(lambda el: el.replace("\n", ""), get_data_file(name_file))

curr_sers = lambda lst: list(map(int, lst.split()))
recurrent = lambda els: 0 if els[1] == els[0] + 1 else els[0] + 1
nearby_el = lambda lst: map(recurrent, zip(lst[:-1], lst[1:]))
els_misng = lambda lst: tuple(filter(lambda el: el, nearby_el(lst)))
missing = [f'{el} -> {els_misng(curr_sers(el))}' for el in l_series]

print(*missing, sep='\n')
