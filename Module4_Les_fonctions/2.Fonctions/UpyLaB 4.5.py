""" PAS ENCORE RESOLU

Considérons les billets et pièces de valeurs suivantes : 20 euros, 10 euros, 5 euros, 2 euros et 1 euro.
Écrire une fonction rendre_monnaie qui reçoit en paramètre un entier prix et cinq valeurs entières x20, x10, x5, x2 et
x1, qui représentent le nombre de billets ou de pièces de chaque valeur que donne un client pour l’achat d’un objet
dont le prix est mentionné.
La fonction doit renvoyer cinq valeurs, représentant le nombre de billets et pièces de chaque sorte qu’il faut rendre
au client, dans le même ordre que précédemment. Cette décomposition doit être faite en rendant le plus possible de
billets et pièces de grosses valeurs.
Si la somme d’argent avancée par le client n’est pas suffisante pour effectuer l’achat, la fonction retournera cinq
valeurs None.
Exemple 1
L’appel suivant de la fonction :
rendre_monnaie(38, 1, 1, 1, 1, 1)
doit retourner :
(0, 0, 0, 0, 0)
Exemple 2
L’appel suivant de la fonction :
rendre_monnaie(56, 5, 0, 0, 0, 0)
doit retourner :
(2, 0, 0, 2, 0)
Exemple 3
L’appel suivant de la fonction :
rendre_monnaie(80, 2, 2, 2, 3, 3)
doit retourner :
(None, None, None, None, None)
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction rendre_monnaie. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de votre fonction avec le bon nombre de
    paramètres.  Si la fonction existe bien, UpyLaB testera votre fonction : il ajoutera des appels à votre fonction
    pour vérifier que celle-ci n'effectue aucun print. Ensuite différents tests de votre fonction seront effectués par
    UpyLaB.
    Il n’est pas demandé que la fonction rendre_monnaie teste le type des paramètres reçus.
    On suppose qu’il y a toujours suffisamment de billets et pièces de chaque sorte.
    Pour retourner cinq valeurs, on pourra utiliser l’instruction return res20, res10, res5, res2, res1.
    Cela renvoie un tuple de cinq valeurs (apparaissant entre parenthèses lorsqu’on l’affiche).
"""

def rendre_monnaie(prix, a, b, c, d, e):
    """Renvoie 5 valeurs représentant le nombre de billets et
    pièces de chaque sorte qu'il faut rendre au client"""
    while a > 0 and prix > 0:
        a -= 1
        prix -= 20
    while b > 0 and prix > 0:
        b -= 1
        prix -= 10
    while c > 0 and prix > 0:
        c -= 1
        prix -= 5
    while d > 0 and prix > 0:
        d -= 1
        prix -= 2
    while e > 0 and prix > 0:
        e -= 1
        prix -= 1
    if prix > 0:
        return (None, None, None, None, None)
    else:
        return (a, b, c, d, e)

print(rendre_monnaie(80, 2, 2, 2, 3, 3))