"""
Écrire une fonction plus_grand_bord(w) qui reçoit un mot w et retourne le plus grand bord de ce mot.
On dit qu’un mot u est un bord du mot w si u est à la fois un préfixe strict et un suffixe strict de w, c’est-à-dire
qu’on retrouve le mot u au début et à la fin du mot w, sans que u soit égal à w lui-même.
Exemples : 'a' et 'abda' sont des bords de 'abdabda'. En effet, 'abdabda' commence et se termine par 'a', ainsi que
par 'abda'. Le plus grand bord de 'abdabda' est 'abda'.
Si w n’a pas de bord, la fonction retourne la chaîne de caractères vide.
Exemple 1
L’appel suivant de la fonction :
plus_grand_bord('abdabda')
doit retourner :
'abda'
Remarque : Notez que les apostrophes indiquent ici que l'objet retourné est de type str. Ces apostrophes ne font pas
partie de la chaîne de caractères elle-même.
Exemple 2
L’appel suivant de la fonction :
plus_grand_bord('abcabd')
doit retourner :
''
Exemple 3
L’appel suivant de la fonction :
plus_grand_bord('abcba')
doit retourner :
'a'
Exemple 4
L’appel suivant de la fonction :
plus_grand_bord('aaaaa')
doit retourner :
'aaaa'
Consignes
Dans cet exercice, il vous est demandé d’écrire seulement la fonction plus_grand_bord.
Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en
particulier aucun appel à input ou à print.
"""

def plus_grand_bord(w):
    n = len(w) - 1
    d_bord = w[:n]
    f_bord = w[-n:]

    while d_bord != f_bord:
        n -= 1
        d_bord = w[:n]
        f_bord = w[-n:]
    return f_bord

print(plus_grand_bord('aaaaa'))
plus_grand_bord('abdabda')
plus_grand_bord('abcabd')
plus_grand_bord('abcba')