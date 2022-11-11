"""
Задача 36
Дан список чисел. Создайте список, в который попадают числа,
описывающие возрастающую последовательность.
Порядок элементов менять нельзя.
Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7]
test_data = [
[[1, 5, 2, 3, 4, 6, 1, 7], [1, 5, 6, 7]],
[[1, 2, 3, 4, 6, 1, 7], [1, 2, 3, 4, 6, 7]]
]
[1, 5, 6, 7]
[1, 2, 3, 4, 6, 7]
"""
import my_Lib as my
import random
from functools import reduce


# Выделение упорядоченной последовательности из исходной
def get_ordering(ser):
    red = reduce(lambda lst, el: lst + [el if el > abs(lst[-1]) else -abs(lst[-1])], ser, [0])
    return list(filter(lambda el: el >= 0, red[1:]))


'''
=====================================================================================
Основное тело программы:
# ====================================================================================
'''
print('Формируем возрастающую последовательность без изменения порядка следования в исходных данных')
el_max = 99
test_data = [[1, 5, 2, 3, 4, 6, 1, 7],
             [1, 2, 3, 4, 6, 1, 7]]

while True:
    series_size = my.get_InputNumber(0, txt='\nВведите число элементов исходной последовательности; '
                                            '\n0 - будут использованы тестовые', end='-')
    if my.check_exit(series_size):
        break

    l_series = [[random.randint(1, el_max) for _ in range(series_size)]] if series_size else test_data
    series_ord = map(get_ordering, l_series)
    res = [f'{init} => {out}' for init, out in zip(l_series, series_ord)]

    print('Результат формирования для заданных последовательностей:', *res, sep='\n')
