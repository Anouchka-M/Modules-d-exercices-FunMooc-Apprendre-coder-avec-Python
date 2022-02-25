"""Cet exercice et le suivant vous demandent de programmer le petit jeu appelé « Pierre-feuille-ciseaux » ou
« Pierre-papier-ciseaux » (et qui porte encore d’autres noms comme indiqué dans la page Pierre-papier-ciseaux sur
Wikipedia que nous utilisons pour rédiger l’énoncé ci-dessous).
Pierre-feuille-ciseaux est un jeu effectué avec les mains et opposant un ou plusieurs joueurs. Ici nous nous supposerons
qu’il y a deux joueurs : l’ordinateur et le joueur lui-même.
Déroulement du jeu
Les deux joueurs choisissent simultanément un des trois coups possibles en le symbolisant de la main :
    poing fermé : Pierre ;
    main ouverte, doigts collés les uns aux autres : Feuille ;
    main avec pouce, annulaire et auriculaire fermé, index et majeur ouvert en forme de V : Ciseaux.
Résultat du jeu :
    la pierre bat les ciseaux (en les émoussant),
    les ciseaux battent la feuille (en la coupant),
    la feuille bat la pierre (en l’enveloppant).
Ainsi chaque coup bat un autre coup, fait match nul contre le deuxième (son homologue) et est battu par le troisième.
Écrire une fonction bat(joueur_1, joueur_2) où joueur_1 et joueur_2 ont chacun une valeur entière 0, 1 ou 2, qui encode
ce que le joueur a fait comme coup (0 : PIERRE, 1 : FEUILLE, 2 : CISEAUX) qui renvoie un résultat booléen :
    vrai si joueur_1 bat le joueur_2 :
    faux si joueur_2 bat joueur_1 ou fait match nul contre lui.
Exemple 1
L’appel suivant de la fonction :
bat(0, 0)
doit retourner :
False
Exemple 2
L’appel suivant de la fonction :
bat(0, 1)
doit retourner :
False
Exemple 3
L’appel suivant de la fonction :
bat(2, 1)
doit retourner :
True
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction bat. Le code que vous soumettez à UpyLaB doit
    donc comporter uniquement la définition de cette fonction, éventuellement accompagné des trois définitions des
    constantes PIERRE, FEUILLE, CISEAUX , et ne fait en particulier aucun appel à inputou à print.
    Il n’est pas demandé que la fonction bat teste le type ou les valeurs des paramètres reçus.
"""

PIERRE, FEUILLE, CISEAUX = 0, 1, 2

def bat(joueur_1, joueur_2):
    return joueur_1 == 0 and joueur_2 == 2 or joueur_1 == joueur_2 + 1

print(bat(2, 0))