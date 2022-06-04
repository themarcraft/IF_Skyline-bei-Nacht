from turtle import *
print("myTools geladen von Marvin")
"""
    MyTools
    Autor: Marvin Niermann
    Erstelldatum: 18.02.2022
    Enthält:
        hopp: Springe eine Distanz ohne eine Linie zu hinterlassen
        parallel: Erstelle ein Parallelogramm
        vieleck: Erstelle eine Figur mit Ecken deiner Wahl
        viereck: Erstelle ein Viereck
        rechteck: Erstelle ein Rechteck
        dreieck: Erstelle ein Dreieck
        Rechtschreibkorrektur
"""
b=0
def hopp(winkel,distanz):
    penup()
    left(winkel)
    fd(distanz)
    right(winkel)
    pendown()
    print("erfolgreich",winkel,"Grad und",distanz,"pixel","gegangen")
def parallel(winkel,laenge,breite):
    for _ in range(2):
        fd(laenge)
        left(winkel)
        fd(breite)
        left(180-winkel)
def vieleck(anzahl,laenge):
    for _ in range(anzahl):
        left(360/anzahl)
        fd(laenge)
def viereck(laenge):
    """
    for i in range(2):
        penup()
        fd(laenge)
        left(90)
        pendown()
        fd(laenge)
        left(90)"""
    parallel(90,laenge,laenge)
def rechteck(laenge,breite):
    parallel(90,laenge,breite)
def dreieck(laenge):
    for _ in range(3):
        pendown()
        left(120)
        fd(laenge)
pensize(20)
def vielecka(anzahl,laenge):
    for i in range(anzahl):
        left(360/anzahl)
        for _ in range(laenge):
            color(0.01*i,0.0,1/i)
            fd(1)
"""
    Extra Korrektur
"""
def forwerd(a):
    fd(a)
def raight(b):
    right(b)
def läft(c):
    left(c)
def fiereck(laenge):
    parallel(90,laenge,laenge)
def vireck(laenge):
    parallel(90,laenge,laenge)