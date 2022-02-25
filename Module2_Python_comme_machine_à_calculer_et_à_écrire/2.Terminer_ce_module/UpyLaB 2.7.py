"""
Écrire un programme qui imprime la valeur du volume d’une sphère de rayon r, float lu en entrée.
On rappelle que le volume d’une sphère de rayon r est donné par la formule : \frac{4}{3}\pi{r^3}
Exemple 1
Avec la donnée lue suivante :
1.0
le résultat à imprimer vaudra (approximativement) :
4.1887902047863905
Exemple 2
Avec la donnée lue suivante :
0.5
le résultat à imprimer vaudra (approximativement) :
0.5235987755982988
Consignes
    Il n’est pas demandé de tester si la valeur lue en entrée est bien positive ou nulle.
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer
    que le résultat attendu. En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input())
    et non float(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res)
    et non print("résultat :", res) par exemple).
    Pour rappel, en Python, l’opérateur exposant est **. Ainsi, 2 ** 3 vaut 8 soit 2 * 2 * 2.
"""

import math

r = float(input())
print(4 / 3 * math.pi * r ** 3 )
