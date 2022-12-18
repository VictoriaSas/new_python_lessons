# 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import sys


try:
    n = input('Введите натуральное число: ')
    if '-' in n:
        raise ValueError
    else:
        n = int(n)
except ValueError:
    print('Неверный формат')
    sys.exit()

factor = 2
list_of_primes = []
while factor * factor <= n:
    while n % factor == 0:
        list_of_primes.append(int(factor))
        n = n / factor
    factor = factor + 1
if n > 1:
    list_of_primes.append(int(n))
print(list_of_primes)

# 2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

import sys


try:
    initial_sequence = input('Задайте последовательность чисел через пробел: ').split(' ')
    for count, el in enumerate(initial_sequence):
        initial_sequence[count] = float(el)
except ValueError:
    print('Неверный формат')
    sys.exit()

unique_values = set()
tmp = set()

for el in initial_sequence:
    if el not in tmp:
        unique_values.add(el)
    else:
        unique_values.discard(el)
    tmp.add(el)

print(list(unique_values))

# 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

k = 4
coefficients = []
for count in range(k+1):
    coefficient = (random.randrange(0, 101))
    if coefficient != 0:
        if k - count == 0:
            coefficients.append(f'{random.randrange(0, 101)}')
        else:
            coefficients.append(f'{random.randrange(0, 101)}**x{k-count}')

print(coefficients)


with open('polynomial.txt', 'w+', encoding='utf-8') as f:
    our_str = ''
    for count in range(k+1):
        if count != 0:
            our_str += ' + '
        our_str += coefficients[count]
    print(our_str)
    f.write(f'{our_str} = 0')




