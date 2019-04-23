"""
Ejercicio 5 de arrays

Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
"""

# Pedir valores
numeros = []
for i in range(0, 10):
    numeros.append(int(input("Introduce el " + str(i + 1) + " numero: ")))

# Resultado
print("El mayor introducido es " + str(max(numeros)) + " y el menor " + str(min(numeros)) + ".")
