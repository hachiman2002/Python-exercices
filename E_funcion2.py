"""
Programa que calcule el IVA de una compra, siendo el IVA del 19%
sobre el valor total de la compra
"""

def calcular_iva(valor):
    iva = valor*0.19
    return iva

compra = float(input("Ingrese el valor de la compra:"))
iva_compra = calcular_iva(compra)
print(f"IVA de la compra:{iva_compra:.2f}")