"""
Une anagramme d’un mot v est un mot w qui comprend les mêmes lettres que le mot initial v, en même quantité, mais non
nécessairement dans le même ordre (par exemple, « marion » et « romina » sont des anagrammes). Notez que anagramme est
un mot féminin.
Écrire une fonction anagrammes(v, w) qui renvoie la valeur booléenne True si les mots v et w sont des anagrammes.
La fonction retourne la valeur booléenne False dans le cas contraire.
Exemple 1
L’appel suivant de la fonction :
anagrammes('marion', 'romina')
doit retourner :
True
Exemple 2
L’appel suivant de la fonction :
anagrammes('bonjour', 'jour')
doit retourner :
False
Exemple 3
L’appel suivant de la fonction :
anagrammes('pate', 'patte')
doit retourner :
False
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction anagrammes. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.
    Votre code ne doit pas tester si les mots existent bien dans un quelconque dictionnaire.
    Pour simplifier, on supposera que tout mot est une anagramme de lui-même (par exemple, anagrammes('jour', 'jour')
    renvoie True), et on ne considèrera que des mots écrits en minuscule. Par ailleurs, il n’est pas demandé que votre
    fonction teste si les mots sont recensés dans un dictionnaire quelconque.
"""

def anagrammes(v, w):
    l = ""
    i = 0
    j = 0
    v_l = list(v)
    w_l = list(w)
    for v_l[i] in v_l:
        for w_l[j] in w_l:
            if w_l[j] in v_l[i]:
                l += w_l[j]
                w_l.pop(j)
                print(l)
            j += 1
        j = 0
        i += 1
    return len(v) == len(l) == len(w)

print(anagrammes('marion', 'romina'))
print(anagrammes('bonjour', 'jour'))
print(anagrammes('pate', 'patte'))
print(anagrammes('baignade', 'badinage'))
print(anagrammes('chicane', 'caniche'))
print(anagrammes('bbonjour', 'bbonjour'))
print(anagrammes('baba', 'aabb'))