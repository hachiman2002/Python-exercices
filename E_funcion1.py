"""
Programa que tome las tres notas de un estudiante y diga las nota fincal de curso.
Tenga en cuenta que la primera y las segunda nota valen en 30% de la nota final.La tercera nota vale el 40%
"""

def calcular_nota(n1,n2,n3):
    promedio = (n1*0.30)+(n2*0.30)+(n3*0.40)
    return promedio

nota1 = float(input("Indique nota 1:"))
nota2 = float(input("Indique nota 2:"))
nota3 = float(input("Indique nota 3:"))

nota_final = calcular_nota(nota1,nota2,nota3)

print(f"La nota final es {nota_final:.1f}")