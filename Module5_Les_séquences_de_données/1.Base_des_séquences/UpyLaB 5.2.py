"""
On représente un brin d’ADN par une chaîne de caractères dont les caractères sont parmi les quatre suivants : 'A'
(Adénine), 'C' (Cytosine), 'G' (Guanine) et 'T' (Thymine).
Écrire une fonction est_adn qui reçoit une chaîne de caractères en paramètre et qui retourne True si cette chaîne de
caractères n'est pas vide et peut représenter un brin d’ADN, False sinon.
Exemple 1
L’appel suivant de la fonction :
est_adn("ATGGT")
doit retourner :
True
Exemple 2
L’appel suivant de la fonction :
est_adn("ISA")
doit retourner :
False
Exemple 3
L’appel suivant de la fonction :
est_adn("CTaG")
doit retourner :
False
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction est_adn. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou
    à print.
    Vous pouvez supposer que l’argument passé à la fonction sera toujours une chaîne de caractères ; notez que l'appel
    de la fonction sur une chaîne vide doit retourner False.
"""

def est_adn(sequence) :
    i = 0
    adn = ["A", "C", "G", "T"]
    while i < (len(sequence)) and sequence[i] in adn:
        i += 1
    return i >= len(sequence) > 0

print(est_adn(""))