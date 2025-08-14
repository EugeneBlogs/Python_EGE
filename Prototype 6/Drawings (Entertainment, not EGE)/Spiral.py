from turtle import *

bgcolor("orange")
color("green")

speed(100)

for i in range(100):
    circle(5 * i)
    circle(-5 * i)
    left(i)

done()
