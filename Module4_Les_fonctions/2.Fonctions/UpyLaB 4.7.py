"""
Écrire une fonction rac_eq_2nd_deg(a, b, c) qui reçoit trois paramètres de type float correspondant aux trois
coefficients de l’équation du second degré ax^2 + bx + c = 0, avec a différent de 0, et qui renvoie la ou les solutions
s’il y en a, sous forme d’un tuple.
Exemple 1
L’appel suivant de la fonction :
rac_eq_2nd_deg(1.0,-4.0,4.0)
doit retourner :
(2.0,)
Exemple 2
L’appel suivant de la fonction :
rac_eq_2nd_deg(1.0,1.0,-2.0)
doit retourner :
(-2.0, 1.0)
Exemple 3
L’appel suivant de la fonction :
rac_eq_2nd_deg(1.0,1.0,1.0)
doit retourner :
()
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction rac_eq_2nd_deg. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de votre fonction avec le bon nombre de
    paramètres.  Si la fonction existe bien, UpyLaB testera votre fonction : il ajoutera des appels à votre fonction
    pour vérifier que celle-ci n'effectue aucun print. Ensuite différents tests de votre fonction seront effectués par
    UpyLaB.
    Il n’est pas demandé que la fonction rac_eq_2nd_deg teste le type des paramètres reçus.
    Le résultat retourné par la fonction rac_eq_2nd_deg est un tuple.
            S’il n’y a pas de solution réelle, elle retourne un tuple vide tuple().
            S’il y a une unique racine r1, elle retourne le tuple (r1,).
            S’il y a deux solutions réelles, r1 et r2, la plus petite des deux devra être la première composante du
            tuple retourné (composante d’indice 0). La fonction pourra retourner le tuple (min(r1, r2), max(r1, r2)).
"""

import math

def rac_eq_2nd_deg(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return ()
    elif delta == 0:
        r1 = (- b) / (2 * a)
        return (r1, )
    elif delta > 0:
        r = (((- b) - (math.sqrt(delta))) / (2 * a), ((- b) + (math.sqrt(delta))) / (2 * a))
        r = sorted(r)
        return tuple(r)

print (rac_eq_2nd_deg(-1.0, 4.5, -4.5))