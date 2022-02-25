"""
Écrire une fonction dupliques qui reçoit une séquence en paramètre.
La fonction doit renvoyer la valeur booléenne True si la séquence passée en paramètre contient des éléments dupliqués,
et la valeur booléenne False sinon.
Exemple 1
L’appel suivant de la fonction :
dupliques([1, 2, 3, 4])
doit retourner :
False
Exemple 2
L’appel suivant de la fonction :
dupliques(['a', 'b', 'c', 'a'])
doit retourner :
True
Exemple 3
L’appel suivant de la fonction :
dupliques('abcda')
doit retourner :
True
Consignes
Dans cet exercice, il vous est demandé d’écrire seulement la fonction dupliques.
Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en
particulier aucun appel à input ou à print.
Il n'est pas demandé que la fonction teste le type de l'argument passé ; vous pouvez supposer qu'il sera valide.
"""

def dupliques(sequence):
    if sequence is str:
        sequence.split()
    sequence_l = list(sequence)
    verif_l = []
    for i in sequence:
        for j in sequence_l:
            if i == j:
                verif_l.append(j)
    return len(verif_l) != len(sequence)

print(dupliques([1, 2, 3, 4]))
print(dupliques(['a', 'b', 'c', 'a']))
print(dupliques('abcda'))