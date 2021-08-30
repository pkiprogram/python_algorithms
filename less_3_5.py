# 5. В массиве найти максимальный отрицательный элемент. Вывести н экран его значение и позицию в массиве.

import random

r = [random.randint(-50, 50) for _ in range(50)]
print(f'Массив: {r}')

min_index = 0

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)

if r[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {r[min_index]}.',
            f'Находится в массиве на позиции {min_index}')
