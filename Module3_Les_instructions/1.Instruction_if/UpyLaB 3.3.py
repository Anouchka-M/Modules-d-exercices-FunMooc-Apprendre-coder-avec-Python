"""
Écrire un programme qui lit trois entiers a, b et c en input. Ensuite :
    si l’entier c est égal à 1, alors le programme affiche la valeur de a + b ;
    si c vaut 2, alors le programme affiche la valeur de a - b ;
    si c est égal à 3, alors l’output sera la valeur de a.b (produit de a par b) ;
    enfin, si la valeur 4 est assignée à la variable c, alors le programme affiche la valeur de a^2 + a.b ;
    et si c contient une autre valeur, le programme affiche le message Erreur.
Exemple 1
Avec les données lues suivantes :
3
2
1
le résultat à imprimer vaudra :
5
Exemple 2
Avec les données lues suivantes :
3
2
4
le résultat à imprimer vaudra :
15
Exemple 3
Avec les données lues suivantes :
3
2
5
le résultat à imprimer vaudra :
Erreur
Consignes
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer
    que le résultat attendu en respectant l’orthographe, les majuscules / minuscules, les espacements, etc.

    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer
    un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non
    print("résultat:", res) par exemple).
"""

a = int(input())
b = int(input())
c = int(input())

if c == 1:
    print(a + b)
elif c == 2:
    print(a - b)
elif c == 3:
    print(a * b)
elif c == 4:
    print(a**2 + a * b)
else:
    print("Erreur")
