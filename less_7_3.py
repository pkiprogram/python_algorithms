# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках


import random

m = 4
size = 2 * m + 1
arr = [random.randint(1, 50) for i in range(size)]

print(f'Исходный массив:\n {arr}\n')

def median(lst):
    if len(lst) % 2 == 0:
        center = []
        for i in lst:
            b = 0
            for j in lst:
                if i < j:
                    b += 1
            if len(lst) == b * 2 + 2 or len(lst) == b * 2:
                center.append(i)
        return sum(center) / 2
    else:
        for i in lst:
            num = i
            b = 0
            for j in lst:
                if i < j:
                    b += 1
            if len(lst) == 2 * b + 1:
                return num

print(f'Медиана неотсортированного массива: {median(arr)}\n')

print(f'Отсортированный массив: \n{sorted(arr)}')