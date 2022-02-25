"""
On considère une liste qui décrit une séquence t. Chaque élément de cette liste est un tuple de deux composantes : le
nombre de répétitions successives de l’élément x dans la séquence t, et l’élément x lui-même.
Par exemple, la liste [(1, 'He'), (2, 'l'), (1,'o')] décrit la séquence "Hello".
Écrire une fonction decompresse qui reçoit une telle liste en paramètre et renvoie la séquence t sous forme d’une
nouvelle liste.
Exemple
L’appel suivant de la fonction :
decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
doit retourner :
[1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour']
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction decompresse. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input
    ou à print.
    Essayez d’utiliser une compréhension de liste pour cet exercice.
"""

def decompresse(list_sequence):
    return [element[1] for element in list_sequence for sequence in range(element[0])]

print(decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))
#[1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour']
print(decompresse([(4, 'b'), (0, 'x'), (2, 'on'), (3, 'j'), (1, 'our')]))
#['b', 'b', 'b', 'b', 'on', 'on', 'j', 'j', 'j', 'our']
print(decompresse([(3, 1), (3, 2), (3, 3), (5, 4), (1, 5)]))
#[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5]
print(decompresse([(1, 'He'), (2, 'l'), (1,'o')]))
#['He', 'l', 'l', 'o']