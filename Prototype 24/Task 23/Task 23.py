# Условие задания КИМ 24 (Умскул, Демоверсия 2022):
'''
Текстовый файл состоит из символов "P", "Q", "R" и "S".
Определите максимальное количество идущих подряд символов в прилагаемом файле,
среди которых нет идущих подряд символов "P".
Для выполнения этого задания следует написать программу.
'''

f = open("23.txt")
s = f.readline()
for _ in range(2):  # Дважды, чтобы точно не возникло ошибки
    s = s.replace("PP", "P P")
max_str = max(s.split(), key=len)
print(len(max_str))
