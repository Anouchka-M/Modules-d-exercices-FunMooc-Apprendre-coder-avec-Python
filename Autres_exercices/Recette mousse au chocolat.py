nombre_personnes = 0

nombre_oeufs = 3 / 4

quantite_chocolat = 100 / 4

sachet_sucre = 1 / 4

print(f"Cette recette nécessite {nombre_oeufs} oeuf, {quantite_chocolat} grammes de chocolat et {sachet_sucre} sachet de sucre par personne.")


nombre_personnes = input("Pour combien de personnes préparez-vous cette recette ? ")

if nombre_personnes.isnumeric() == False:
    print("Veuillez saisir un nombre entier ou 'quitter' pour quitter le programme.")
    nombre_personnes = input("Pour combien de personnes préparez-vous cette recette ? ")

elif nombre_personnes == 'quitter':
    print("Byebye")
    exit()

else:
    nombre_personnes = int(nombre_personnes)

    nombre_oeufs = nombre_oeufs * nombre_personnes
    nombre_oeufs = round(nombre_oeufs)

    quantite_chocolat = quantite_chocolat * nombre_personnes
    quantite_chocolat = round(quantite_chocolat)

    sachet_sucre = sachet_sucre * nombre_personnes
    sachet_sucre = int(sachet_sucre)

    print(f"Pour {nombre_personnes} personnes il vous faut : {nombre_oeufs} oeufs, {quantite_chocolat} grammes de chocolat et {sachet_sucre} sachet(s) de sucre.")