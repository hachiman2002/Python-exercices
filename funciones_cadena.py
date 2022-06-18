"""
Ejercicio con funciones:
Desarrolla un progrma que ingrese una cadena y usando funciones permita:
-Determinar la cantidad de espacios que hay en una cadena
-Devolver la cadena invertida
-Eliminar los espacios en blanco que pueda contener la cadena
"""
def funcion(cadena):
    cont=0
    for a in cadena:
        if a == " ":
            cont+=1
        else:
            pass
    return cont

def cadena_invetida(cadena):
    cad_aux = ""
    for i in range(len(cadena)-1,-1,-1):
        cad_aux=cad_aux+cad[i]
    return cad_aux
def eliminar_espacios(cadena):
    cad_aux2 = ""
    for b in range(len(cadena)-1,-1,-1):
        if b == ""
        
    cad_aux2=cad_aux2+cad[b]


cad = input("Ingresa cadena:")

espacios = funcion(cad)
print("La cantidad de espacios son:", espacios)

invertida = cadena_invetida(cad)
print("La cadena invertida es:",invertida)

sin_espacios = eliminar_espacios(cad)
print(f"Cadena sin espacios:{sin_espacios} ")
