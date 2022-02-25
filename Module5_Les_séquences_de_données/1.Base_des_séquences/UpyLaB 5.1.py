"""
Écrire une fonction signature qui reçoit un paramètre identite . Ce paramètre est un couple (tuple de deux composantes)
dont la première composante représente un nom et la seconde un prénom.
Cette fonction doit retourner la chaîne de caractères formée du prénom suivi du nom, séparés par une espace.
Exemple
L’appel suivant de la fonction :
signature(('de Saint-Exupéry', 'Antoine'))
doit retourner :
'Antoine de Saint-Exupéry'
Note : Il s'agit de la valeur retournée par la fonction. Cette valeur est de type chaîne de caractères, c'est pourquoi
elle est notée entourée de quotes, mais ces quotes ne font pas partie de la chaîne elle-même.
Consignes
        Dans cet exercice, il vous est demandé d’écrire seulement la fonction signature. Le code que vous soumettez à
        UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel
        à input ou à print.
        Vous pouvez supposer que l’argument passé à la fonction est valide (couple de deux chaînes de caractères).
"""

def signature(identite):
    prenom = identite[1]
    nom = identite[0]
    return prenom + " " + nom

print(signature(('de Saint-Exupéry', 'Antoine')))