# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


import collections

company = collections.namedtuple('company', ['name', 'profit1', 'profit2', 'profit3', 'profit4', 's'])
companies = []
x = int(input("Введити кол-во компаний: "))
total = 0
for i in range(x):
    name = input(f"Название {i+1}-ого предприятия: ")
    profit1 = int(input("Прибыль за 1 квартал: "))
    profit2 = int(input("Прибыль за 2 квартал: "))
    profit3 = int(input("Прибыль за 3 квартал: "))
    profit4 = int(input("Прибыль за 4 квартал: "))
    s = profit1 + profit2 + profit3 + profit4
    total += s
    companies.append(company(name=name, profit1=profit1, profit2=profit2, profit3=profit3, profit4=profit4, s=s))
total_avg = total / x
print(f"Предприятия с прибылью выше средней {total_avg}: ")
for company in companies:
    if company.s >= total_avg:
        print(company.name)
print(f"Предприятия с прибылью неже средней {total_avg}: ")
for company in companies:
    if company.s < total_avg:
        print(company.name)