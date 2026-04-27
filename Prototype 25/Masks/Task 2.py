# Условие задания КИМ 25 ( скинул Дима :) ):
'''
Среди натуральных чисел, не превышающих 10^10, найдите все числа, соответствующие маске "14?127*0", которые делятся на
1234 без остатка и у которых сумма цифр - простое число.
В ответе запишите все найденные числа в порядке возрастания, справа от каждого числа - результат его деления на 1234.
'''


def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


from fnmatch import fnmatch

for x in range(1234, 10 ** 10 + 1, 1234):
    if fnmatch(str(x), "14?127*0"):
        summa = sum(int(el) for el in str(x))
        if prime(summa):
            print(x, x // 1234)

# Условие задания КИМ 25 (Умскул):
'''
Среди натуральных чисел, не превышающих 10^8, найдите все числа, соответствующие маске "12?5*5??",
которые представляют собой произведение двух различных простых чисел и делятся на 311 без остатка.
В ответе запишите все найденные числа в порядке возрастания, справа от каждого числа – результат его деления на 311.
'''

from fnmatch import fnmatch


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return x > 1


def dels(x):
    delit = []
    for i in range(2, int(x ** 0.5) + 1):
        if i ** 2 == x:
            delit.append(i)
        elif x % i == 0:
            delit.append(i)
            delit.append(x // i)
    return delit


for i in range(311, 10 ** 8 + 1, 311):
    if fnmatch(str(i), "12?5*5??"):
        a = dels(i)
        if len(a) == 2:
            if is_prime(a[0]) and is_prime(a[1]):
                print(i, i // 311)
