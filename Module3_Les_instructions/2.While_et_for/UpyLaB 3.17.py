""" PAS ENCORE RESOLU

On peut calculer approximativement le sinus d’un nombre x en effectuant la sommation des premiers termes de la série
(une série est une somme infinie) :
sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + ...
où x est exprimé en radians et 3! désigne la factorielle de 3.
Écrire un programme qui lit une valeur flottante x en entrée et imprime une approximation de sin(x)
Cette approximation sera obtenue en additionnant successivement les différents termes de la série jusqu’à ce que la
valeur du terme devienne inférieure (en valeur absolue) à une constante \epsilon que l’on fixera à 10^{-6}.
Exemple 1
Avec les données lues suivantes :
0.8
le résultat à imprimer vaudra  :
0.7173557231746032
Remarque : Du fait du manque de précision dans les calculs avec les nombres de type float, votre résultat pourra
différer de celui indiqué ci-dessus. Ce n'est pas un problème, car UpyLaB acceptera toute réponse suffisamment proche
du résultat attendu, avec une tolérance d'environ 1.0e-5.
Exemple 2
Avec les données lues suivantes :
-0.5
le résultat à imprimer vaudra  :
-0.479425533234127
Consignes
    Nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le
    résultat attendu. En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et
    nonfloat(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et
    non print("résultat :", res) par exemple).
"""

j = 2
for i in range(4):
    print(i)
    j = j + 2
