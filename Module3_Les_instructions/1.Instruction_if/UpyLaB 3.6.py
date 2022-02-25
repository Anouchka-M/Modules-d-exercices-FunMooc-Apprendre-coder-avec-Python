"""
Écrire un programme qui imprime la moyenne géométrique \sqrt{a.b} (la racine carrée du produit de a par b) de deux
nombres positifs a et b de type float lus en entrée.
Si au moins un de ces nombres est strictement négatif, le programme imprime le texte « Erreur ».
Exemple 1
Avec les données lues suivantes :
1.0
2.0
le résultat à imprimer vaudra approximativement  :
1.4142135623730951
Exemple 2
Avec les données lues suivantes :
-1.0
2.0
le résultat à imprimer vaudra :
Erreur
Consignes
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer
    que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et non
    float(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et
    non print("résultat:", res) par exemple).
"""

import math

a = float(input())
b = float(input())

if a < 0 or b < 0:
    print("Erreur")
else:
    print(math.sqrt(a * b))