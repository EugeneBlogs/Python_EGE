# Условие задания (Гусева Марина Альфонсовна, "Решу ЕГЭ"):
'''
В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
Определите и запишите в ответе сначала количество пар элементов последовательности, разность которых четна
и хотя бы одно из чисел делится на 31, затем максимальную из сумм элементов таких пар.
В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.
'''

file = open("2.txt")
data = file.readlines()
count = 0
max_sum = -1000000000
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        a, b = int(data[i]), int(data[j])
        if (a - b) % 2 == 0 and (a % 31 == 0 or b % 31 == 0):
            count += 1
            max_sum = max(max_sum, a + b)
print(count)
print(max_sum)
