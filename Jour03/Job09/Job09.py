def moyenne ():
    a = float(input("Veuillez saisir votre première note : "))
    b = float(input("Veuillez saisir une deuxieme note : ")) 
    c= float(input("Veuillez saisir une troisième note : "))
    
    moyenne_etudiant = (a + b + c)/3
    return moyenne_etudiant

moyenne_etudiant = moyenne()


if moyenne_etudiant >=0 and moyenne_etudiant <=7:
    print ("Elève devant faire des efforts" f"\nVous avez une moyenne de {moyenne_etudiant}")
elif moyenne_etudiant >=8 and moyenne_etudiant <=10:
    print ("Elève moyen" f"\nVous avez une moyenne de {moyenne_etudiant}")
elif moyenne_etudiant >11 and moyenne_etudiant <14:
    print ("Bon élève" f"\nVous avez une moyenne de {moyenne_etudiant}")
elif moyenne_etudiant >=15 and moyenne_etudiant <=20:
    print ("Très bon élève" f"\nVous avez une moyenne de {moyenne_etudiant}")