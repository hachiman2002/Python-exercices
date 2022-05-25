"""
4.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

"""
contraseña = str(input("Contraseña:"))
con = "hola"

while contraseña != con:
   contraseña = str(input("Error,contraseña:"))

if contraseña == con:
    print("Correcto!")
