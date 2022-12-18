# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих
# на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import sys

try:
    our_str = input('Введите целые числа через пробел: ').split(' ')
    for count, i in enumerate(our_str):
        our_str[count] = abs(int(i))
except ValueError:
    print(f'Неверный формат ввода')
    sys.exit()
final = 0
for count, i in enumerate(our_str):
    if count % 2 != 0:
        final += i
print(final)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import sys

try:
    our_list = input('Введите целые числа через пробел: ').split(' ')
    for count, i in enumerate(our_list):
        our_list[count] = int(i)
except ValueError:
    print(f'Неверный формат ввода')
    sys.exit()

final_list = []
if len(our_list) % 2 != 0:
    numb_for_count = len(our_list)//2 + 1
else:
    numb_for_count = len(our_list)//2

for count in range(numb_for_count):
    final_list.append(our_list[0+count]*our_list[-1-count])
print(final_list)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import sys


initial_str = input('Задайте список из вещественных чисел через запятую :')
list_str = initial_str.split(', ')
list_float = []
try:
    for numb in list_str:
        if '.' in numb and len(numb.split('.')) <= 2:
            new_numb = numb.split('.')[1]
            list_float.append(float(f'0.{new_numb}'))
        else:
            print(f'Неверный формат ввода')
            sys.exit()
except ValueError:
    print(f'Неверный формат ввода')
    sys.exit()

diff_bw_numbs = round(max(list_float) - min(list_float), 5)
print(diff_bw_numbs)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые
# функции.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import sys


our_numb = input('Введите целое десятичное число для перевода в двоичную систему: ')

try:
    our_numb = int(our_numb)
except ValueError:
    print('Неверный формат ввода')
    sys.exit()

list_for_binary_numbs = []
while our_numb != 1:
    list_for_binary_numbs .append(our_numb % 2)
    our_numb = our_numb // 2
list_for_binary_numbs.append(1)
list_for_binary_numbs.reverse()
str_for_binary_numbs = ''
for i in list_for_binary_numbs:
    str_for_binary_numbs = f'{str_for_binary_numbs}{str(i)}'

print(int(str_for_binary_numbs))
