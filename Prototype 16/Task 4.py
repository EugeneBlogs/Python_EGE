# Условие задания КИМ 16 (Умскул):
'''
Алгоритм вычисления значения функции "F(n)", где "n" - натуральное
число, задач следующими соотношениями:
"F(n) = 1" при "n = 1";
"F(n) = 3 * n + F(n - 1)", если "n > 1".
Чему равно значение "F(124352)"?
'''

# Из-за больших чисел, легко превысить лимит рекурсии,
# поэтому будет использовать списки

F = [0] * 130000  # Создаём большой список, заполненный нулями
# Циклом обновляем все значения массива в зависимости от условия
for n in range(130000):
    if n == 1:
        F[n] = 1
    elif n > 1:
        F[n] = 3 * n + F[n - 1]
print(F[124352])
