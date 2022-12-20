# 1. Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# import random
# import sys
#
#
# def check_candies(number_candies, player):
#     if number_candies <= 1:
#         print(f'Выиграл {player}!')
#
#
# def player_turn(numb_of_cands, choices):
#     numb_of_cands -= choices
#     print(f'Ход игрока: {choices}')
#     print(f'Осталось {numb_of_cands} конфет\n')
#     return numb_of_cands
#
#
# def main_players(numb_of_cands):
#     try:
#         players_choice = int(input('Введите желаемое количество конфет: '))
#     except ValueError:
#         print('Неверный формат значение')
#         sys.exit()
#     # players_choice = random.randrange(1, 29)
#     while players_choice < 1 or players_choice > 28:
#         print('Неверно задано значение. Попробуйте еще раз')
#         players_choice = int(input('Введите желаемое количество конфет: '))
#     numb_of_cands = player_turn(numb_of_cands, players_choice)
#     return numb_of_cands
#
#
# def computer_turn(numb_of_cands):
#     count = numb_of_cands / 28  # множитель
#     if (count % 1) != 0:        # если есть остаток, то округляем до следующего множителя
#         count += 1
#     if count % 2 == 0:          # если четный множитель - проигрыш при идеальных стратегиях. если нет - выигрыш
#         numb_of_cands -= 1
#         print(f'Ход компьютера: 1')
#     else:
#         numb_of_cands -= 28
#         print(f'Ход компьютера: 28')
#     print(f'Осталось {numb_of_cands} конфет\n')
#     return numb_of_cands
#
#
# def main_computers(numb_of_cands):
#     numb_of_cands = computer_turn(numb_of_cands)
#     return numb_of_cands
#
#
# print('Добро пожаловать в игру с конфетами.\n\nПравила:\nНа столе лежит 2021 конфета. Играют игрок и компьютер делая '
#       'ход друг после друга. Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет. '
#       'Все конфеты оппонента достаются сделавшему последний ход. Выигрывает тот, у кого останутся все конфеты.\n')
# numb_of_candies = 2021
# candies = numb_of_candies
# whos_first = random.randrange(0, 1)
# if whos_first == 0:
#     print('Игру начинает игрок\n')
#     while candies > 0:
#         candies = main_players(candies)
#         check_candies(candies, 'игрок')
#         if candies <= 0:
#             sys.exit()
#         candies = main_computers(candies)
#         check_candies(candies, 'компьютер')
# else:
#     print('Игру начинает компьютер\n')
#     while candies > 0:
#         candies = main_computers(candies)
#         check_candies(candies, 'компьютер')
#         if candies <= 0:
#             sys.exit()
#         candies = main_players(candies)
#         check_candies(candies, 'игрок')

# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (здесь только буквы).
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# import random
# import string
#
#
# def input_generation():
#     letters = string.ascii_lowercase
#     rand_string = ''.join(random.choice(letters) for i in range(random.randrange(100, 1001)))
#     return rand_string
#
#
# def encode(data_for_encode):
#     output_data_from_encode = ''
#     for i, symbol in enumerate(data_for_encode):
#         count = 1
#         while i + 1 < len(data_for_encode) and symbol == data_for_encode[i + 1]:
#             count = count + 1
#             i = i + 1
#         output_data_from_encode += f'{str(count)}{data_for_encode[i]}'
#
#     return output_data_from_encode
#
#
# with open('input_data.txt', 'w', encoding='utf=8') as f:    # запись входных данных
#     f.write(input_generation())
#
# with open('input_data.txt', 'r', encoding='utf=8') as f:
#     input_data = f.read()
#
# output_data = encode(input_data)
#
# with open('out_data.txt', 'w', encoding='utf=8') as f:
#     f.write(output_data)


# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

def del_some_words(text):
    text = list(filter(lambda x: ('а' not in x) and ('б' not in x) and ('в' not in x), text.split()))
    return " ".join(text)


original_string = 'Напишите программу, удаляющую из текста все слова, содержащие "абв"'

final_string = del_some_words(original_string.lower())
print(final_string)
