"""
Progra,a que valide si una contraseña es especificada por el usuario es segura
Una contraseña segura:
-tiene mas de 8 caracteres
-tiene al menos una letra mayuscula
-tiene al menos un numero
"""
"""
print(len("hola"))--> len verifica cuantos caracteres tiene la cadena
print("A".isupper())-->Verifica si hay mayuscula en una cadena
print("1".isnumeric())-->verifica si hay algun numero en la cadena
"""

def con_segura(contraseña):
    contm = 0
    contn = 0
    largo = False
    if len(contraseña)>8:
        largo = True
    for i in range(len(contraseña)):

        if contraseña[i].isnumeric():
            contn+=1
        if contraseña[i].isupper():
            contm=+1
    if contn >= 1 and contm >= 1 and largo == True:
        print("Es segura")
    else:
        print("No es segura")
contraseña1 = input("Digite contraseña:")
segura = con_segura(contraseña1)

