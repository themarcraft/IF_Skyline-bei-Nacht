from turtle import *
from myTools import *
from random import randrange
print(randrange(10))
bgcolor("black")
"""
    Befehl um Haus zu bauen
"""
def haus(höhe):
    pensize(1)
    s = pos()
    color(0.11,0.11,0.11)
    for _ in range(höhe*9):
        a = pos()
        penup()
        goto(a)

        penup()
        left(90)
        fd(5)
        right(90)
        """
            Fenster
        """
        for _ in range(9):
            gg = randrange(0,3)
            if(gg==1):
                fillcolor("yellow")
            else:
                fillcolor("black")
            fd(5)
            pendown()
            begin_fill()
            rechteck(2,4)
            penup()
            end_fill()
        fd(-45)
    """
        Der Rahmen folgt:
    """
    goto(s)
    left(90)
    pendown()
    pensize(5)
    fd(5*höhe*9+2)
    print(5*höhe*9)
    left(-90)
    fd(4)
    fd(5*9)
    penup()
    goto(s)
    pendown()
    fd(5*9+6)
    left(90)
    fd(5*höhe*9+2)
    penup()
    """
        Zum Nächstem Haus
    """
    goto(s)
    left(-90)
    fd(75)
tracer(False)
goto(-1000,-100)
"""
    Befhel für zufällige Häuser
"""
def rand(a):
    for h in range(a):
        """
            Mond Soll nicht von Häuser verdeckt sein
        """
        if((h==14)or(h==15)):
            haus(4)
        else:
            haus(randrange(5,13))
"""
    Häuser Zufällig Bauen
"""
rand(30)
tracer(True)