"""
3.- Desarrolla una función que permita emular el lanzamiento de dos dados y muestre la cantidad de
veces que los dados tuvieron el mismo resultado
"""
from random import randint
def lanzar_dado(lanzamientos):
    contc = 0
    for i in range(0,lanzamientos):
        cara = randint(1,6)
        cara2 = randint(1,6)
        print(cara)
        print(cara2)
        if cara == cara2:
            contc+=1
    return contc

n = int(input("Cantidad de lanzamientos:"))
contador_iguales = lanzar_dado(n)
print(f"Mismo resultado: {contador_iguales} ")