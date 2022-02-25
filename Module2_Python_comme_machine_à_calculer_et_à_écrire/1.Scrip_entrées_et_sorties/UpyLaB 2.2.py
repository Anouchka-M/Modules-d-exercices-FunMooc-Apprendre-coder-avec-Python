"""
Le but de cet exercice est de vérifier que vous savez lire des données en entrée avec la fonction input, les affecter
à des variables et imprimer (on dit aussi afficher) une valeur grâce à la fonction print.

Écrire un programme qui imprime (donc grâce à la fonction print) la moyenne arithmétique de deux nombres de type float
lus en entrée (c'est-à-dire grâce à des appels à la fonction input) .

On rappelle que la moyenne arithmétique de deux nombres a et b est égale à  \frac{a+b}{2}.
Exemple 1

Avec les données lues suivantes :
2.0
3.0

le résultat à imprimer vaudra :
2.5

Exemple 2

Avec les données lues suivantes :
4.2
3.8

le résultat à imprimer vaudra :
4.0

Consignes

Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que
le résultat attendu.

En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et non float(input("Entrer
un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat :", res)
par exemple).
"""

a = input()
b = input()
a = float(a)
b = float(b)
print((a + b) / 2)