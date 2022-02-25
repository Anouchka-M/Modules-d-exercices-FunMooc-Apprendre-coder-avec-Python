"""Attention : cet exercice est composé de l'exercice UpyLaB 4.2.a suivi en dessous de l'exercice UpyLaB 4.2.b.
Le Petit Prince vient de débarquer sur la planète U357, et il apprend qu'il peut y voir de belles aurores boréales !
La planète U357 a deux soleils : les étoiles E1515 et E666.  C'est pour cela que les tempêtes magnétiques sont
permanentes, ce qui est excellent pour avoir des aurores boréales.
Par contre, il y fait souvent jour, sauf bien évidemment quand les deux soleils sont couchés en même temps.
Heureusement pour nous, une journée U357 s'écoule sur 24 heures comme sur notre Terre, et pour simplifier, nous ne
prendrons pas en compte les minutes (on ne donne que les heures avec des valeurs entières entre 0 et 23).
Nous vous demandons d'aider le Petit Prince à déterminer les périodes de jour et de nuit.
UPYLAB 4.2A
Pour cela, vous allez dans un premier temps écrire une fonction soleil_leve qui, pour un soleil particulier, reçoit
trois valeurs entières en argument pour la planète :
     - l'heure de lever du soleil (entre 0 et 23)
     - l'heure du coucher du soleil (entre 0 et 23)
     - l'heure actuelle (entre 0 et 23)
et qui renvoie une valeur booléenne vraie si le soleil est levé sur la planète à l'heure donnée en troisième argument
et fausse, s'il est couché.
On supposera que chacun des soleils ne se lève et ne se couche au plus qu'une seule fois par jour.
Il est toutefois possible que le lever ait lieu après l'heure du coucher, ce qui signifie dans ce cas que le soleil est
levé au début de la journée, puis qu'il se couche, puis qu'il se lève à nouveau plus tard dans la journée.
Enfin, si l'heure du lever est la même que l'heure du coucher :
     - soit toutes deux valent 12, cela signifie que le soleil ne se lève pas de la journée,
     - soit toutes les deux valent 0, cela signifie que le soleil ne se couche pas de la journée.
Exemple 1
L'appel suivant de la fonction :
soleil_leve(6, 18, 10)
doit retourner
True
Exemple 2
L'appel suivant de la fonction :
soleil_leve(15, 8, 12)
doit retourner
False
Exemple 3
L'appel suivant de la fonction :
soleil_leve(12, 12, 10)
doit retourner
False
Exemple 4
L'appel suivant de la fonction :
soleil_leve(0, 0, 22)
doit retourner
True
Consignes
    Dans cette première partie de l'exercice, il est demandé d'écrire seulement la fonction soleil_leve. Le code que
    vous soumettez à UpyLaB ne doit donc comporter que la définition de cette fonction. Ne mettez donc pas la partie
    appel à cette fonction. En particulier, il n'y a aucun appel à faire aux fonctions input et print.
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de fonction soleil_leve avec le bon nombre de
    paramètres.  Si la fonction existe bien, UpyLaB testera votre fonction en exécutant un code qui réalise un appel à
    votre fonction et affiche le résultat, ceci pour vérifier que votre fonction n'effectue aucun print.  Ensuite
    différents tests de votre fonction seront effectués par UpyLaB.
    Il n’est pas demandé que la fonction soleil_leve teste le type des paramètres reçus.
    Quand UpyLaB teste spécifiquement le code d’une fonction (ici la fonction soleil_leve), le type du résultat est
    également validé. Veillez donc bien à renvoyer un résultat de type requis. En particulier, les objets True et
    "True" ne sont pas du même type.
"""

def soleil_leve(a, b, c):
    return a <= c < b or a == b == 0 or c >= a > b or a > b > c

