# Условие задания КИМ 14 ("Решу ЕГЭ"):
'''
В каждой строке электронной таблицы записаны восемь натуральных чисел.
Число в строке считается заметным, если оно строго больше среднего арифметического всех чисел строки.
Определите количество строк таблицы, для которых одновременно выполнены следующие условия:
— количество заметных чётных чисел в строке больше количества заметных нечётных чисел в строке;
— сумма всех чётных чисел строки меньше суммы всех нечётных чисел строки.
'''

file = open("5.txt")
data = file.readlines()
count = 0
for el in data:
    numbers = [int(i) for i in el.split()]
    srednee = sum(numbers) / len(numbers)
    zametnye = [c for c in numbers if c > srednee]
    zametnye_chet = [c for c in zametnye if c % 2 == 0]
    zametnye_nechet = [c for c in zametnye if c % 2 != 0]
    chet = [c for c in numbers if c % 2 == 0]
    nechet = [c for c in numbers if c % 2 != 0]
    if len(zametnye_chet) > len(zametnye_nechet) and sum(chet) < sum(nechet):
        count += 1
print(count)
