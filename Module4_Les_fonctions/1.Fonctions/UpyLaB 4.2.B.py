"""Il vous faut maintenant écrire un programme qui lit en entrée :
. l'heure de lever du soleil E1515
. l'heure du coucher du soleil E1515
. l'heure de lever du soleil E666
. l'heure du coucher du soleil E666
et qui utilise la fonction soleil_leve pour afficher ligne par ligne chacune des heures de la journée, depuis 0
jusqu'à 23, suivies d'une espace et d'une astérisque s'il fait nuit à cette heure.
Attention, il ne fera nuit que si E1515 et E666 sont tous deux couchés.
Exemple 1
Avec les données lues suivantes :
6
18
10
21
le résultat à imprimer vaudra donc
0 *
1 *
2 *
3 *
4 *
5 *
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21 *
22 *
23 *
Exemple 2
Avec les données lues suivantes :
15
8
6
17
le résultat à imprimer vaudra donc
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
Consignes
    N'oubliez pas d'insérer votre fonction soleil_leve.
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que
    le résultat attendu. En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input())et non
    int(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non
    print("résultat :", res) par exemple).
"""

def soleil_leve(a, b, c):
    return a <= c < b or a == b == 0 or c >= a > b or a > b > c

leve_E1515 = int(input())
couche_E1515 = int(input())
leve_E666 = int(input())
couche_E666 = int(input())

for h in range(0, 24):
    if soleil_leve(leve_E1515, couche_E1515, h) or soleil_leve(leve_E666, couche_E666, h):
        print(h)

    else:
        print(str(h) + " *")