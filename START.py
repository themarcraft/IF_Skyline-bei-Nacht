from myTools import *
tracer(False)
from Himmel import *
penup()
seth(0)
goto(0,0)
from Häuser import *
penup()
seth(0)
goto(0,0)
from Wasser import *
tracer(True)
penup()
speed(100)
goto(-1000,0)
pendown()
fd(3000)