from turtle import *

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
bgcolor("black")

speed(1000)

for x in range(500):
    pencolor(colors[x % 6])
    width(x // 100 + 1)
    forward(x)
    left(59)

done()
