from turtle import *
from myTools import*
from random import*
tracer(False)
"zeichnet wasser"
color(0,0,0.2)
pensize(10)
hopp(-90,500)
hopp(180,1000)
begin_fill()
rechteck(2000,500)
end_fill()
"definiert die wellen mit farbe und zufallsposition"
def welle():
    color(0,0,0.35)
    penup()
    goto(randrange(-400,800),randrange(-500,0))
    pendown()
    pensize(randrange(3,7))
    fd(randrange(20,40))
"definiert den Baum mit Farbe"
def Baum():
    pensize(15)
    a=randrange(50,75)
    fd(randrange(50,100))
    right(90)
    color(0,0.05,0)
    begin_fill()
    fd(a*0.75)
    circle(a/4,90)
    fd(a/4)
    circle(a,180)
    fd(a/4)
    circle(a/4,90)
    fd(a*0.75)
    end_fill()
    color(0,0,0)
    left(90)
"zeichnet wellen"
for _ in range(25):
    welle()
"zeichnet Park"
penup()
goto(-1000,10)
pendown()

color(0,0.1,0)
begin_fill()
penup()
rechteck(1000,-510)
end_fill()
"zeichnet Weg"
goto(0,0)
pendown()
color(0.025,0.025,0.025)
pensize(30)
right(90)
fd(500)
penup()
pensize(100)
right(90)
fd(100)
right(90)
pendown()
fd(100)
left(35)
fd(100)
left(35)
fd(100)
right(70)
fd(100)
pensize(90)
left(45)
fd(100)
pensize(80)
fd(50)
pensize(70)
right(22.5)
fd(50)
right(22.5)
fd(25)
"zeichnet bäume mit Zufallsposition im Park"
baum=0
while baum<12:
    penup()
    goto(randrange(-1000,-20),randrange(-500,0))
    pendown()
    Baum()
    baum=baum+1

spiegelung=0
while spiegelung <500:
    pensize(5)
    color(0.6,0.6,0.1)
    penup()
    goto(randrange(15,1000),randrange(-300,0))
    pendown()
    fd(1)
    spiegelung=spiegelung+1
tracer(True)