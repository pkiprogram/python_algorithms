# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Введите трехзначное число: ')

sum = 0
proizv = 1

for n in number:
    sum += int(n)
    proizv *= int(n)
print(f'Сумма цифр числа {number}: {sum}')
print(f'Произведение цифр: {number}: {proizv}')