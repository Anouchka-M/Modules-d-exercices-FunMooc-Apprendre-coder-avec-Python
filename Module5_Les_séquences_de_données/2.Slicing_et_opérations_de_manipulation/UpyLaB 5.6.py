"""Écrire une fonction transcription_arn(brin_codant) qui reçoit une chaîne de caractères en paramètre, correspondant
à un brin codant d'ADN, et qui retourne la chaîne de caractère représentant le brin d' ARN correspondant.".
Nous rappelons qu'un brin d'ADN peut être modélisé par une chaîne de caractères, dont les caractères sont pris parmi
les quatre suivants  : 'A'(Adénine), 'C' (Cytosine),'G' (Guanine) et 'T' (Thymine).
La transcription en ARN se traduit par le remplacement des nucléotides de Thymine par des nucléotides d'Uracile, que
l'on représentera par le caractère 'U'.
Exemple
L’appel suivant de la fonction :
transcription_arn('AGTCTTACCGATCCAT')
doit retourner :
'AGUCUUACCGAUCCAU'
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction transcription_arn. Le code que vous soumettez
    à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.
    Il n'est pas demandé que la fonction teste le type de l'argument passé ; vous pouvez supposer qu'il s'agira d'une
    chaîne de caractères valide.
"""

def transcription_arn(brin_codant):
    n = 0
    l_brin_codant = list(brin_codant)
    brin_codant_uracile = ""
    for i in l_brin_codant:
        if i == "T":
            l_brin_codant[n] = "U"
        brin_codant_uracile += l_brin_codant[n]
        n += 1
    return brin_codant_uracile

print(transcription_arn("AGTCTTACCGATCCAT"))
