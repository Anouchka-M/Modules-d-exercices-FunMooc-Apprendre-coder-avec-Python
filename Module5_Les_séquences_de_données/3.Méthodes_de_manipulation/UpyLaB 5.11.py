"""
Écrire une fonction intersection(v, w) qui calcule l’intersection entre deux chaînes de caractères v et w.
On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots. Par exemple,
l’intersection de « programme » et « grammaire » est « gramm ».
Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.
Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans v. Par exemple,
intersection('bbaacc', 'aabb') renvoie 'bb'.
Exemple 1
L’appel suivant de la fonction :
intersection('programme', 'grammaire')
doit retourner :
'gramm'
Exemple 2
L’appel suivant de la fonction :
intersection('salut', 'merci')
doit retourner :
''
Exemple 3
L’appel suivant de la fonction :
intersection('merci', 'adieu')
doit retourner :
'e'
Consignes
Dans cet exercice, il vous est demandé d’écrire seulement la fonction intersection.
Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en
 particulier aucun appel à input ou à print.
"""

def intersection(v, w):
    ###calcule l’intersection entre deux chaînes de caractères v et w
    ###on définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots

    #définition des variables
    n, m = -1, -1 #int indice de v et w
    n_v, m_w = [], [] #listes qui contient les indices des lettres communes dans la chaîne v et w
    o = 0 #permettra d'étendre les intersections
    v_inter = "" #intersection de v
    w_inter = "" #intersection de w
    res_v = [] #liste qui contient caractères confirmés entre v_inter et w_inter
    res = "" #str intersection la plus grande entre v et w

    #création et tri des listes n_v et m_v
    for i in v:
        n += 1
        m = - 1
        for j in w:
            m += 1
            if i == j: #si un caractère commun est trouvé
                if n not in n_v: #s'il n'est pas déjà dans la liste n_v
                    n_v.append(n)
                    n_v.sort()
                if m not in m_w: #s'il n'est pas déjà dans la liste n_w
                    m_w.append(m)
                    m_w.sort()

    #boucle sur les deux listes n_v et m_w afin de compléter res_v et res
    for i in n_v:
        for j in m_w:
            o = 0 #remet o à 0 pour continuer à boucler
            res_v = [] #vide res_v pour continuer à boucler
            v_inter = v[i:i + 1]  #définition de la première inter à partir de laquelle chercher pour v
            w_inter = w[j:j + 1]  #définition de la première inter à partir de laquelle chercher pour w

            while v_inter == w_inter and o < len(v_inter): #aussi longtemps qu'il y a intersection
                o += 1
                v_inter= v[i:i + 1 + o]
                w_inter = w[j:j + 1 + o]
                res_v.append(v_inter[o - 1])
                if len(res_v) > len(res): #si res_v est plus longue que res
                    res = "".join(res_v) #res est remplacé par le contenu de cette liste transformé en str

    return res

#paramètres testés par la console FunMOOC, avec en commentaire le résultat à obtenir
print(intersection('programme', 'grammaire'))  # gram
print(intersection('salut', 'merci'))  # ''
print(intersection('merci', 'adieu'))  # e
print(intersection('bbaacc', 'aabb'))  # bb
print(intersection('imaginer', 'migraine'))  # ine
print(intersection('police', 'picole'))  # ol
print(intersection('argent', 'gérant'))  # nt
print(intersection('abracadabra', 'ababraaracd'))  # abra
print(intersection('ironique', 'onirique'))  # ique
print(intersection('chicane', 'caniche'))  # can

###solution ohe
def find_indexes(word, char):
    """
    Cette methode retrouve, pour un mot donné, tous les index où apparait le caractère recherché
    """
    return [i for i, c in enumerate(word) if c == char]


def identical_part(v, w):
    """
    Cette methode retourne pour deux chaines de caractères la partie commune la plus longue.
    On aura préalablement positionné les deux chaines sur des lettres identiques
    """
    letters = ""
    for l1, l2 in zip(v, w):
        if l1 == l2:
           letters += l1
        else:
            break
    return letters


def intersection(v, w):
    intersections = [''] # A minima, on aura une intersection vide
    for idx, letter in enumerate(v):          # J'itere sur les lettres de mon premier mot
        if letter in w:       # Si la lettre est presente dans le second mot alors, j'ai au moins une intersection de 1
            for idx_w in find_indexes(w, letter):  # Je prends tous les idx ou "letter" apparait dans w
               current_intersection = identical_part(v[idx:],w[idx_w:])  # Pour chaque index, je retrouve la partie identique
               intersections.append(current_intersection)  # Je l'ajoute alors dans mes intersections

    return sorted(intersections, key=lambda x: len(x), reverse=True)[0]  # Il me faut la plus longue intersection ... Alors je trie mes intersections par leur longueur et retourne la plus longue

#paramètres testés par la console FunMOOC, avec en commentaire le résultat à obtenir
print(intersection('programme', 'grammaire'))  # gram
print(intersection('salut', 'merci'))  # ''
print(intersection('merci', 'adieu'))  # e
print(intersection('bbaacc', 'aabb'))  # bb
print(intersection('imaginer', 'migraine'))  # ine
print(intersection('police', 'picole'))  # ol
print(intersection('argent', 'gérant'))  # nt
print(intersection('abracadabra', 'ababraaracd'))  # abra
print(intersection('ironique', 'onirique'))  # ique
print(intersection('chicane', 'caniche'))  # can


#def intersection(v, w):
#    res = ""
#    res_v = [] #liste qui contiendra première lettre commune en partant de v
#    res_w = [] #liste qui contiendra première lettre commune en partant de w
#    n, m = -1, -1
#    n_v, m_v = 0, 0
#    n_w, m_w = 0, 0
#    o = 0
#    v_bord = ""
#    w_bord = ""

#    for i in v: #cherche la première lettre commune en partant de v
#        if res_v == []: #continue si liste vide
#            n += 1
#            m = - 1
#            for j in w:
#                m += 1
#                if i == j:
#                    res_v.append(i)
#                    n_v = n
#                    m_v = m
#                    res = []
#                    break
#        else: #passe à la suite quand une lettre commune est trouvée
#            break

#    if res_v != []: #si une lettre commune à partir de v est trouvée
#        m = - 1
#        for j in w: #cherche la première lettre commune en partant de w
#            if res_w == []: #continue si liste vide
#                m += 1
#                n = - 1
#                for i in v:
#                    n += 1
#                    if j == i:
#                        res_w.append(j)
#                        m_w = m
#                        n_w = n
#                        break
#            else: #passe à la suite quand une lettre commune est trouvée
#                break

#    if n_v <= m_w: #si lettre co. trouvée dans v indice <= à celle de w
#        v_bord = v[n_v:n_v + 1] #définition du 1er bord à partir duquel chercher
#        w_bord = w[m_v:m_v + 1] #d'après la première lettre co. de v
#        n = n_v
#        m = m_v

#    else : #si lettre co. trouvée dans v indice à celle de w
#        v_bord = v[n_w:n_w + 1] #définition du 1er bord à partir duquel chercher
#        w_bord = w[m_w:m_w + 1] #d'après la première lettre co. de w
#        m = m_w
#        n = n_w

#    while v_bord == w_bord != "":
#        res.append(v_bord[o])
#        o += 1
#        v_bord = v[n:n + o + 1]
#        w_bord = w[m:m + o + 1]

#    return "".join(res)