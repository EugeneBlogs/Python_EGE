from turtle import *
import math


def xt(t):
    return 16 * math.sin(t) ** 3


def yt(t):
    return 13 * math.cos(t) - 5 \
        * math.cos(2 * t) - 2 * \
        math.cos(3 * t) - math.cos(4 * t)


speed(500)
colormode(255)
Screen().bgcolor(0, 0, 0)
for i in range(2550):
    goto((xt(i) * 20, yt(i) * 20))
    pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
    goto(0, 0)
hideturtle()
update()
mainloop()
