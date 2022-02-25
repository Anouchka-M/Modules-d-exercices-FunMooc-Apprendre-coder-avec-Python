""" PAS ENCORE RESOLU

Écrivez un code qui lit un nombre entier strictement positif n et affiche sur n lignes une table de multiplication de
taille  n x n, avec, pour i entre 1 et n,  les n premières valeurs multiples de i strictement positives sur la ième
ligne.
Ainsi, les n premiers multiples de 1 strictement positifs (0 non compris) sont affichés sur la première ligne, les n
premiers multiples de 2 sur la deuxième, et cætera.
Exemple 1
Avec la valeur lue suivante :
3
le résultat à afficher sera :
1   2   3
2   4   6
3   6   9
Exemple 2
Avec la valeur lue suivante :
10
le résultat à afficher sera :
 1   2   3   4   5   6   7   8   9  10
 2   4   6   8  10  12  14  16  18  20
 3   6   9  12  15  18  21  24  27  30
 4   8  12  16  20  24  28  32  36  40
 5  10  15  20  25  30  35  40  45  50
 6  12  18  24  30  36  42  48  54  60
 7  14  21  28  35  42  49  56  63  70
 8  16  24  32  40  48  56  64  72  80
 9  18  27  36  45  54  63  72  81  90
10  20  30  40  50  60  70  80  90 100
Exemple 3
Avec la valeur lue suivante :
1
le résultat à afficher sera :
1
Consignes
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que
    le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un
    nombre : ")) par exemple), et à afficher précisément le résultat demandé.
    Il n'est pas requis que les nombres soient alignés verticalement. Pour cet exercice, UpyLaB ne tiendra pas compte
    du nombre d'espaces séparant les nombres sur chaque ligne, ni de la présence d'espace en fin de ligne.
"""

n = int(input())

for a in range(1, n + 1):
    for b in range(1, a + 1):
        print(b * a, end = ' ')
    print()