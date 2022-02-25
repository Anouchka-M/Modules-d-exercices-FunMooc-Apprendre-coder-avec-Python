"""
Dans cet exercice, nous allons mettre en pratique la notion de valeur par défaut des paramètres d’une fonction.
Écrire une fonction somme(a, b) qui retourne la somme de deux valeurs entières a et b. Par défaut, la valeur de a est 0
et la valeur de b est 1.
Exemple 1
L’appel suivant de la fonction :
somme(24, 18)
doit retourner :
42
Exemple 2
L’appel suivant de la fonction :
somme(4)
doit retourner :
5
Exemple 3
L’appel suivant de la fonction :
somme()
doit retourner :
1
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction somme. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou
    à print.
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de votre fonction avec le bon nombre de
     paramètres.  Si la fonction existe bien, UpyLaB testera votre fonction : il ajoutera des appels à votre fonction
     pour vérifier que celle-ci n'effectue aucun print. Ensuite différents tests de votre fonction seront effectués
     par UpyLaB.
    Il n’est pas demandé que la fonction somme teste le type des paramètres reçus.
"""

def somme(a = 0, b = 1):
    return a + b

print (somme(4))