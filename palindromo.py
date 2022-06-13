"""
Diseñar una funcion que permita evaluar si la cadena ingresada
es un palidromo. ejemplo oso, nadan, anita lava la tina
"""

def cadena(cad):
    cad_aux = ""

    for letra in cad:
        cad_aux=letra+cad_aux
    if cad_aux == cad:
        print("Es palidromo")

cadena1 = input("Ingresa cadena:")
palidromo = cadena(cadena1)
