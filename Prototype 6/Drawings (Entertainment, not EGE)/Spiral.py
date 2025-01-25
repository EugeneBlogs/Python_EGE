from turtle import *

speed(100)

for i in range(100):
    circle(5 * i)
    circle(-5 * i)
    left(i)

done()
