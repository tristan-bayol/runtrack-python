def pair_impair (x):
    
        if x > 0:
            if x % 2 == 0:
                print(f"{x} est un nombre pair")
            else:
                print(f"{x} est un nombre impair")
        else:
            print("Veuillez entrer un nombre supérieur à 0")
    else:
        print("Veuillez saisir un nombre entier")
    
pair_impair(4)
pair_impair(0)
pair_impair(2.5)
pair_impair(7)