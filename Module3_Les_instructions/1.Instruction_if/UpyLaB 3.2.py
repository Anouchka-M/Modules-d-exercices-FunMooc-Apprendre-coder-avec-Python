"""
Écrire un programme qui, si temperature (entier lu sur input correspondant à la température maximale prévue pour
aujourd’hui) est strictement supérieur à 0, teste si temperature est inférieur ou égal à 10, auquel cas il imprime
le texte :
    Il va faire frais.
et qui, si temperature n’est pas supérieur à 0, imprime le texte :
    Il va faire froid.
Dans les autres cas, le programme n’imprime rien.
Exemple 1
Avec la donnée lue suivante :
1
le résultat à imprimer vaudra :
Il va faire frais.
Exemple 2
Avec la donnée lue suivante :
20
le programme n’affichera rien.
Exemple 3
Avec la donnée lue suivante :
-1
le résultat à imprimer vaudra :
Il va faire froid.
Consignes
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer
    que le résultat attendu. En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input())et
    non int(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non
    print("résultat :", res) par exemple).
    Faites attention d’écrire les messages à l’identique de ce qui est demandé (majuscule au début de la ligne, une
    espace entre chaque mot, etc) . Un conseil pour avoir des messages identiques est de les copier de l’énoncé pour
    les coller dans votre code.
    Lors de l’affichage des résultats, en cas d’erreur dans certains tests, UpyLaB pourra marquer : « Le résultat
    attendu était : aucun résultat ». Cela voudra bien dire qu’il ne faut rien imprimer dans ce cas.
"""

temperature = int(input())

if 0 < temperature <= 10:
    print("Il va faire frais.")
elif not temperature > 0:
    print("Il va faire froid.")