"""
Task-38_seminar.py:
-----------------
Задача 38.
Напишите программу, удаляющую из текста все слова, содержащие "абв".
test_data = [[["привет абв как абвышные дела?", "абв"], "привет как дела?"]]
"""
import my_Lib as my
from functools import reduce

is_fragment = lambda fr, s: s == s.replace(fr, '')

'''
=====================================================================================
Основное тело программы:
# ====================================================================================
'''
print('Удаляем из указанного текста все слова, содержжащие указанный фрагмент')
txt_test = 'привет абв как абвышные дела? абв'
fragment_clr = 'абв'

while True:
    txt, fragment = my.get_InputTuple('Введите любой текст (или "*" для тестирования)',
                                      'Введите фрагмент, слова содержащие который, нужно удалить',
                                      type_input=str, end='-')
    if txt is None and my.check_exit(txt):
        break

    if txt == "*":  txt = txt_test
    else:           fragment_clr = fragment

    txt_cleared = ' '.join(list(filter(lambda word: is_fragment(fragment_clr, word), txt.split())))
    print(f'\nИсходный текст -> "{txt}"',
          f'Фрагмент для поиска и удаления слов -> "{fragment_clr}"',
          f'Очищенный текст -> "{txt_cleared}"', '', sep='\n')

exit()

"""
Task-38_seminar.py:
-----------------
Задача 38 - измененная версия.
Напишите программу, удаляющую из текста все фрагменты строк, заданные списком.
Пример:
test_data = ["Шольц не очень ливерная колбаса или ливерная колбаса, но не очень", ["ливерная", "не"], 
            "Шольц очень колбаса или колбаса, но очень"]]
"""

# Наличие указанного фрагмента в списке для удаления
is_fragments = lambda curr_fr, l_fr: len(list(filter(lambda elem: curr_fr == elem, l_fr)))

'''
=====================================================================================
Основное тело программы:
Решение реализовано без использования встроенных средств, таких как:
res = txt.replace(clear_fragment, '')
res = ''.join(txt.split(clear_fragment))
# ====================================================================================
'''
print('Удаляем из указанного текста все заданные фрагменты')
test_txt = 'привет абв как абвышные дела? абв'
clr_fragments = ['абв']

while True:
    params = my.get_InputTuple('Введите любой текст (или "*" для тестирования)',
                               'Введите через запятую фрагменты, которые нужно удалить по всему тексту',
                               type_input=str, end='-')

    txt, fragments = (params + (None,))[:2]  # временная мера, пока библиотека my_lib не обновилась

    if txt is None and my.check_exit(txt):
        break

    if txt == "*":
        txt = test_txt
    else:
        clr_fragments = fragments.split(',')

    maxlen_fragment = reduce(lambda max_len, el: max(max_len, len(el)), clr_fragments, 0)
    txt_cleared = ""
    txt_rest = txt

    while len(txt_rest):
        curr_fragment = ''
        for el in txt_rest:
            curr_fragment += el
            if is_fragments(curr_fragment, clr_fragments):
                txt_rest = txt_rest[len(curr_fragment):]
                break
            elif len(curr_fragment) == maxlen_fragment:
                txt_cleared += curr_fragment[0]
                txt_rest = txt_rest[1:]
                break
        else:
            break

    txt_cleared += txt_rest

    print(f'\nИсходный текст -> "{txt}"',
          f'Фрагменты для очистки -> "{clr_fragments}"',
          f'Очищенный текст -> "{txt_cleared}"', '', sep='\n')
