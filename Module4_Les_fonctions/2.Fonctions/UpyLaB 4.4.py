"""
Écrire une fonction alea_dice(s) qui génère trois nombres (pseudo) aléatoires à l’aide de la fonction randint du module
random, représentant trois dés (à six faces avec les valeurs de 1 à 6), et qui renvoie la valeur booléenne True si les
dés forment un 421, et la valeur booléenne False sinon.
Le paramètre s de la fonction est un nombre entier, qui sera passé en argument à la fonction random.seed au début du
code de la fonction. Cela permettra de générer la même suite de nombres aléatoires à chaque appel de la fonction, et
ainsi de pouvoir tester son fonctionnement.
Exemple 1
L’appel suivant de la fonction :
alea_dice(1)
doit retourner :
False
Exemple 2
L’appel suivant de la fonction :
alea_dice(25)
doit retourner :
True
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction alea_dice. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de votre fonction avec le bon nombre de
    paramètres.  Si la fonction existe bien, UpyLaB testera votre fonction : il ajoutera des appels à votre fonction
    pour vérifier que celle-ci n'effectue aucun print. Ensuite différents tests de votre fonction seront effectués par
    UpyLaB.
    Il n’est pas demandé que la fonction alea_dice teste le type du paramètre reçu.
    N’importe quelle combinaison de trois dés permettant de former le nombre 421 sera acceptée, quel que soit l’ordre
    de la combinaison. Par exemple, les tirages 2, 4, 1 forment bien 421.
    La première instruction de la fonction, après l’import du module random, sera random.seed(s).
    On rappelle que la fonction randint(a, b) retourne un nombre (pseudo) aléatoire compris entre les bornes a et b
    incluses.
"""

import random

def alea_dice(s):
    """génère trois nombres aléatoires représentant trois dés à 6 faces
    renvoie True si les dés forment 421, False sinon"""
    random.seed(s) #permet de reproduire la même séquence pour tester le code
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)

    res = a + b + c
    return res == 7 and 4 in(a, b, c)

print(alea_dice(25))
print(alea_dice(1))