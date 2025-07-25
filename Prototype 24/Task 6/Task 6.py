# Условие задания КИМ 24 (Яндекс Учебник, Досрок 2022):
'''
Текстовый файл состоит из символов, обозначающих прописные буквы латинского алфавита.
Определите максимальное количество идущих подряд символов, среди которых никакие
две буквы из набора букв "A", "B" и "С" (с учётом повторений) не записаны подряд.
'''

# СПОСОБ 1
f = open("6.txt")
s = f.readline()
s = s.replace("A", "*").replace("B", "*").replace("C", "*")
max_count = 0
count = 1
for i in range(len(s) - 1):
    if s[i] + s[i + 1] != "**":
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
print(max_count)

# СПОСОБ 2
f = open("6.txt")
s = f.readline()
s = s.replace("A", "*").replace("B", "*").replace("C", "*")
for _ in range(2):
    s = s.replace("**", "* *")
max_str = max(s.split(), key=len)
print(len(max_str))
