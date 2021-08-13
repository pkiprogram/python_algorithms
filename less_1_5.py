# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.


letr1 = input('Введите первую букву из диапазона от a до z только в нижнем регистре: ')
letr2 = input('Введите вторую букву из диапазона от a до z только в нижнем регистре: ')

# получаем числовой код введенных букв
letr1_int = ord(letr1)
letr2_int = ord(letr2)

# получаем числовой код начала и конца алфавита
a_code = ord('a')
z_code = ord('z')

if (letr1_int < letr2_int
        and a_code <= letr1_int <= z_code
        and a_code <= letr2_int <= z_code):
    letr1_pos = letr1_int - a_code + 1
    letr2_pos = letr2_int - a_code + 1
    print(f"Позиция '{letr1}' = {letr1_pos}, позиция '{letr2}' = {letr2_pos}, букв между ними: {letr2_pos - letr1_pos - 1}")
else:
    print('Ошибка ввода данных')