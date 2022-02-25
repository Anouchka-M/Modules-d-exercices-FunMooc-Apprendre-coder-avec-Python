"""
Écrire un programme qui lit 3 nombres entiers, et qui, si au moins deux d’entre eux ont la même valeur, imprime cette
valeur (le programme n’imprime rien dans le cas contraire).
Exemple 1
Avec les données lues suivantes :
2
1
2
le résultat à imprimer vaudra :
2
Exemple 2
Avec les données lues suivantes :
1
2
3
le programme n’affichera rien.
Exemple 3
Avec les données lues suivantes :
42
42
42
le résultat à imprimer vaudra :
42
Consignes

    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer
    que le résultat attendu.

    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer
    un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non
    print("résultat:", res) par exemple).
"""

value_1 = int(input())
value_2 = int(input())
value_3 = int(input())

if value_1 == value_2 or value_1 == value_3:
    print(value_1)
elif value_2 == value_3:
    print(value_2)