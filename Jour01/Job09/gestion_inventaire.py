var1="Ecran"
var2=405.99
var3=25

print("Nom du produit:" , var1)
print("Prix Unitaire:" , var2)
print("Stock:" , var3)

var4=((var2 * 10)/100)
#La fonction input interrompt le scrit pour permettre à l'utilisateur d'agir sur la suite
#Les input sont par défault des string du coup on lui met int(....)pour convertir la valeur en entier
var5 =int(input("Combien de produits souhaitez vous ajouter au stock?"))

print("Nom du produit:", var1)
print("Prix Unitaire après inflation:", var2 + var4)
print("Nombre d'ajout au stock:", var5)
#L'équation suivante est rendu possible car grace au int() la var5 est devenue un nombre entier
#On évite donc ce genre d'erreur : "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
print("Stock:", var3 + var5)
