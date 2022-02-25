""" auteur: Thierry Massart
    date : 10 avril 2018
    but du programme : trace avec turtle des spirales
"""

import turtle

def spirale(couleur, largeur):
    """ Dessine avec turtle une spirale
    paramètres :
    - couleur : la couleur à utiliser
    - largeur : la largeur du tracé"""

    turtle.color(couleur)
    turtle.width(largeur)
    for i in range(100):
        turtle.circle(i*(largeur/2),90)

while True:
    turtle.reset()
    turtle.speed(0)
    spirale('red', 10)