# Условие задания КИМ 14 (Яндекс Учебник):
'''
Дано уравнение: "4163x1 (y сс) = 247393 (10 сс)"
В записи чисел переменной "x" обозначена неизвестная цифра из алфавита "y"-ричной системы счисления.
Вычислите "x", "y".
'''

import string

alphabet = string.digits + string.ascii_uppercase
for y in range(7, len(alphabet)):  # От 7, так как максимальная цифра в первом числе - 6
    s = alphabet[:y]
    for x in s:
        a = int(f"4163{x}1", y)
        b = 247393
        if a == b:
            print(x, y)
            break
