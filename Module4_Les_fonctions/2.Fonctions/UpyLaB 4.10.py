"""
Pierre-feuille-ciseaux (voir Pierre-papier-ciseaux sur Wikipedia) est un jeu effectué avec les mains et opposant un ou
plusieurs joueurs.
Déroulement du jeu
Les deux joueurs choisissent simultanément un des trois coups possibles en le symbolisant de la main :
    poing fermé : Pierre ;
    main ouverte, doigts collés les uns aux autres : Feuille ;
    main avec pouce, annulaire et auriculaire fermé, index et majeur ouvert en forme de V : Ciseaux.
La pierre bat les ciseaux (en les émoussant), les ciseaux battent la feuille (en la coupant), la feuille bat la pierre
(en l’enveloppant). Ainsi chaque coup bat un autre coup, fait match nul contre le deuxième (son homologue) et est battu
par le troisième.
Écrire un programme qui réalise 5 manches du jeu Pierre-feuille-ciseaux entre l’ordinateur et le joueur. Chaque manche
va consister en :
    la génération (pseudo) aléatoire d’un nombre entre 0 et 2 compris, à l’aide de la fonction randint du module random,
    qui va représenter le coup de l’ordinateur (0 valant Pierre, 1, Feuille et 2, Ciseaux) ;
    la lecture en entrée (input) d’une valeur entière entre 0 et 2 compris qui représente le coup du joueur ;
    l’affichage du résultat sous une des formes :
        coup_o bat coup_j : points
        coup_o est battu par coup_j : points
        coup_o annule coup_j : points
    où
        coup_o et coup_j sont respectivement le coup de l’ordinateur et du joueur : "Pierre" s’il a joué 0, "Feuille"
        s’il a joué 1 et "Ciseaux" s’il a joué 2.
        points donne le résultat des manches jusqu’à présent sachant que le compteur points part de zéro, et est
        incrémenté de un chaque fois que le joueur gagne une manche, et décrémenté de un chaque fois que l’ordinateur
        gagne une manche (les match nuls ne modifiant pas le compteur points).
À la fin des cinq manches, votre programme affichera : Perdu, Nul ou Gagné suivant que le compteur est négatif, nul ou
strictement positif.
Pour plus de clarté dans votre code, nous vous conseillons de définir les trois constantes symboliques :
PIERRE = 0
FEUILLE = 1
CISEAUX = 2
Par ailleurs, votre code doit importer le module random et, avant de commencer les manches, pour permettre à UpyLaB de
valider les résultats, il doit d’abord lire une valeur entière s et appeler la fonction random.seed(s). Vous devez donc
intégrer le code suivant :
import random
PIERRE = 0
FEUILLE = 1
CISEAUX = 2
...
s = int(input())
random.seed(s)
Votre code fera donc un appel à random.seed suivi de cinq appels à random.randint, un par manche. Aucun autre appel à
une fonction de random ne pourra être effectué.
Vous pouvez bien sûr utiliser la fonction bat de l’exercice 4.9 mais nous vous conseillons vivement de définir aussi
d’autres fonctions (par exemple , une fonction qui réalise une manche et imprime la ligne de message) pour structurer
votre code.
Exemple 1
Sachant que le code suivant :
random.seed(65)
for i in range(5):
    print(random.randint(0,2))
donne le résultat :
1
1
1
2
0
l’exécution du code avec les entrées :
65
0
1
2
1
0
doit afficher :
Feuille bat Pierre : -1
Feuille annule Feuille : -1
Feuille est battu par Ciseaux : 0
Ciseaux bat Feuille : -1
Pierre annule Pierre : -1
Perdu
Exemple 2
Sachant que le code suivant :
random.seed(1515)
for i in range(5):
    print(random.randint(0,2))
donne le résultat :
2
1
0
2
2
l’exécution du code avec les entrées :
1515
0
1
2
1
0
doit afficher :
Ciseaux est battu par Pierre : 1
Feuille annule Feuille : 1
Pierre bat Ciseaux : 0
Ciseaux bat Feuille : -1
Ciseaux est battu par Pierre : 0
Nul
Exemple 3
Sachant que le code suivant :
random.seed(2001)
for i in range(5):
    print(random.randint(0,2))
donne le résultat :
2
0
1
0
0
l’exécution du code avec les entrées :
2001
0
1
2
1
0
doit afficher :
Ciseaux est battu par Pierre : 1
Pierre est battu par Feuille : 2
Feuille est battu par Ciseaux : 3
Pierre est battu par Feuille : 4
Pierre annule Pierre : 4
Gagné
Consignes
    Dans cet exercice, il vous est demandé d’écrire un programme contenant des fonctions.
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que
    le résultat attendu en respectant majuscules et minuscules et en veillant à n’avoir qu’une espace entre les mots et
    signes et aucune espace supplémentaire en fin de ligne. En particulier, il ne faut rien écrire à l’intérieur des
    appels à input (int(input()) et non int(input("Entrer un nombre : ")) par exemple), ni ajouter du texte
    supplémentaire dans ce qui est imprimé (print(points) et non print("résultat :",points) par exemple).
"""

import random

def bat():
    return coup_o == 0 and coup_j == 2 or coup_o == coup_j + 1

def t_points():
    if coup_o == coup_j:
        return 0
    elif bat() == True:
        return -1
    elif bat() == False:
        return 1

def def_n_coup_o():
    if coup_o == 0:
        return "Pierre"
    elif coup_o == 1:
        return "Feuille"
    elif coup_o == 2:
        return "Ciseaux"

def def_n_coup_j():
    if coup_j == 0:
        return "Pierre"
    elif coup_j == 1:
        return "Feuille"
    elif coup_j == 2:
        return "Ciseaux"

def tour():
    n_coup_o = def_n_coup_o()
    n_coup_j = def_n_coup_j()
    if res_tour == 0:
        return f"{n_coup_o} annule {n_coup_j} : {points}"
    elif res_tour == -1:
        return f"{n_coup_o} bat {n_coup_j} : {points}"
    elif res_tour == 1:
        return f"{n_coup_o} est battu par {n_coup_j} : {points}"

def resultat():
    if points > 0:
        return "Gagné"
    if points < 0:
        return "Perdu"
    else:
        return "Nul"

PIERRE = 0
FEUILLE = 1
CISEAUX = 2

s = int(input())
random.seed(s)
points = 0

for i in range(5):
    coup_o = random.randint(0, 2)
    coup_j = int(input())
    res_tour = t_points()
    points += res_tour
    print(tour())

print(resultat())