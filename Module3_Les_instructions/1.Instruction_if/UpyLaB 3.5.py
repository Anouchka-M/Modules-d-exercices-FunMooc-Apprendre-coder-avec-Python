"""
Écrire un programme qui lit en entrée deux nombres entiers strictement positifs, et qui vérifie qu’aucun des deux
n’est un diviseur de l’autre.
Si tel est bien le cas, le programme imprime True. Sinon, il imprime False.
Exemple 1
Avec les données lues suivantes :
6
42
le résultat à imprimer vaudra :
False
Exemple 2
Avec les données lues suivantes :
5
42
le résultat à imprimer vaudra :
True
Consignes
    Notez qu’il n’est pas demandé de vérifier que les deux nombres en entrée sont strictement positifs. Vous pouvez
    supposer que ce sera le cas pour toutes les entrées proposées par UpyLaB lors des tests.
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer
    que le résultat attendu. En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et
    non int(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non
    print("résultat :", res) par exemple).
"""

a = int(input())
b = int(input())

print(not (a % b == 0 or b % a == 0))