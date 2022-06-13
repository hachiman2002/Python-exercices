
def eliminar_espacios(cad):
    cad_aux=""
    for letra in cad:
        if letra!=" ":
            cad_aux = cad_aux + letra
    return cad_aux

def invertir_cadena(cad):
    cad_nueva=""
    for letra in cad:
        cad_nueva=letra+cad_nueva
    return cad_nueva

"""
Diseñar una funcion que permita evaluar si la cadena ingresada
es un palindromo. ejemplo oso, nadan, anita lava la tina
"""

def cadena_palindromo(cad):
    cad = eliminar_espacios(cad)
    inv=invertir_cadena(cad)

    if cad==inv:
        return True
    else:
        return False

cadena = input("Ingresa cadena:")
#Necesitamos eliminar los espacios en blancos

sin_espacios = eliminar_espacios(cadena)
print(sin_espacios)

cadena_invertida = invertir_cadena(cadena)
print(cadena_invertida)

if cadena_palindromo(cadena):
    print("Cadena es un palindromo")
else:
    print("Cadena no es un palindromo")


#print(eliminar_espacios(input("Ingresa otra cadena:")))
