"""En mathématiques, et plus particulièrement en combinatoire, les nombres de Catalan forment une suite d’entiers
naturels utilisée dans divers problèmes de dénombrement.
Ils sont nommés ainsi en l’honneur du mathématicien belge Eugène Charles Catalan (1814-1894).
Les dix premiers nombres de Catalan (pour n de 0 à 9) sont :
1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862.
Le nombre de Catalan d’indice n, appelé n-ième nombre de Catalan, est défini par :
C_n = \frac{(2n)!}{(n+1)!n!}
où n! désigne la factorielle de la valeur entière n :
n! = n(n-1)(n-2)...1
Par exemple, 5! = 5.4.3.2.1 = 120 et
C_4 = \frac{8!}{5! 4!} = 14
Le nombre de chemins sous-diagonaux les plus courts dans une grille de taille {n}\times{n}, le nombre de façons de
découper en triangles un polygone convexe à n+2 côtés, ou encore le nombre de configurations possibles d’expressions
avec n paires de parenthèses, appelé également mot de Dyck de longueur 2n, sont des exemples dont le résultat est donné
par le nombre de Catalan C_n.
Exemples d’applications de \mathbf{C_n} (ici, n = 4)
    Nombre de chemins sous-diagonaux les plus courts dans une grille de taille {n}\times{n}
https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/chemins.jpg
    Nombre de façons de découper en triangles un polygone convexe de taille n + 2
https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/catalan_hexagone.jpg
    Nombre de parenthésages possibles (mots de Dyck)
(((())))
((()()))
((())())
(()(()))
()((()))
(()()())
((()))()
()(()())
(())(())
(()())()
(())()()
()(())()
()()(())
()()()()
Nous vous demandons d’écrire une fonction catalan(n), où n est un nombre entier positif ou nul, qui renvoie la valeur
du  n-ième nombre de Catalan.
Exemple 1
L'appel suivant de la fonction :
catalan(5)
doit retourner
42
Exemple 2
L'appel suivant de la fonction :
catalan(0)
doit retourner
1
Consignes
    Il n’est pas demandé que la fonction catalan teste le type du paramètre reçu.
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de votre fonction avec le bon nombre de
    paramètres.  Si la fonction existe bien, UpyLaB testera votre fonction : il ajoutera des appels à votre fonction
    pour vérifier que celle-ci n'effectue aucun print. Ensuite différents tests de votre fonction seront effectués par
    UpyLaB.
    Votre fonction doit renvoyer une valeur entière.
    Rappelons aussi que si une fonction est demandée, UpyLaB va tester à la fois que les résultats envoyés par cette
    fonction sont corrects et qu’ils ont le bon type.
"""

import math

def catalan(n):
    c_n = math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n))
    return int(c_n)

print(catalan(0))