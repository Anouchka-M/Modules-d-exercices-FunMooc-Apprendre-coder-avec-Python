"""
Écrire une fonction longueur(*points) qui reçoit en paramètres un nombre arbitraire de points (tuples de deux
composantes), et retourne la longueur de la ligne brisée correspondante.
Cette longueur se calcule en additionnant les longueurs des segments formés par deux points consécutifs.
Exemple 1
L’appel suivant de la fonction :
longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0))
doit retourner :
2.0
Exemple 2
L’appel suivant de la fonction :
longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0))
doit retourner (approximativement) :
7.1122677042334645
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction longueur. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à
    print.
    Pour simplifier, on supposera qu’il y aura toujours au moins deux points passés en paramètre lors des appels à la
    fonction longueur.
    Il est conseillé d’utiliser la fonction distance_points définie lors de l’exercice précédent.
"""

import math

def longueur(*points):
    res = 0.0
    for i in range(1, len(points)):
        x_1 = points[i - 1][0] - points[i][0]
        y_1 = points[i - 1][1] - points[i][1]
        res += math.sqrt((points[i - 1][0] - points[i][0]) ** 2 + (points[i - 1][1] - points[i][1]) ** 2)
    return res

print(longueur((-1.0, 0.5), (2.0, 1.0)))
print(longueur((1.0, 1.0), (2.0, 1.0)) + longueur((2.0, 1.0), (3.0, 1.0)))
print(longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)))
print(longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0)))