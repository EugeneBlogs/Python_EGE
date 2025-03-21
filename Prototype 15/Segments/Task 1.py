# Условие задания КИМ 15 (Умскул):
'''
На числовой прямой даны два отрезка: D = [17; 58] и С = [29; 80].
Укажите наименьшую возможную длину такого отрезка "A", для которого логическое выражение
(x ∈ D) ⟶ ((¬ (x ∈ C) ∧ ¬ (x ∈ A)) ⟶ ¬(x ∈ D))
истинно (т.е. принимает значение 1) при любом значении переменной "x".
'''

# Получаем списки чисел "D" и "C" из диапозонов (включительно, поэтому прибавляем справа 1)
D = list(range(17, 58 + 1))
C = list(range(29, 80 + 1))
A = []  # Создаём пустой список "A", потому что нам нужна наименьшая длина (самая маленькая длина - это ничего)
for x in range(1, 100):  # Перебираем все "x" в диапозоне, чтобы входили все числа из условий (например, от 1 до 100)
    # Если условие ложно, то есть данное "A" нужно брать, то добавляем его в список
    if not ((x in D) <= (((not (x in C)) and (not (x in A))) <= (not (x in D)))):
        A.append(x)
print(A)

'''
Вывод: [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
17 - есть в условии, значит всё в порядке.
28 - нет в условии, ближайшее к нему - 29.
Значит наш отрезок от 17 до 29 ИЛИ [17; 29].
Длина данного отрезка: 29 - 17 = 12.
Ответ: 12.
'''
