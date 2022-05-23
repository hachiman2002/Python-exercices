"""
.- Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

"""
num1 = int(input("num1?:"))
num2 = int(input("num2?:"))

if num2==0:
  print("Error divisor no debe ser igal a cero")
else:
  print(num1/num2)
