"""
Écrire une fonction prime_numbers qui reçoit comme paramètre un nombre entier nb et qui renvoie la liste des nb
premiers nombres premiers.
Si le paramètre n’est pas du type attendu, ou ne correspond pas à un nombre entier positif ou nul, la fonction renvoie
None.
Exemple 1
L’appel suivant de la fonction :
prime_numbers(4)
doit retourner :
[2, 3, 5, 7]
Exemple 2
L’appel suivant de la fonction :
prime_numbers(-2)
doit retourner :
None
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement une fonction prime_numbers, et non un programme complet.
    Le code que vous soumettez à UpyLaB ne fait donc en particulier aucun appel à input ou à print. Par contre, il est
    tout à fait possible, voire conseillé, de définir une fonction annexe, qui par exemple ici détermine si le nombre
    passé en paramètre est premier ou non.
    On rappelle qu’un nombre premier est un entier naturel qui possède exactement deux diviseurs distincts et positifs,
    1 et lui-même.
"""

def prime_numbers(nb):
    if type(nb) is int and nb >= 0:
        lst_prime_numbers = []
        n = 1

        while len(lst_prime_numbers) < nb:
            n += 1
            for i in range(1, n + 1):
                if (n - 1 == i and n % i != 0) or (n - 1 == i == 1):
                    lst_prime_numbers.append(n)
                elif i not in (n, 1) and n % i == 0:
                    break

        return lst_prime_numbers

print(prime_numbers(4))
print(prime_numbers(-1))
print(prime_numbers("b"))