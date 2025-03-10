# Условие задания КИМ 5 (Умскул):
'''
На вход алгоритма подаётся натуральное число "N". Алгоритм строит по нему новое число "R" следующим образом.
1. Строится двоичная запись числа "N".
2. Далее эта запись обрабатывается по следующему правилу:
а) если сумма цифр в двоичной записи числа чётная, то к этой записи справа дописывается О, а затем два левых разряда заменяются на 10;
б) если сумма цифр в двоичной записи числа нечётная, то к этой записи справа дописывается 11, а затем два левых разряда заменяются на 11.
Полученная таким образом запись является двоичной записью искомого числа "R".
Укажите наибольшее число "N", после обработки которого с помощью этого алгоритма получается число "R", меньшее 99.
В ответе это число запишите в десятичной системе счисления.
'''

maximum = 10 ** (-10)
for n in range(1, 1001):
    result = bin(n)[2:]
    summa = 0
    for s in result:
        summa += int(s)
    if summa % 2 == 0:
        result += "0"
        result = f"10{result[2:]}"
    else:
        result += "11"
        result = f"11{result[2:]}"
    r = int(result, 2)
    if r < 99:
        if n > maximum:
            maximum = n
print(maximum)
