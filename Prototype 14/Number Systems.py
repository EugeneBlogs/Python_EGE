# Перевод из 10 системы счисления в "N"

import string

alphabet = string.digits + string.ascii_uppercase
result = ""
base = int(input("Система счисления: "))
number = int(input("Число: "))
while number > 0:
    result += alphabet[number % base]
    number //= base
result = result[::-1]
print(result)

# Перевод из "N" системы счисления в 10 ("2 <= N <= 36")

base = int(input("Система счисления: "))
number = input("Число: ")
print(int(number, base))

# Перевод из "N" системы счисления в 10 (универсальный метод)

from string import ascii_uppercase as al

al = "0123456789" + al

base = int(input("Система счисления: "))
number = input("Число: ")


def int(s, n):
    s = s[::-1]
    sm = 0
    for i in range(len(s)):
        sm += al.index(s[i]) * n ** i
    return sm


print(int(number, base))
