# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.


# Python 3.9.X
# OS - 64bit

import sys

def count_size(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                size += sys.getsizeof(item)
    return size

# 1 урок 3 задача. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

x1 = float(input('Введите координату X первой точки '))
y1 = float(input('Введите координату Y первой точки '))
x2 = float(input('Введите координату X второй точки '))
y2 = float(input('Введите координату Y второй точки '))
if x2 == x1:
    print('Error')
    exit()
k = (y2 - y1) / (x2 - x1)
b = (y1 - k * x1)

print(f'Уравнение прямой: y = {k}x + {b}')

sum_ = 0
var_lst = (x1, y1, x2, y2, k, b)
for i in var_lst:
    sum_ += count_size(i)
print(f'Под переменные задействованно {sum_} байт памяти')

# Под переменные задействованно 144 байт памяти



# 2 урок 3 задача. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


# Вариант 1
number = input('Введите число: ')
new_number = int(number[::-1])
print(f'Сформированное число: {new_number}')

sum_ = 0
var_lst = (number, new_number)
for i in var_lst:
    sum_ += count_size(i)
print(f'Под переменные задействованно {sum_} байт памяти')

# Под переменные задействованно 83 байт памяти



# Вариант 2
num = int(input("Введите целое число: "))
num_rev = 0

while num > 0:
    # находим остаток - последнюю цифру
    x = num % 10
    # делим нацело - удаляем последнюю цифру
    num = num // 10
    # увеличиваем разрядность второго числа
    num_rev = num_rev * 10
    # добавляем очередную цифру
    num_rev = num_rev + x

print(f'Сформированное число: {num_rev}')

sum_ = 0
var_lst = (num, num_rev)
for i in var_lst:
    sum_ += count_size(i)
print(f'Под переменные задействованно {sum_} байт памяти')

# Под переменные задействованно 52 байт памяти