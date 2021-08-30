# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):
    matrix.append([])
    summ = 0
    for n in range(4):
        user_number = int(input(f'Введите элемент {i+1} и {n+1} столбца: '))
        summ += user_number
        matrix[i].append(user_number)

    matrix[i].append(summ)

for a in matrix:
    print(('{:>4d}' * 5).format(*a))
