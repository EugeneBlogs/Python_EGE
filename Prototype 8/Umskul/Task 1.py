# Условие задания КИМ 8 (Умскул):
'''
Сколько существует чисел, одиннадцатеричная запись которых содержит ровно 8 знаков,
причем в ней чередуются цифры кратные и некратные трем?
'''

from itertools import product

p = product("0123456789A", repeat=8)
k = "0369"
n = "124578A"
count = 0
for x in p:
    s = "".join(x)
    if s[0] != "0":
        if (s[0] in k and s[1] in n and s[2] in k and s[3] in n and s[4] in k and s[5] in n and s[6] in k and s[
            7] in n) or (
                s[0] in n and s[1] in k and s[2] in n and s[3] in k and s[4] in n and s[5] in k and s[6] in n and s[
            7] in k):
            count += 1
print(count)
