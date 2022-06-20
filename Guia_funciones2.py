"""
2.- Desarrolla una función que simule el lanzamiento de un dado. Muestra cuantas veces se obtuvo el valor 3.
Para el desarrollo puedes usar las siguientes variables:
N=cantidad de lanzamientos
I=conteo de lanzamientos
X=cada valor aleatorio (usa la función randint() )
C=contador de aciertos

"""
from random import randint
def lanzar_dado(lanzamientos):
    cont3 = 0
    for i in range(0,lanzamientos):
        cara = randint(1,6)
        if cara == 3:
            cont3+=1
    return cont3

n = int(input("Cantidad de lanzamientos:"))
contador3 = lanzar_dado(n)
print(f"El numero 3 salio {contador3} veces")