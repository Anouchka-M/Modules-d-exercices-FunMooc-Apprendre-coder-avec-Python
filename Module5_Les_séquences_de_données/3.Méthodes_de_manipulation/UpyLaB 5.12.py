"""
Écrire une fonction my_insert qui reçoit comme premier paramètre une liste d’entiers relatifs triée par ordre croissant
et comme deuxième paramètre un entier relatif n, et qui renvoie une liste correspondant à la liste reçue, mais dans
laquelle le nombre n a été inséré à la bonne place.
La liste donnée en paramètre ne doit pas être modifiée par votre fonction.
Vous pouvez supposer que le premier paramètre sera bien une liste triée d’entiers, mais si le deuxième paramètre n’est
pas du bon type, la fonction retourne None.
Exemple 1
L’appel suivant de la fonction :
my_insert([1, 3, 5], 4)
doit retourner :
[1, 3, 4, 5]
Exemple 2
L’appel suivant de la fonction :
my_insert([2, 3, 5], 1)
doit retourner :
[1, 2, 3, 5]
Exemple 3
L’appel suivant de la fonction :
my_insert([2, 3, 5], 0.5)
doit retourner :
None
Consignes
Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_insert.
Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en
particulier aucun appel à input ou à print.
"""

def my_insert(lst, n):
    if type(n) == int:
        res = lst.copy()
        res.append(n)
        res.sort()
        return res

l = [1, 3, 5]
print(my_insert([l], 4))
print(l)
print(my_insert([2, 3, 5], 1))
print(my_insert([2, 3, 5], 0.5))
print(my_insert([1, 5, 78], 39))
print(my_insert([1, 5, 78], -1))
print(my_insert([1, 5, 78], 80))