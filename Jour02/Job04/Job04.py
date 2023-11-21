
#Saisi du nombre (rappel une input est un string par défault)
nombre_string = (input("Entrez un entier supérieur à zéro (N): "))

#verifie qu'il ne s'agit pas d'un nombre décimale
if ',' in nombre_string or '.' in nombre_string:
    print("Rappel un nombre entier ne comporte pas de décimale") 

#Verifie que ma chaine de caractère ne comporte que des nombres gràce à isdigit
elif not nombre_string.isdigit():
    print("Erreur ! veuillez entrer un nombre entier")

else:
#convertion de la chaine en entier
    nombre = int(nombre_string)

#Affiche la table de multiplication de ce nombre
    if nombre == 0:
        print("Veuillez entrer un nombre supérieur à 0")

    elif nombre > 0:
        print("Table de multiplication de ", nombre)
        for i in range(1, 11):
            resultat = i * nombre
            print (f"{i} x {nombre} = {resultat}")