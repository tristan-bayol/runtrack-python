def calcule(num1,operator,num2):
    if operator == "+":
        resultat = num1 + num2
    elif operator == "-":
        resultat = num1 - num2
    elif operator == "*":
        resultat = num1 * num2
    elif operator == "/":
        resultat = num1 / num2
    elif operator == "%":
        resultat = num1 % num2
    return resultat

resultat = calcule(5,"*",4)
print (resultat)

