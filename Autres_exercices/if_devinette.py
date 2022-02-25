import random
secret = random.randint(0, 5)
secret = int(secret)

valeur = int(input("choisissez un nombre entre 1 et 5 : "))

if secret == valeur:
    print("gagné !")

else:
    print(f"perdu ! la valeur était : {secret}")