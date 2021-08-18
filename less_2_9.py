# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def summ_num(num):
    summ = 0
    for dig in num:
        summ += int(dig)
    return summ


numbers = [i for i in input('Введите числа через пробел').split()]

max_num = 0
max_summ = 0
for i in numbers:
    if summ_num(i) > max_summ:
        max_num = i
        max_summ = summ_num(i)

print(f'Наибольшая сумма цифр {max_summ} у числа {max_num}')

