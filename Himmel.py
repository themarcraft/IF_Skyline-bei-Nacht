from turtle import *
from random import *

pensize(2000)
a=1000000
penup()
right(90)
fd(-5)
pendown()
tracer(False)
for i in range(a):
    color(0.0,0.0,i/a)
    fd(0.01)
pensize(1)
bgcolor("black")
color("white")
def Mond():
    speed("fastest")
    color("white")
    penup()
    goto(75,200)
    pendown()
    begin_fill()
    circle(100)
    end_fill()
    penup()
    goto(125,200)
    pendown()
    color("black")
    begin_fill()
    circle(100)
    end_fill()
    penup()
Mond()
    
def Sterne():
    d = 6
    begin_fill()
    while d>0:
        forward(15)
        left(145)
        d = d-1
    end_fill()
color("white")
pendown()
sa = 0
while sa <110:
    x=randint(-900,900)
    y=randint(0,600)
    penup()
    goto(x,y)
    pendown()
    Sterne()
    sa = sa + 1
    
tracer(True)

