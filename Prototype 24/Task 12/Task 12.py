# Условие задания КИМ 24 (Яндекс Учебник)
'''
Текстовый файл состоит из букв "D", "E", "G", "O", "R", "T".
Найдите максимальную длину цепочки вида "DOGDOGDOGD..." Цепочка состоит из повторяющихся фрагментов "DOG",
последний фрагмент может быть неполным.
'''

f = open("12.txt")
s = f.readline()
count = 1
max_count = 0
current = "D"
for el in s:
    if el == "D" and current == "D":
        count += 1
        current = "O"
    elif el == "O" and current == "O":
        count += 1
        current = "G"
    elif el == "G" and current == "G":
        count += 1
        current = "D"
    else:
        max_count = max(count, max_count)
        count = 1
print(max_count)
