# Условие задания КИМ 24 (Яндекс Учебник, ЕГЭ 2024):
'''
Текстовый файл состоит из символов "T", "U", "V", "W", "X", "Y", "Z".
Определите в прилагаемом файле максимальное количество идущих подряд символов (длину непрерывной подпоследовательности),
среди которых символ "T" встречается ровно 100 раз.
'''

# СПОСОБ 1
f = open("5.txt")
s = f.readline()
s = s.split("T")
count = 0
for i in range(len(s) - 101):
    line = "T".join(s[i:i + 101])
    count = max(count, len(line))
print(count)

# СПОСОБ 2
f = open("5.txt")
s = "T" + f.readline() + "T" # В начало и конец добавляет также буквы "T", чтобы сделать проверку на начало и конец строки
index_T = [i for i in range(len(s)) if s[i] == "T"]  # Создаём список со всеми индексами буквы "T"
result = []
# Если разность между индексами равна 101, то между данными буквами ровно 100 "T"
for i in range(101, len(index_T)):
    result.append(index_T[i] - index_T[i - 101] - 1)
print(max(result))
