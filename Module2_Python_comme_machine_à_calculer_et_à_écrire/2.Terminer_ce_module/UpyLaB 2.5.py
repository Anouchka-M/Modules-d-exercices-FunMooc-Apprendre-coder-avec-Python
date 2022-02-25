"""
Le but de cet exercice est de vous familiariser avec la syntaxe Python pour écrire des expressions arithmétiques
simples et avec l’instruction print qui affiche (on dit aussi imprime) des valeurs à l’écran.

Écrire un programme qui lit deux valeurs entières x et y strictement positives suivies de deux valeurs réelles
(float) z et t, et qui affiche les valeurs des expressions suivantes, chacune sur une nouvelle ligne :
    x - y
    x + z
    z + t
    x.z        (soit le produit de x et de z)
    \frac{x}{2}
    \frac{x}{y + 1}
    x^{-\frac{1}{2}}       (soit x à la puissance d'exposant -1/2)

Exemple

Avec les données lues suivantes :
2
1
3.0
3.5

le résultat à imprimer vaudra (approximativement pour la dernière valeur) :
1
5.0
6.5
6.0
1.0
1.0
1.125
0.7071067811865476

Consignes
    Il n’est pas demandé de tester si les valeurs de x et de y sont bien strictement positives.
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer
    que le résultat attendu. En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input())et
    non int(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et
    non print("résultat :", res) par exemple).
"""

x = int(input())
y = int(input())

z = float(input())
t = float(input())

print(x - y)
print(x + z)
print(z + t)
print(x * z)
print(x / 2)
print(x / (y + 1))
print(((x + y) * z) / (4 * x))
print(x ** (-1 / 2))