#Determine les nombres concernés par mon programme
for nombre in range(1, 1001):

#On eclue le 1 de plage car ce n'est pas un nombre entier    
    if nombre > 1:
  
#Boucle pour tester la divisibilité par tous les nombres de 2 à nombre - 1
#Nombre -1 car un nombre divisible par lui même est premier 
        for i in range(2, nombre):
#Si nombre est divisible par i, ce n'est pas un nombre premier
            if nombre % i == 0:
                break
#Sinon si la boucle est parcourue sans break alors le nombre est premier et donc affiché !
        else:
            print(nombre)