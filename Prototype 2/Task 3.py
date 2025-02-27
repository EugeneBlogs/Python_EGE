# Условие задания КИМ 2 (Умскул):
'''
Логическая функция задана выражением ((w → x) ≡ (z → y)) ∧ (¬y ∨ w),
а у нас есть неполная таблица истинности (содержит не все наборы аргументов и значений, котоая приведена ниже.

?   ?   ?   ?   F
_   0   0   _   1
0   0   _   0   1
1   1   1   _   0

Запишите в ответ имена переменных в том порядке, в котором они идут по таблице.
'''

print('x y z w | F')
print('-----------')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                F = int(((w <= x) == (z <= y)) and (
                            (not (y)) or w))  # Записываем результат и приводим к единому значению INT
                print(x, y, z, w, "|", F)
'''
1. В таблице в условии только одна строчка с результатом 0.
Убираем все лишние строчки (с результатом 0), которые не подходят по условию (менее трёх единиц).
2. Убираем все лишние строчки с результатом 1, которые не подходят по условию (менее двух нулей).
3. Попробуем заполнить пропуски в таблице:
(для объяснения мы их обозначили буквами, во время решения это делать не нужно)

На месте пропуска "A" точно 1 (если поставить 0, то будет 2 одинаковых столбика: первый и второй)
На месте пропуска "C" точно 1 (если поставить 0, то будет 2 одинаковых столбика: второй и третий)
На месте пропуска "D" точно 0 (если поставить 1, то на месте пропуска B мы ставим либо 0, либо 1;
если ставим 0, то будет 2 одинаковых столбика: второй и четвёртый, если ставим 1, то будет 2 одинаковых столбика: первый и четвёртый)

?   ?   ?   ?   F
A   0   0   B   1
0   0   C   0   1
1   1   1   D   0

Теперь таблица выглядит так:

?   ?   ?   ?   F
1   0   0   _   1
0   0   1   0   1
1   1   1   0   0

4. Убираем строчку "0 0 0 0 | 1", так как в каждой строке есть хотя бы одна единица.
5. Заметим, что вторая строчка таблицы условия имеет одну единицу, и она истина.
Находим данную строчку в наших строчках и понимаем, что данная единица - это "x".
6. Убираем строчку "0 1 1 1 | 0", так как в третьей строчке таблицы условия "x" = 1, а здесь = 0.
7. Находим строчки "0 0 1 1 | 1" и "1 0 0 1 | 1".
Нам подходит первый вариант, так как в первой строчке таблицы условия "x" = 0.
Поэтому если мы имеем 2 нуля, то второй ноль - это "y".
8. Находим строчки "1 0 1 1 | 0" и "1 1 1 0 | 0".
Нам подходит второй вариант, так как в третьей строчке таблицы условия "y" = 1.
В данной строке 1 нуль - это "w".
9. Методом исключения остаётся "z".

Ответ: zyxw. 
'''
