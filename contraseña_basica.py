#2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la 
#contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

passs= "holaaaa"

intento = str(input("Ingrese contrasena:"))
if passs == intento:
  print("correcta")
else:
  print("incorrecta")
