"""PAS ENCORE RESOLU

Écrire un programme qui lit un nombre entier strictement positif n et imprime une pyramide de chiffres de hauteur n
(sur n lignes complètes, c'est-à-dire toutes terminées par une fin de ligne).
    La première ligne imprime un “1” (au milieu de la pyramide).
    La ligne i commence par le chiffre i % 10 et tant que l’on n’est pas au milieu, le chiffre suivant a la valeur
    suivante ((i+1) % 10).
    Après le milieu de la ligne, les chiffres vont en décroissant modulo 10 (symétriquement au début de la ligne).
Notons qu’à la dernière ligne, aucune espace n’est imprimée avant d’écrire les chiffres 0123....
Exemple 1
Avec la donnée lue suivante :
1
le résultat à imprimer vaudra :
1
Exemple 2
Avec la donnée lue suivante :
2
le résultat à imprimer vaudra :
 1
232
Exemple 3
Avec la donnée lue suivante :
10
le résultat à imprimer vaudra :
         1
        232
       34543
      4567654
     567898765
    67890109876
   7890123210987
  890123454321098
 90123456765432109
0123456789876543210
Consignes
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que
    le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un
    nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé.
"""