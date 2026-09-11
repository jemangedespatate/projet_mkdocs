from turtle import *

def maison():
    # place la structure de la maison
    placement(0,0)
    structure(100)
    placement(0,0)
    
    # place la fenetre e bas a gauche de la maison
    placement(20,20)    
    fenetre(20,10)
    placement(0,0)

    # place la fenetre en haut a gauche de la maison
    placement(20,60)    
    fenetre(20,10)
    placement(0,0)    
    
    # place la fenetre en haut a droite de la maison
    placement(70,60)    
    fenetre(20,10)
    placement(0,0)
    
    # place la porte en bas a droite de la maison
    placement(50,0)
    porte(40,20)
    placement(0,0)

    # place le toit au dessus de la maison
    placement(0,100)
    toit(100)
    placement(0,0)
    
def structure(longeur):
    # crée la base de la maison
    for i in range(4):
        forward(longeur)
        left(90)
    
def fenetre(longeur,largeur):
    # crée une fenetre avec les longeur et largeur des coté sont spécifier
    for i in range(2):
        forward(largeur)
        left(90)
        forward(longeur)
        left(90)
    
def porte(longeur,largeur):
    # crée une porte avec les longeur et largeur des coté sont spécifier
    for i in range(2):
        forward(largeur)
        left(90)
        forward(longeur)
        left(90)

def toit(longeur):
    # crée un toit dont la longeur des coté est specifier
    for i in range(3):
        forward(longeur)
        left(120)

def placement(x,y):
    penup()
    setpos(x,y)
    pendown()

maison()