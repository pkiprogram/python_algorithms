# 2. Написать два алгоритма нахождения i-го по счёту простого числа.


import cProfile as cp



number = int(input('Введите порядковый номер простого числа: '))

# Без «Решета Эратосфена»;

def algo(number):
    primes = []
    for i in range(2, 10000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    print(f'Искомое простое число = {primes[number - 1]} без использования "Решета"')
    
cp.run('algo(number)')



# С «Решетом Эратосфена»

def sieve(number):
    primes = []
    nums = [i for i in range(2, 10000)]

    for i in nums:
        if i != 0:
            primes.append(i)
            for j in nums[i:]:
                if j % i == 0:
                    nums[j - 2] = 0
    print(f'Искомое простое число = {primes[number - 1]} с использованием "Решета"')

cp.run('sieve(number)')

# Скорость  алгоритма с "Решетом" ниже, чем без "Решета",
