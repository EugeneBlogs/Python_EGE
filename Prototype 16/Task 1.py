# Условие задания КИМ 16 (Умскул):
'''
Функция "F(n)" определятся следующим образом:
"F(n) = n", если "n <= 5":
"F(n) = 2 * F(n - 3)", если "n > 5" и не делится на 5;
"F(n) = F(n - 4) + F(n - 5)", если "n > 5" и делится на 5.
Чему равно значение "F(30)"?
'''


def F(n):
    if n <= 5:
        return n
    if n > 5 and n % 5 != 0:
        return 2 * F(n - 3)
    if n > 5 and n % 5 == 0:
        return F(n - 4) + F(n - 5)


print(F(30))

'''
Пусть "а % b" - это остаток при делении натурального числа "а" на натуральное число "b",
"а /" - целочисленное деление. Тело функции "F(n)" задано следующими строчками и условиями:
"F(0) = F(1) = 5",
"F(n) = F(n - 5) / 3 + 9", при "n > 1" и при "n % 5 = 0",
"F(n) = F(n - (n % 5)) + n * 2", при "n > 1" и при "n % 5 > 0",
При этом "n" - целое неотрицательное число. Определите, что вернет данная функция, если в неё передать аргумент "n = 42".
'''


def F(n):
    if n == 0 or n == 1:
        return 5
    if n > 1 and n % 5 == 0:
        return F(n - 5) // 3 + 9
    if n > 1 and n % 5 > 0:
        return F(n - (n % 5)) + n * 2


print(F(42))

# Условие задания КИМ 16 (Умскул):
'''
Алгоритм вычисления значения функции "F(n)", где "n" - натуральное число,
задан следующими соотношениями:
"F(n) = 1", если "n = 1"
"F(n) = n * F(n - 1)", если "n > 1".
Чему равно значение выражения "F(2023) / F(2020)"?
'''

'''
Известно, что в Python по умолчанию установлено ограничение на глубину рекурсии - не больше 1000 рекурсивных вызовов.
Для того, чтобы увеличить возможную глубину рекурсии до 10000 нужно в начале программы выполнить две инструкции:
'''

import sys

sys.setrecursionlimit(10000)

'''
Примечание: следует учесть, что глубину рекурсии нельзя увеличивать до очень большого значения,
помимо ограничения, который устанавливается при помощи "setrecursionlimit",
есть и ограничения операционной системы!
'''


def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)


print(F(2023) / F(2020))
print((F(2024) // 15 - F(2023)) // F(2021))