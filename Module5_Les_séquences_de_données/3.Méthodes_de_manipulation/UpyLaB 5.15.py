"""
(D’après une idée de Jacky Trinh - 11/02/2018)
Joao vient d’arriver dans notre pays depuis le Portugal. Il a encore du mal avec la langue française. Malgré ses efforts
considérables, il fait une faute d’orthographe quasi à chaque mot. Son souci est qu’il n’arrive pas toujours à écrire
un mot correctement sans se tromper à une lettre près. Ainsi pour écrire « bonjour », il peut écrire « binjour ». Pour
remédier à ce problème, Joao utilise un correcteur orthographique. Malheureusement, Joao a un examen aujourd’hui et il
a oublié son petit correcteur.
Afin de l’aider, nous vous demandons d’écrire une fonction correcteur(mot, liste_mots) où mot est le mot que Joao écrit
et liste_mots est une liste qui contient les mots (ayant la bonne orthographe) que Joao est susceptible d’utiliser.
Cette fonction doit retourner le mot dont l’orthographe a été corrigée.
Exemple 1
L’appel suivant de la fonction :
correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
doit retourner :
"bonjour"
Exemple 2
L’appel suivant de la fonction :
correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
doit retourner :
"chat"
Consignes
    Pour cet exercice, vous pourrez utiliser la fonction distance_mots(mot_1, mot_2) que vous avez précédemment codée
    et qui donne la distance entre deux mots de même longueur. N’oubliez pas alors de mettre aussi le code de cette
    fonction dans votre solution.
    Le correcteur orthographique demandé est une version simple ; les mots en paramètre auront au maximum une seule
    lettre qui diffère par rapport à la bonne orthographe.
    Nous ne prenons pas en compte les mots avec accents, ni les mots composés de tiret, d’apostrophes, d’espace,..
    liste_mots ne contient pas de mots qui se ressemblent ; si Joao écrit le mot « liee », il se peut en effet que cela
    représente le mot « lire » ou « lier ». Afin d’éviter cette confusion, deux mots de même longueur de la liste sont
    au moins à une distance de 3. Il n’y aura ainsi qu’un seul mot dans liste_mots répondant au problème.
    Vous pouvez supposer que Joao soit arrive à écrire des mots sans fautes, soit fait au plus une erreur.
"""

def correcteur(mot, liste_mots):
    for element in liste_mots:
        indice = 0
        distance_mots = 0
        for lettre in element:
            if distance_mots >= 2:
                break
            elif lettre != mot[indice]:
                distance_mots += 1
            indice += 1
        if distance_mots < 2:
            return element

print(correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"])) #"bonjour"
print(correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"])) #chat

### Solution Swak ###
from difflib import SequenceMatcher

def similar(word1, word2):
    return SequenceMatcher(None, word1, word2).ratio()

def correcteur(mot, liste_mots):
    best_similarity = 0
    best_word = ''
    for word in liste_mots:
        sim = similar(mot, word)
        if sim > best_similarity:
            best_similarity = sim
            best_word = word
    return best_word

print(correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"])) #"bonjour"
print(correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"])) #chat

### Solution en utilisant la fonction distance_mots(mot_1, mot_2) d'UpyLaB 5.14 et en l'améliorant pour qu'elle prenne
### en compte les mots de longueurs différentes

def distance_mots(mot_1, mot_2):
    indice = 0
    distance = 0

    while indice < len(mot_1) and indice < len(mot_2):
        if mot_1[indice] != mot_2[indice]:
            distance += 1
        indice += 1
    #return distance + len(mot_1) - len(mot_2) if len(mot_1) >= len(mot_2) else distance + len(mot_2) - len(mot_1)
    return distance + abs(len(mot_1) - len(mot_2))

def correcteur(mot, liste_mots):
    for element in liste_mots:
        if distance_mots(mot, element) <= 1:
            return element

print(correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"])) #"bonjour"
print(correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"])) #chat