# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

arr = [random.randint(-100, 100) for i in range(10)]
print(f' {arr}')

def bubble_sort(arr):
    n = 1
    while n < len(arr):
        sorted = True
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
        if sorted == True:
            break
        n += 1

    print(f'Отсортированный массив:\n {arr}')

bubble_sort(arr)