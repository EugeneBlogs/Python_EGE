# Условие задания КИМ 5 (Умскул):
'''
На вход алгоритма подаётся натуральное число "N". Алгоритм строит по нему новое число "R" следующим образом:
1) Строится двоичная запись числа "N".
2) Если "N" кратно 5, то в конец двоичной записи числа дописываются три последние цифры числа.
Иначе в конец двоичной записи числа дописывается остаток от деления "N" на 5,
умноженный на 4, в двоичной записи.
Полученная таким образом запись является двоичной записью искомого числа "R". Укажите
минимальное число "N", после обработки которого автомат получает число, большее 150.
 В ответе это число запишите в десятичной системе
'''

for N in range(1, 100):
    bin_N = bin(N)[2:]
    if N % 5 == 0:
        bin_N += bin_N[-3:]
    else:
        bin_N += bin((N % 5) * 4)[2:]
    R = int(bin_N, 2)
    if R > 150:
        print(N)
        break
