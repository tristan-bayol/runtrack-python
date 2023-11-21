for nombre in range(1, 101):
# % me pert de definir si un nombre est un multiple de 3 ou 5
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    elif nombre % 3 == 0:
        print("Fizz")
    elif nombre % 5 == 0:
        print("Buzz")
    else:
        print(nombre)
