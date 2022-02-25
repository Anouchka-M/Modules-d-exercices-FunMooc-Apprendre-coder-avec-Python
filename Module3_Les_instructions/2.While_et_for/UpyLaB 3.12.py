"""
Cet exercice propose une variante de l’exercice précédent sur le carré de X.
Écrire un programme qui lit en entrée une valeur naturelle n et qui affiche à l’écran un triangle supérieur droit formé
de X (voir exemples plus bas).
Exemple 1
Avec la donnée lue suivante :
6
le résultat à imprimer vaudra :
XXXXXX
 XXXXX
  XXXX
   XXX
    XX
     X
Exemple 2
Avec la donnée lue suivante :
2
le résultat à imprimer vaudra :
XX
 X
Consignes
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que
    le résultat attendu. En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input())et
    non int(input("Entrer un nombre : ")) par exemple).

    Il n’est pas demandé de tester si la valeur n est bien positive ou nulle, vous pouvez supposer que ce sera toujours
    le cas pour les valeurs transmises par UpyLaB.
"""

value = int(input())
X = value
blank = " "
blank2 = ""

for n in range(value):
    print(blank2 + "X" * X)
    blank2 = (blank2 + blank)
    X = X - 1