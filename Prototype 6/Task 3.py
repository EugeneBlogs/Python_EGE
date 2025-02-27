# Условие задания КИМ 6 (Умскул):
'''
Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат,
её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии.
В каждый конкретный момент известно положение исполнителя и направление его движения.
У исполнителя существует 6 команд:
- Поднять хвост, означающая переход к перемещению без рисования.
- Опустить хвост, означающая переход в режим рисования.
- Вперёд n (где "n" - целое число), вызывающая передвижение Черепахи на "n" единиц в том направлении, куда указывает её голова.
- Назад n (где "n" - целое число), вызывающая передвижение в противоположном голове направлении.
 - Направо m (где "m" - целое число), вызывающая изменение направления движения на "m" градусов по часовой стрелке.
 - Налево m (где "m" - целое число), вызывающая изменение направления движения на "m" градусов против часовой стрелки.

Запись "Повтори k [Команда1 Команда2... Команда]" означает, что последовательность из "S" команд повторится "k" раз.

Черепахе был дан для исполнения следующий алгоритм:
"Направо 90
Повтори 3 [Направо 45 Вперёд 12 Направо 45]
Направо 315 Вперёд 12
Повтори 2 [Направо 90 Вперёд 12]".

Определите, сколько точек с целочисленными координатами будут находиться внутри области, которая ограничена линией,
заданной алгоритмом. Точки на линий учитывать не следует.
'''

from turtle import *

tracer(0)
k = 100
left(90)

pendown()
begin_fill()
right(90)
for _ in range(3):
    right(45)
    forward(12 * k)
    right(45)
right(315)
forward(12 * k)
for _ in range(2):
    right(90)
    forward(12 * k)
end_fill()
penup()

count = 0
canvas = getcanvas()
for x in range(-300, 300):
    for y in range(-300, 300):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            count += 1
print(count)
