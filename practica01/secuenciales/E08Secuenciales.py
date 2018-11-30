# Ejercicio 8 de Secuenciales
#
# pablo

# Pedir valores
salario = int(input("Introduce el salario base: "))
venta1 = int(input("Introduce el precio de la venta 1: "))
venta2 = int(input("Introduce el precio de la venta 2: "))
venta3 = int(input("Introduce el precio de la venta 3: "))

# Resultado
comisiones=venta1*0.1+venta2*0.1+venta3*0.1
total=salario+comisiones

print("Obtendra "+str(comisiones)+" en concepto de comisiones y "+str(total)+" en total.")
