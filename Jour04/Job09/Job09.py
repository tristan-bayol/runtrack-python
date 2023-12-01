L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

#Defini la valeur max dans "L"
def maximum (L):
    maxi = L[0]
    for i in L :    
        if i > maxi :
            maxi = i
    return maxi

#Defini la valeur min dans "L"
def minimum (L):
    mini = L[0]
    for i in L :    
        if i < mini :
            mini = i
    return mini

maxi = maximum(L)
mini = minimum(L)
print ( f"La valeur max est de : {maxi}"f"\nLa valeur min est de : {mini}")
