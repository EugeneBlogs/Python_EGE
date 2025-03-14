# Условие задания КИМ 25 (Гусева Марина Альфонсовна, "Решу ЕГЭ"):
'''
Пусть "M(N)" - пятый по величине делитель натурального числа "N" без учёта самого числа и единицы.
Например, "M(1000) = 100".
Если у числа "N" меньше 5 различных делителей, не считая единицы и самого числа,
считаем, что "M(N) = 0".
Найдите 5 наименьших натуральных чисел, превышающих 300.000.000, для которых "M(N) > 0".
В ответе запишите найденные значения "M(N)" в порядке возрастания соответствующих им чисел "N".

Примечание.
Пятый по величине делитель - пятый делитель из пяти наибольших делителей числа.
То есть для числа 1000 пять наибольших делителей, не считая единицы и самого числа: 500, 250, 200, 125, 100, пятый по величине - 100.
'''

result = []
num = 300000001
while len(result) != 5:
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1
            if count == 5:
                result.append(num // i)
                break
    num += 1
print(result)
