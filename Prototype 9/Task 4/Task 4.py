# Условие задания КИМ 14 (Гусева Марина Альфонсовна, "Решу ЕГЭ"):
'''
Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.
Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
— каждое число в строке встречается по одному разу,
— утроенная сумма максимального и минимального значений не превышает удвоенной суммы оставшихся чисел.
В ответе запишите только число.
'''

file = open("4.txt")
data = [[int(n) for n in el.split()] for el in file.readlines()]
count = 0
for el in data:
    arr = sorted(el)
    povtor = [el for el in arr if arr.count(el) != 1]
    ne_povtor = [el for el in arr if arr.count(el) == 1]
    max_number = max(arr)
    min_number = min(arr)
    if not povtor and (3 * (max_number + min_number) <= 2 * (sum(arr) - min_number - max_number)):
        count += 1
print(count)