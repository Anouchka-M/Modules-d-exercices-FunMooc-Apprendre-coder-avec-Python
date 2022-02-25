"""
Les cinq polyèdres réguliers de Platon sont représentés ci-dessous, avec la formule de leur volume.
Source des images de polyèdres : Vikidia, l’encyclopédie pour les jeunes, qui explique aux enfants et à ceux qui
veulent une présentation simple d'un sujet (https://fr.vikidia.org/wiki/Polyèdre).
Écrire un programme qui lit :
    la première lettre en majuscule du nom du polyèdre ("T", "C", "O", "D" ou "I"),
    la longueur de l’arête du polyèdre,
et qui imprime le volume du polyèdre correspondant.
Si la lettre lue ne fait pas partie des cinq initiales, le programme imprime le message "Polyèdre non connu".
Exemple 1
Avec les données lues suivantes :
C
2.0
le résultat à imprimer vaudra :
8.0
Exemple 2
Avec les données lues suivantes :
I
2.0
le résultat à imprimer vaudra (approximativement) :
17.4535599249993
Exemple 3
Avec les données lues suivantes :
A
2.0
le résultat à imprimer vaudra :
Polyèdre non connu
Consignes
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer
    que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et non
    float(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et
    non print("résultat:", res) par exemple).
"""

import math

polyedre = str(input())
a = float(input())

if polyedre == "T":
    print(f"T\n" and math.sqrt(2) / 12 * a ** 3)

elif polyedre == "C":
    print(f"C\n" and a ** 3)

elif polyedre == "O":
    print(f"O\n" and math.sqrt(2) / 3 * a** 3)

elif polyedre == "D":
    print(f"D\n" and (15 + 7 * math.sqrt(5)) / 4 * (a ** 3))

elif polyedre == "I":
    print(f"I\n" and 5 * (3 + math.sqrt(5)) / 12 * (a ** 3))

else:
    print("Polyèdre non connu")
