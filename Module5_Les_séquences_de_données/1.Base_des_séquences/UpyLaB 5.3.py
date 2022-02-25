"""
Écrire une fonction duree qui reçoit deux paramètres debut et fin. Ces derniers sont des couples (tuples de deux
composantes) dont la première composante représente une heure et la seconde les minutes.
Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants. Le résultat sera donné sous la forme
d’un tuple (heure, minutes).
Exemple 1
L’appel suivant de la fonction :
duree ((14, 39), (18, 45))
doit retourner :
(4, 6)
Exemple 2
L’appel suivant de la fonction :
duree ((6, 0), (5, 15))
doit retourner :
(23, 15)
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction duree. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou
    à print.
    Notez que l’appel duree ((6, 0), (5, 15)) retourne le couple (23, 15) et non (0, 45). Le premier argument
    correspond à l’instant initial et le second à l’instant final.
"""

def duree(debut, fin):
    h_debut = debut[0]
    m_debut = debut[1]
    h_fin = fin[0]
    m_fin = fin[1]
    h_res = 0
    m_res = 0

    m_res = m_fin - m_debut

    if m_res < 0:
        m_res = 60 + m_res
        h_res -= 1

    if h_debut > h_fin:
        h_res += 23 - h_debut + h_fin + 1
    elif h_debut == h_fin:
        h_res = 23
    else :
        h_res += h_fin - h_debut

    return (h_res, m_res)

print(duree((12, 21), (21, 47)))