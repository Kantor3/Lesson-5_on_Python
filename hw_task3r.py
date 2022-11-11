"""
Задача 3.
Создайте программу для игры в ""Крестики-нолики"".
"""
# import copy                         # st = copy.deepcopy(board_status)
import random
from functools import reduce
import my_Lib as myl

signs = {0: '.', 1: 'x', -1: 'o'}  # словарь соответствия кодов и значков на игровом поле

# обращение к реверсному словарю
dict_rev = lambda dic, key: dict([(v, k) for k, v in dic.items()])[key]


# 3. Инициация и старт игры:
#    Определить random кто начинает и сообщить об этом и о формате
#    ввода своего хода. Формат ввода: [r][c], например "12" - сделать
#    ход на поле, находящееся на пересечении 1-й строки и 2-го столбца
#    (как показно на рис.)
def init_game(my_number, size):
    global signs
    # signs = {0: '.', 1: 'x', -1: 'o'}
    prime_player = random.randint(1, 2)
    n_pl, win_pl1, win_pl2, board_st = 0, 0, 0, [[0] * size for _ in range(size)]

    print(f'\nПервый ход за {"Вами" if prime_player == my_number else f"Игроком № {prime_player}"}')
    print(f'Формат ввода хода - число в виде [№ строки][№ колонки], например: 21')
    return prime_player, n_pl, win_pl1, win_pl2, board_st


# 4. Показать текущее состояние игры на доске
# stt = [[0, 0, -1, 1], [-1, 0, 0, 1], [0, 1, 0, 0], [0, -1, 1, 0]]
# [ell for el in stt for ell in el]
#     -----------
#     = 1   2   3
#     1 . | x | .
#     2 . | . | .
#     3 . | . | .
def show_board(board_st):

    print(f'signs -> {signs}')
    print(f'board_st -> {board_st}')

    print('-----------')
    print('= 1 2 3')
    board_sign = reduce(lambda lel, el: lel + [list(map(lambda l_el: signs[l_el], el))], board_st, [])
    for i, row in enumerate(board_sign):
        print(f'{i+1} ', end='')
        # print(*row, '\n')
        print(*row)


# 5. Получить ход у игрока, чей ход сейчас в таком виде: "Игрок-1 ->"
#    Проверить корректность хода. Если ход не корректен
#    (вне поля или поле уже занято) запросить ход повторно.
def get_move(player, board_st):
    av_moves = [10 * ell + el for ell in range(1, size_board + 1) for el in range(1, size_board + 1)]
    av_moves = tuple(filter(lambda m: not board_st[m // 10 - 1][m % 10 - 1], av_moves))
    while True:
        # Запрос хода
        # go = myl.get_InputNumber(av_moves, txt=f'Ход игрока {player} (доступные ходы: {av_moves})', end='-')
        # go = myl.get_InputNumber(av_moves, type_input=tuple, txt=f'Ход игрока {player}:', end='-')
        # if not (go is None) and board_st[go // 10 - 1][go % 10 - 1]:
        #     print(f'поле {go} занято, укажите другое поле.')
        #     continue
        # break
        go = myl.get_InputNumber(tuple(map(str, av_moves)), type_input=tuple, txt=f'Ход игрока {player}:', end='-')
        if go is None: break
        else: go = int(go)
        if board_st[go // 10 - 1][go % 10 - 1]:
            print(f'поле {go} занято, укажите другое поле.')
            continue
        return go  # отправка хода


# 6. Проверить игру на завершение (выигрыш одного из игроков или ничья)
# Выигрыш - наличия numb_XO идущих подряд ('x' или '0') по горизонтали, вертикали или на диагоналях
# Ничья - если нет выигрыша и все поля заняты
# Возврат:
# - None - если игра не завершена
# - 0 - если ничья
# - № игрока, который выиграл, если на доске есть выигрыш
def is_winnings(board_st):

    # Выигравший символ (код), было: cod_win = get_cod(stat, str_cod(numb))
    def get_cod(st, number):

        print(f'st = {st}')
        print(f'number = {number}')

        return [el[0] for el in st
                if str(list(signs.keys())[number]) * numb_XO
                in ''.join(map(str, el))]

    # транспонирование вложенного списка
    def trans(stt):
        stt_t = [ell for i in range(len(stt)) for el in board_st for ell in [el[i]]]
        return [reduce(lambda ell, el: ell + [el],
                       stt_t[i * size_board:][:size_board], []) for i in range(size_board)]

    # выделение элементов, находящихся на диагоналях вложенного списка
    def diagonals(st, b, sl):
        bb = int((1 - b) / 2)
        diagonal = lambda d: [[st[i - d * bb][(size_board - 1) * sl - (i + d * bb)] for i in range(d * b, size_board)]]
        return reduce(lambda st_d, j: st_d + diagonal(j), range(0, (size_board - numb_XO + 1) * b, 1), [])

    # Организация вложенных циклов, обеспечивающая возможность выхода из всех разом
    def multi_for(*ins):
        in1, in2, in3 = ins
        for i in in1:
            for j in in2:
                for k in in3: yield i, j, k

    # Проверяем наличие на доске ничьи
    if not filter(lambda el: not el, [ell for el in board_st for ell in el]):
        # return None  # на доске ничья!
        return 0                            # на доске ничья

    # Проверка наличия выигрышного фрагмента по горизонтали и вертикали игрового поля
    cod_win = []
    for stat, numb, _ in multi_for((board_st, trans(board_st)), (1, 2), (0, 0)):
        cod_win = get_cod(stat, numb)

        print(f'cod_win = {cod_win}')

        if cod_win: break

    # Проверяем наличие выигрышного фрагмента на диагоналях (сложный фрагмент кода)
    # Диагонали: (начинаются с верхней границы поля)
    # reduce(lambda st_d, j: st_d + [[st [i-j] [         i] for i in range(j, lw)]], range(0, (lw-numb_XO+1), 1), [])
    # reduce(lambda st_d, j: st_d + [[st [i-j] [(lw-1) - i] for i in range(j, lw)]], range(0, (lw-numb_XO+1), 1), [])
    # Диагонали: (заканчиваются на нижней границе поля)
    # reduce(lambda st_d, j: st_d + [[st [i] [         (j+i)] for i in range(-j, lw)]], range(0, -(lw-numb_XO+1), -1), [])
    # reduce(lambda st_d, j: st_d + [[st [i] [(lw-1) - (j+i)] for i in range(-j, lw)]], range(0, -(lw-numb_XO+1), -1), [])
    # Пример:
    # st = [[11,12,13,14], [21,22,23,24], [31,32,33,34], [41,42,43,44]]
    # print(*st, sep='\n')
    # [11, 12, 13, 14]
    # [21, 22, 23, 24]
    # [31, 32, 33, 34]
    # [41, 42, 43, 44]
    if not cod_win:
        for bound, slash, numb in multi_for((1, -1), (0, 1), (1, 2)):
            stat = diagonals(board_st, bound, slash)

            print(f'(bound, slash, numb) = {(bound, slash, numb)}')

            cod_win = get_cod(stat, numb)

            print(f'cod_win = {cod_win}')

            if cod_win: break
        else:
            return None                     # игра не закончена (нет победителей или ничьи)

    print(f'pin_player = {pin_player}')
    print(f'cod_win = {cod_win}')

    return dict_rev(pin_player, cod_win)


# 7. Показать статистику игр
#    Сыграно партий - N, из них:
#    Побед: Игрок-1 - x
#           Игрок-2 - y
#    Ничьих         - D (N - x - y)
def show_account(n_pl, win_pl1, win_pl2, win_pl, st):
    print(f'\nРаунд {n_pl}.')
    txt_result = f'Победитель: Игрок-{win_pl}' if win_pl else 'НИЧЬЯ'
    print(txt_result)
    show_board(st)
    print('-----------------------')
    print('Всего:')
    print(f'Сыграно партий - {n_pl}, из них:')
    print(f'Побед: Игрок-1 - {win_pl1}')
    print(f'       Игрок-2 - {win_pl2}')
    print(f'Ничьих         - {n_pl - win_pl1 - win_pl2}')
    print('-----------------------')


'''
=====================================================================================
Основное тело программы:
# ===================================================================================

План реализации:
-------------------
1. Выбрать игрока ("1" - Игрок-1; "2" - Игрок-2")
2. Выбрать значок ("х" иди "о")
3. Инициация и старт игры:
   Определить random кто начинает и сообщить об этом и о формате
   ввода своего хода. Формат ввода: [r][c], например "12" - сделать
   ход на поле, находящееся на пересечении 1-й строки и 2-го столбца
   (как показно на рис.)
4. Показать текущее состояние игры на доске:
    = 1   2   3
    1 . | x | .
    2 o | . | .
    3 . | . | .
5. Получить ход игрока, чей ход сейчас в таком виде: "Игрок-1 ->"
   Проверить корректность хода. Если ход не корректен (вне поля или
   поле уже занято) повторить запрос.
6. Обработать ход:
   - провести сделанный ход, обновив состояние в board_status
   - если сложилась тройка одинаковых значков на к-л строке, колонке
   или диагонали или все поля заняты (ничья) - игра завершена.
   Сообщить о результате игры (п.7)
   
Если игра завершена:
7. Вывести сообщение о результате:
    - Текущий результат (результат текущего раунда):
      Есть выигравший - "Победил игрок - ["Игрок-{}"] 
    - Общий счет:
        сколько сыграно, сколько побед у каждого игрока:
        Сыграно партий - N
        Побед: Игрок-1 - x
               Игрок-2 - y
        Ничьих         - D (N - x - y)
8. Уточнить о следующем раунде игры: 
"Еще раз?": - если да - переход на шаг-2; если нет - завершить игру.

Если игра не завершена:
9. Поменять текущего игрока, переход на шаг-4
------------------
'''
global size_board  # размер доски для игры
global numb_XO     # число значков ('x' или 'o') в линию для выигрыша
global pin_player  # фишки (значки) игроков (коды фишек см. signs)

player_one, player_two = 1, 2   # Номера игроков
size_min, size_max = 3, 8       # Допустимые размеры доски

print('\nСыграем в крестики-нолики?', end='')
while True:

    if myl.check_exit(txt_req='("Y" - ДА) -> '):
        break

    # Уточнение параметров игры (размер доски, число фишек в линии для выигрыша)
    size_board = myl.get_InputNumber(size_min, size_max, default=3, txt='\nВыберите размер доски (от 3 до 8)', end='-')
    if myl.check_exit(size_board):
        break
    numb_XO = myl.get_InputNumber(size_min, size_board, default=3,
                                  txt=f'Укажите число фишек в линию для выигрыша '
                                      f'(от {size_min} до {max(size_min, size_board - 1)})', end='-')
    if myl.check_exit(numb_XO):
        break

    # 1. Выбрать игрока ("1" - Игрок-1; "2" - Игрок-2")
    # 2. Выбрать значок ("х" иди "о")
    player_my, pin = myl.get_InputTuple(
        ((str(player_one), str(player_two)), player_one, 'Выберите номер игрока, за которого вы будете играть (1 или 2)'),
        (('x', 'o'), 'x', 'Выберите свой символ для игры ("x" или "o" - в латинице)'), type_input=tuple, end='-')
    player_my = int(player_my)
    pin_cod = dict_rev(signs, pin)

    pin_player = dict([(player_my, signs[pin_cod]), (player_one + player_two - player_my, signs[-pin_cod])])

    if player_my is None and myl.check_exit(player_my):
        break

    # 3. Инициация и старт игры - показать доску:
    current_player, n_games, wins_pl1, wins_pl2, board_status = init_game(player_my, size_board)

    # Игра:
    while True:

        # 4. Показать текущее состояние игры на игровом поле (показать доску)
        show_board(board_status)

        # 5. Получить ход текущего игрока (чей ход сейчас) и проверить корректность хода.
        move = get_move(current_player, board_status)
        if myl.check_exit(move):
            break

        # 6. Обработать ход:
        #    - провести сделанный ход, обновив состояние в board_status

        print(f'board_status-1 -> {board_status}')
        print(f'move -> {move}')
        print(f'current_player -> {current_player}')
        print(f'pin_player -> {pin_player}')
        print(f'pin_player[current_player] -> {pin_player[current_player]}')
        print(f'signs -> {signs}')

        # board_status[move // 10 - 1][move % 10 - 1] = pin_player[current_player]
        pin = pin_player[current_player]
        # lev1 = move // 10 - 1
        # lev2 = move % 10 - 1
        # board_status[lev1][lev2] = dict_rev(signs, pin)
        board_status[move // 10 - 1][move % 10 - 1] = dict_rev(signs, pin)

        print(f'board_status-2 -> {board_status}')

        #    - если сложилась тройка одинаковых значков на к-л строке, колонке
        #    или диагонали - игра завершена, если все поля заняты - ничья - сообщить о результате игры (п.7)
        #    иначе, устанавливаем текущего игрока и продолжаем игру (переход к п.4)
        result = is_winnings(board_status)

        print(f'result -> {result}')

        if result is None:                              # --- Если игра не завершена
            # 9. Поменять текущего игрока, переход на шаг-4
            current_player = player_one + player_two - current_player
            continue

        else:                                           # --- Если игра завершена:
            # 7. Ведение и вывод статистики игр по данным о результатах игр (result)
            n_games += 1
            wins_pl1 += 1 if result == player_one else 0
            wins_pl2 += 1 if result == player_two else 0
            show_account(n_games, wins_pl1, wins_pl2, result, board_status)

            # 8. уточнить о следующем раунде игры.
            #    "Еще раз?": - если да - переход на шаг-2; если нет - завершить игру.
            special = 'NnТт'
            select_cont = myl.check_exit(special=special, txt_req='\nЕще партию - нажмите кл. [ Y ]. '
                                                                  '\nЕсли желаете изменить вариант игры '
                                                                  '(размер доски, кол. "x" или "о" в ряд победы), '
                                                                  'нажмите кл. [ N ]ew -> ')
            if select_cont:
                if isinstance(select_cont, str):
                    # new = select_cont in special
                    break
                exit()


    print('\n Выбрано изменение варианта игры. Продолжить?')
