"""
Écrire un programme qui teste la parité d’un nombre entier lu sur input et imprime True si le nombre est pair, False
dans le cas contraire.
Exemple 1
Avec la donnée lue suivante :
13
le résultat à imprimer vaudra :
False
Exemple 2
Avec la donnée lue suivante :
42
le résultat à imprimer vaudra :
True
Consignes
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer
    que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non
    int(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non
    print("résultat:", res) par exemple).
"""

print(int(input()) % 2 == 0)