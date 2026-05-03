# Условие задания КИМ 24 (Профиматика):
'''
Текстовый файл состоит из заглавных букв латинского алфавита "A", "B", "C", "D", "E" и "F".
Определите в прилагаемом файле максимальное количество идущих подряд символов,
среди которых пара символов "BC" (в указанном порядке) встречается ровно 190 раз.
В ответе запишите число – количество символов в найденной последовательности.
Для выполнения этого задания следует написать программу.
'''

from time import *

### 1. Метод разделения на строки (≈3 секунды)
start = time()
a = open("24.txt").readline()
# a = "AAABCAAABCAAABCAAABCAA"  # Для данного условия нужно, чтобы "BC" встречалось ровно 2 раза
a = a.replace("BC", "B C")
s = a.split()
r = 0
for i in range(len(s) - 190):
    st = ''.join(s[i:i + 191])
    r = max(r, len(st))
print(f"1. Метод разделения на строки. Ответ: {r} | Время: {time() - start}")

### (Реализация: Умскул) 2. Метод индексов (≈5 секунд)
st = time()
a = open("24.txt").readline()
# a = "AAABCAAABCAAABCAAABCAA"  # Для данного условия нужно, чтобы "BC" встречалось ровно 2 раза
a = "BC" + a + "BC"
indexes_BC = [i for i in range(len(a)) if a[i:i + 2] == "BC"]
res = []
for i in range(len(indexes_BC) - 191):
    res.append(indexes_BC[i + 191] - indexes_BC[i])
res[0] -= 1
res[-1] -= 1
print(f"2. Метод индексов. Ответ: {max(res)} | Время: {time() - start}")

### 3. Метод двух указателей (≈15 секунд)
start = time()
a = open("24.txt").readline()
# a = "AAABCAAABCAAABCAAABCAA"  # Для данного условия нужно, чтобы "BC" встречалось ровно 2 раза
k = 0
s = ""
m = 0
for r in range(len(a)):
    s += a[r]
    if s[-2:] == "BC": k += 1
    while k > 190:
        if s[:2] == "BC": k -= 1
        s = s[1:]
    if k == 190: m = max(m, len(s))
print(f"3. Метод двух указателей. Ответ: {m} | Время: {time() - start}")

### 4. Метод двух циклов (≈1,5 минуты)
start = time()
a = open("24.txt").readline()
# a = "AAABCAAABCAAABCAAABCAA"  # Для данного условия нужно, чтобы "BC" встречалось ровно 2 раза
m = 1
for l in range(len(a)):
    for r in range(l + m, len(a)):
        s = a[l:r + 1]
        if s.count("BC") == 190:
            m = max(m, len(s))
        if s.count("BC") > 190: break
print(f"4. Метод двух циклов. Ответ: {m} | Время: {time() - start}")
