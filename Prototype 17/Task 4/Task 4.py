# Условие задания (Гусева Марина Альфонсовна, "Решу ЕГЭ"):
'''
В файле содержится последовательность натуральных чисел. Элементы последовательности могут принимать целые значения
от 1 до 100000 включительно. Определите количество пар элементов последовательности, в которых сумма остатков от деления
обоих элементов на 18 равна минимальному элементу последовательности. В ответе запишите количество найденных пар,
затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд
элемента последовательности.
'''

file = open("4.txt")
data = file.readlines()
count = 0
max_sum = -1000000000
min_number = 10 ** 10
for el in data:
    min_number = min(int(el), min_number)
for i in range(len(data) - 1):
    a, b = int(data[i]), int(data[i + 1])
    if ((a % 18) + (b % 18)) == min_number:
        count += 1
        max_sum = max(max_sum, a + b)
print(count)
print(max_sum)
