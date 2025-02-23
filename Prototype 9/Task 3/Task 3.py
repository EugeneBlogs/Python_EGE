# Условие задания КИМ 14 (Гусева Марина Альфонсовна, "Решу ЕГЭ"):
'''
Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
Определите количество строк таблицы, содержащих числа, для чисел которых выполнены оба условия:
— в строке есть одно число, которое повторяется трижды, остальные три числа различны;
— повторяющееся число строки не меньше, чем среднее арифметическое трёх её неповторяющихся чисел.
В ответе запишите только число.
'''

file = open("3.txt")
data = [[int(n) for n in el.split()] for el in file.readlines()]
count = 0
for el in data:
    arr = sorted(el)
    povtor = [el for el in arr if arr.count(el) != 1]
    ne_povtor = [el for el in arr if arr.count(el) == 1]
    if len(ne_povtor) == 3 and len(set(povtor)) == 1 and max(povtor) >= (sum(ne_povtor) / len(ne_povtor)):
        count += 1
print(count)
