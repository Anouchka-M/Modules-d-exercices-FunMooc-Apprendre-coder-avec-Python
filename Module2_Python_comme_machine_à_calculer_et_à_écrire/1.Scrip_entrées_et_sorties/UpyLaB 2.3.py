""" Le but de cet exercice est de vous familiariser avec la lecture (input()) de données et l’impression (print())
de résultats.
Une méthode pour trouver le quatrième terme parmi quatre termes ayant un même rapport de proportion
\frac{a}{b} = \frac{c}{d} lorsque trois de ces termes sont connus repose sur l'égalité des produits en croix.

Elle utilise le fait que le produit des premier et quatrième termes est égal au produit du second et du troisième :
a.d = b.c et donc d = \frac{b.c}{a}
Exemple : si chacun mange autant de chocolat et que pour 4 personnes il en faut 100 grammes, pour 7 personnes il en
faudra donc d tel que \frac{4}{100} = \frac{7}{d}

D’où d = \frac{7.100}{4} grammes = 175 grammes.
Écrire un programme qui lit des valeurs de type float pour a, b et c et qui affiche la valeur de d vérifiant
l'égalité \frac{a}{b} = \frac{c}{d}.
Exemple 1

Avec les données lues suivantes :
4.0
100.0
7.0

le résultat à imprimer vaudra :
175.0

Exemple 2

Avec les données lues suivantes :
3.5
0.5
8.0

le résultat à imprimer vaudra :
1.1428571428571428

Remarque : Du fait du manque de précision dans les calculs avec les nombres de type float, votre résultat
pourra différer de celui indiqué ci-dessus. Ce n'est pas un problème, car UpyLaB acceptera toute réponse suffisamment
proche du résultat attendu, avec une tolérance d'environ 1.0e-5.
Consignes

Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le
résultat attendu.

En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et non float(input("Entrer un
nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat :", res)
par exemple).
"""

a = float(input())
b = float(input())
c = float(input())
d = (b * c) / a
print(d)