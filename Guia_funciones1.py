"""
1.- Para el pago semanal de un empleado se consideran lo siguientes datos: horas trabajadas, valor por hora y
descuentos. Si la cantidad de horas en la semana es mayor a 40, se le debe pagar las horas extras con una bonificación
de 50% adicional al pago normal.

Variables a considerar:
	c=cantidad de horas trabajadas semanalmente
	t=tarifa por hora
	d=descuentos del pago semanal
	p=pago del empleado
Desarrolla el programa en base a una función que determine el pago de cada empleado.


"""
def calcular_sueldo(c,t,d):
    pago_t = (c * t) - (d)
    if c>40:
        pago_e = (c-40)*(t+(t/2))
    return pago_t+pago_e
c = int(input("Horas trabajadas semanalmente:"))
t = float(input("Tarifa por hora:"))
d = float(input("Descuentos del pago semanal:"))
pago = calcular_sueldo(c,t,d)
print(f"El pago final es ${pago} ")