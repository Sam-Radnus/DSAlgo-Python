import turtle
import random
import time
from Polygon import *

t = turtle.Turtle()


def radialPattern(t,n,length,shape):
    for count in range(n):
        shape(t,length)
        t.left(360/n)

radialPattern(t, 15, 50, square)
time.sleep(3)
t.clear()
