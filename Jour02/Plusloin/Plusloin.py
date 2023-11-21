# Demander à l'utilisateur les longueurs des côtés du triangle
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Vérifier si les longueurs peuvent former un triangle
def est_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Vérifier le type de triangle
def type_triangle(a, b, c):

#Triangle équilatérale, les trois cotés doivent etre égaux !
    if a == b and b == c:
        return "Equilatéral"
#Triangle Isocele au moins deux cotés egaux + si la somme du carré de ses deux cotés = carré hypothénuse alors Rectangle/isocele 
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Rectangle et Isocèle"
        else:
            return "Isocèle"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Rectangle"
#Autre cas !    
    else:
        return "Quelconque"

# Vérifier si les longueurs peuvent former un triangle
if est_triangle(a, b, c):
    # Déterminer le type de triangle
    type_tri = type_triangle(a, b, c)
    print(f"Les longueurs {a}, {b}, {c} peuvent former un triangle de type {type_tri}.")
else:
    print(f"Les longueurs {a}, {b}, {c} ne peuvent pas former un triangle.")
