#Definitions des Variables
#var1 = Montant initiale
#var2 = Taux Initiale

#Choix du montant initiale
var1=int(input("Entrez le montant de votre investissement "))
print("Investissement",var1, "€")
var2=int(input("Entrée votre taux de rendement en pourcentage sans le signe % "))

#Calcul du rendement annuel après avoir demander les interet à l'utilisateur !
var3=((var1 * var2)/100)
print("Rendement Annuel=",var3, "€")

#Augmentation de "var 1" et de "var 2" de 2%
var4=var1+5000 #Montant initiale + 5000 euros
var5=(var2 + 2)#Aungmentation du taux initiale de 2%
var6=((var4 * var5)/100)
print("Rendement annuel après ajout de 5000 euros=", var6, "€")

#Retrait de 10%
var7=((var4 * 10)/100)#Calcul des 10%
var8=(var4 - var7)#Retrait des 10%
print("Investissement Final", var8, "€")

var9=(var5 - 1)#Diminution du rendement de 1%
var10= ((var8 * var9)/100)
print("Rendement annuel Final", var10, "€")

