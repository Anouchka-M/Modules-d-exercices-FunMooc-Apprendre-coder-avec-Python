"""
Écrire une fonction my_filter qui reçoit une liste lst et une fonction booléenne f en paramètres et renvoie une nouvelle
liste constituée des éléments de lst pour lesquels la fonction f renvoie True.
Exemples
Pour tester dans votre IDE (Thonny ou PyCharm par exemple) la fonction my_filter, vous allez devoir définir une fonction
booléenne f et la passer en argument à la fonction my_filter.
Vous pourrez donc d’abord définir la fonction f à l’aide du mot-clé def, mais sachez que l’on peut aussi définir
directement la fonction f lors de l’appel à la fonction my_filter en utilisant ce qu’on appelle une fonction lambda.
Il s’agit de fonctions anonymes que l’on peut utiliser au moment même.
Exemple d’une fonction lambda :
lambda x : isinstance(x, int)
Cette fonction testera si l’objet x qu’on lui passe est de type int et fait le même travail que la fonction is_int plus
classiquement définie ci-dessous :
def is_int(x):
    return isinstance(x, int)
On pourra alors appeler la fonction my_filter des deux manières suivantes :
my_filter(lst, lambda x : isinstance(x, int))
my_filter(lst, is_int)
La seule différence, c’est que dans le deuxième cas, il faut avoir défini la fonction is_int au préalable (mais
l’avantage, c’est qu’on pourrait la réutiliser dans la suite du code, contrairement à la fonction lambda).
Notez qu’UpyLaB utilisera ces fonctions lambda dans ses tests.
Exemple 1
L’appel suivant de la fonction :
my_filter(['hello', 666, 42, 'Thierry', 1.5], lambda x : isinstance(x, int))
doit retourner :
[666, 42]
Exemple 2
L’appel suivant de la fonction :
my_filter([-2, 0, 4, -5, -6], lambda x : x < 0)
doit retourner :
[-2, -5, -6]
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_filter. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à
    print.
    On rappelle qu’une fonction booléenne est une fonction qui retourne True ou False.
    Essayez d’utiliser une compréhension de liste pour cet exercice.
"""

def my_filter(lst, f):
    return [element for element in lst if f(element)]
print(my_filter(['hello', 666, 42, 'Thierry', 1.5], lambda x : isinstance(x, int)))
#[666, 42]
print(my_filter([-2, 0, 4, -5, -6], lambda x : x < 0))
#[-2, -5, -6]