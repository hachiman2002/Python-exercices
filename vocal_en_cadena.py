"""
saber cuantas vocales hay en una palabra
probar con 4 palabras diferentes
"""

def vocal(cadena):
    cont = 0
    for i in cadena:
        if i in "aeiou":
            cont+=1
    print(f"La cadena {cadena} contiene {cont} vocales")

for a in range(0,4):
    vocal(input("Ingresa cadena:"))
