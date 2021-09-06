# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


import random

def m_sort(arr):
    if len(arr) <= 1:
        return arr

    # необязательное дополненение
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    left = m_sort(arr[:len(arr) // 2])
    right = m_sort(arr[len(arr) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[j]
            j += 1

    while len(left) > i:
        arr[i + j] = left[i]
        i += 1
    while len(right) > j:
        arr[i + j] = right[j]
        j += 1

    return arr

fl_arr = [round(random.uniform(1, 50, ), 2) for i in range(8)]
print(fl_arr)
m_sort(fl_arr)
print(fl_arr)