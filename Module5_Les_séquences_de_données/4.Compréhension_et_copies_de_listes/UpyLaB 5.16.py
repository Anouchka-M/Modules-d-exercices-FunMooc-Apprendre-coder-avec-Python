"""
AVEC OU SANS COMPRÉHENSION
Les exercices UpyLaB suivants peuvent aussi se résoudre sans utiliser la technique de compréhension de liste. Mais les
solutions sont beaucoup plus courtes avec cette technique ! Nous vous demandons donc si possible de les réaliser avec
du code utilisant des compréhensions de liste.
ÉNONCÉ DE L’EXERCICE UPYLAB 5.16
Écrire une fonction my_pow qui prend comme paramètres un nombre entier m et un nombre flottant b, et qui renvoie une
liste contenant les m premières puissances de b, c’est-à-dire une liste contenant les nombres allant de b^0 à b^{m - 1}.
Si le type des paramètres n’est pas celui attendu, la fonction retournera la valeur None.
Exemple 1
L’appel suivant de la fonction :
my_pow(3, 5.0)
doit retourner :
[1.0, 5.0, 25.0]
Exemple 2
L’appel suivant de la fonction :
my_pow(3.0, 5.0)
doit retourner :
None
Exemple 3
L’appel suivant de la fonction :
my_pow('a', 'b')
doit retourner :
None
Consignes
Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_pow.
Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en
particulier aucun appel à input ou à print.
"""

def my_pow(m, b):
    if isinstance(m, int) and isinstance(b, float):
        return [b**i for i in range(0, m)]

print(my_pow(3, 5.0)) #[1.0, 5.0, 25.0]
print(my_pow(3.0, 5.0)) #None
print(my_pow('a', 'b')) #None