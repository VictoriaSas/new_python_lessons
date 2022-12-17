# 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
#
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

import sys


def sum_right(full_numb):
    count = 0
    while full_numb % 1 != 0:
        full_numb = round(full_numb * 10, 5)
        count += 1

    our_numb_right = round(full_numb % (10 ** count), 5)

    full_right_sum = 0
    while our_numb_right > 0:
        full_right_sum += round(our_numb_right % 10)
        our_numb_right = (our_numb_right // 10)
    return full_right_sum


def sum_left(full_numb):
    count = 0
    while full_numb % 1 != 0:
        full_numb = round(full_numb * 10, 5)
        count += 1

    our_numb_left = round(full_numb // (10 ** count), 5)

    full_left_sum = 0
    while our_numb_left > 0:
        full_left_sum += round(our_numb_left % 10)
        our_numb_left = (our_numb_left // 10)
    return full_left_sum


def total_amount(number):
    return sum_right(number) + sum_left(number)


try:
    numb = abs(round(float(input('Введите число: ')), 5))
except ValueError:
    sys.exit('Неверный формат')

print(total_amount(numb))

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import sys


try:
    n = abs(int(input('Введите целое число: ')))
except ValueError:
    sys.exit('Неверный формат')


final_numb = []
i = 1
product_of_numb = 1
while n > 0:
    product_of_numb *= i
    i += 1
    final_numb.append(product_of_numb)
    n -= 1

print(final_numb)

# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество
# вхождений одной строки в другой. Нельзя юзать find или count.
import re


first_phrase = input('Введите первую фразу: ')
second_phrase = input('Введите вторую фразу: ')

our_match = re.findall(rf'{first_phrase}', second_phrase, re.IGNORECASE)
print(f'Количество вхождений первой строки во вторую: {len(our_match)}')
