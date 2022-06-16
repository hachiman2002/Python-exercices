"""
comprobar si una palabra o frase es palindroma.
ejemplo:
-reconocer
-anna
-ojo rojo
-la ruta nos aparto a ptrp paso natural
"""

def sin_espacios(palabra):
    cad_aux = ""
    for letra in palabra:
        if letra!=" ":
            cad_aux = cad_aux + letra
    return cad_aux

def palabra_alrevez(palabra):
    alrevez = sin_espacios(palabra)
    cad_aux2 = ""
    for i in reversed(alrevez):
        cad_aux2 = cad_aux2 + i
    return cad_aux2
def palindromo(palabra):
    sin_e = sin_espacios(palabra)
    alv = palabra_alrevez(palabra)

    if sin_e == alv:
        return "Es palindromo"
    else:
        return "No es palindromo"

palabra_usuario = input("Ingrese Palabra:")

sinespacios = sin_espacios(palabra_usuario)
print(sinespacios)
alrevez = palabra_alrevez(palabra_usuario)
print(alrevez)
p_palindromo = palindromo(palabra_usuario)
print(p_palindromo)