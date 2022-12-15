# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли
# этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

numb = input('введите цифру, обозначающую день недели, где 1-пн, вс-7: ')
if numb.isdigit() is True:
    if 1 <= int(numb) <= 7:
        if int(numb) == 6 or int(numb) == 7:
            print('это выходной')
        else:
            print('это не выходной')
else:
    print('неверный формат')


# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений.

def first_check_statement(numb_x, numb_y, numb_z):
    if (numb_x + numb_y + numb_z) > 0:
        return False
    else:
        return True


def second_check_statement(numb_x, numb_y, numb_z):
    if numb_x == 0:
        numb_x = 1
    else:
        numb_x = 0
    if numb_y == 0:
        numb_y = 1
    else:
        numb_y = 0
    if numb_z == 0:
        numb_z = 1
    else:
        numb_z = 0
    if (numb_x * numb_y * numb_z) == 0:
        return False
    else:
        return True


binary_code = {
    0: '000',
    1: '001',
    2: '010',
    3: '011',
    4: '100',
    5: '101',
    6: '110',
    7: '111'
}

answer = True
for count in range(8):

    xyz = binary_code.get(count)
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    if first_check_statement(x, y, z) != second_check_statement(x, y, z):
        answer = False

if answer is True:
    print('Выражение истинно')
else:
    print('Выражение ложно')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

if x > 0:
    if y > 0:
        print('1')
    elif y < 0:
        print('4')
    elif y == 0:
        print('x')
elif x < 0:
    if y > 0:
        print('2')
    elif y < 0:
        print('3')
    elif y == 0:
        print('x')
elif x == 0:
    if y == 0:
        print('Начало координат')
    else:
        print('y')


# задача 4 HARD (необязательная)
# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и
# операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и
# выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.
#
# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!
#
# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0
#
# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

our_operation = ('+', '-', '/', '*', 'mod', 'pow', 'div')
first_numb = input('Введите первое число: ')
second_numb = input('Введите второе число: ')
operation = input('Введите желаемую операцию: ')

if (first_numb.count('.') == 1) and first_numb.split('.')[0].isdigit() and first_numb.split('.')[1].isdigit():
    first_numb = float(first_numb)
else:
    raise ValueError('Неверный формат записи первого числа')

if (second_numb.count('.') == 1) and second_numb.split('.')[0].isdigit() and second_numb.split('.')[1].isdigit():
    second_numb = float(second_numb)
else:
    raise ValueError('Неверный формат записи второго числа')
if operation not in our_operation:
    raise ValueError('Неверный формат записи операции')

match operation:
    case '+':
        print(round(first_numb+second_numb, 4))
    case '-':
        print(round(first_numb-second_numb, 4))
    case '/':
        if second_numb == 0.0:
            print('Деление на ноль!')
        else:
            print(round(first_numb/second_numb, 4))
    case '*':
        print(round(first_numb*second_numb, 4))
    case 'mod':
        print(round(first_numb%second_numb, 4))
    case 'pow':
        print(round(first_numb**second_numb, 4))
    case 'div':
        print(round(first_numb//second_numb, 4))


