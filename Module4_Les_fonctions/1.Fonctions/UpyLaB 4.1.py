"""
Écrire une fonction deux_egaux(a, b, c) qui reçoit trois nombres en paramètre et qui renvoie la valeur booléenne True
si au moins deux de ces nombres ont la même valeur, et la valeur booléenne False sinon.
Ensuite, écrire un programme qui lit trois données de type int, x, y et z, et affiche le résultat de l’exécution de
deux_egaux(x, y, z).
Exemple 1
Avec les données lues suivantes :
1
2
3
le résultat à imprimer vaudra donc
False
Exemple 2
Avec les données lues suivantes :
42
6
42
le résultat à imprimer vaudra donc
True
Consignes
    Dans cet exercice, il vous est demandé d’écrire une fonction, puis un programme appelant cette fonction sur des
    valeurs lues en entrée. Notez qu’UpyLaB testera ces deux points, en exécutant le programme entier mais aussi en
    appelant directement la fonction avec les arguments de son choix.
    Plus précisément UpyLaB testera d'abord l'existence d'une définition deux_egaux avec le bon nombre de paramètres.
    Si la fonction existe bien, UpyLaB testera votre programme en ajoutant 2 appels à la fonction deux_egaux pour
    vérifier que celle-ci n'effectue aucun print.  C'est en effet à votre programme d'effectuer le print demandé.
    Ensuite différents tests de votre programme complet et de la fonction seront effectués par UpyLaB.
    Il n’est pas demandé que la fonction deux_egaux teste le type des paramètres reçus.
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que
    le résultat attendu. En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input())et non
    int(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non
    print("résultat :", res) par exemple).
    Quand UpyLaB teste spécifiquement le code d’une fonction (ici la fonction deux_egaux), le type du résultat est
    également validé. Veillez donc bien à renvoyer un résultat de type requis. En particulier, les objets True et "True"
    ne sont pas du même type.
"""

def deux_egaux(a, b, c):
    return a in (b, c) or b is c

a = int(input())
b = int(input())
c = int(input())

print (deux_egaux(a, b, c))
