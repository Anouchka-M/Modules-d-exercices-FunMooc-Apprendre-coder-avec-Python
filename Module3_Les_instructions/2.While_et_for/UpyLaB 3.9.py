"""
Écrire un programme qui demande à l’utilisateur combien de plis de papier sont nécessaires pour se rendre sur la Lune,
et pose la question tant que l’utilisateur n’a pas saisi la bonne réponse.
Si la réponse saisie par l’utilisateur n’est pas correcte, le programme affiche le message "Mauvaise réponse.", puis
pose à nouveau la question. Si la réponse saisie par l’utilisateur est correcte, le programme affiche le message
"Bravo !", et s’arrête.
Exemple
Dans cet exemple d’exécution, le texte est affiché par le programme, alors que les nombres sont saisis par
l’utilisateur :
Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : 666
Mauvaise réponse.
Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : 3
Mauvaise réponse.
Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : 42
Bravo !
Consignes
    UpyLaB va vérifier le bon fonctionnement du programme en comparant ce qui est affiché à l’écran avec ce qu’il
    attend. Veillez donc à bien respecter le texte à afficher (casse, espaces, ponctuation…).
    En particulier, pour lire les données utilisez précisément l’instruction :
    int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
    et pour afficher utilisez précisément les instructions
    print("Mauvaise réponse.")
    et
    print("Bravo !")
    Pour rappel, la réponse attendue a été calculée par le script de Sébastien dans la vidéo d'introduction de la
    boucle while, en section 3.4.1.
    Cette réponse n'est pas à faire calculer par votre programme, qui se contente de la demander à l'utilisateur.
"""

plis_necessaires = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))

while plis_necessaires != 42:
    print("Mauvaise réponse.")
    plis_necessaires = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))

print("Bravo !")