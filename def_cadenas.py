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

cadena = input("Ingresa cadena:")
#Necesitamos eliminar los espacios en blancos

sin_espacios = eliminar_espacios(cadena)
print(sin_espacios)

cadena_invertida = invertir_cadena(cadena)
print(cadena_invertida)

#print(eliminar_espacios(input("Ingresa otra cadena:")))
