from turtle import *

bgcolor("light green")
color("blue")

now_speed = 3


def sqrfunc(size):
    global now_speed
    for i in range(4):
        fd(size)
        left(90)
        size += 5
        now_speed += 0.1
        speed(now_speed)


for i in range(6, 1200, 20):
    sqrfunc(i)

done()
