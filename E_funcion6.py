"""
Programa que calcule el nuevo salario de un trabajador si obtuvo un
incremento del x%
"""

def nuevo_salario(sueldo,x):
    sueldo_f = sueldo + (sueldo*(x/100))
    return sueldo_f

sueldo1 = float(input("Indique el sueldo:"))
porcentaje = float(input("Indique el porcentaje de aumento:"))
sueldo_final = nuevo_salario(sueldo1,porcentaje)
print(sueldo_final)