from turtle import forward, left, right, exitonclick
from fibonacci import fib_gen
from math import log



for i in fib_gen():
    for j in range(4):
        forward(log(20+i))
        left(90)
    left(10)
exitonclick()
