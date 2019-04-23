"""
Ejercicio 1

Haz un programa en Java y Python que calcule el combinatorio de dos numeros. Si hay un error en la introduccion debe indicarlos.
"""

# Pedir los valores de N y M
n = int(input("Introduce N: "))
m = int(input("Introduce M: "))
while n < m:
    n = int(input("Introduce N: "))
    m = int(input("Introduce M: "))

# Calcular el factorial de N
contador = n
factorialN = 1
for x in range(1, n):
    factorialN = factorialN*contador
    contador = contador-1

# Calcular el factorial de M
contador = m
factorialM = 1
for x in range(1, m):
    factorialM = factorialM*contador
    contador = contador-1

# Calcular el factorial de N-M
contador = n - m
factorialNM = 1
for x in range(1, n-m):
    factorialNM = factorialNM * contador
    contador = contador - 1

# Calcular el combinatorio de N y M y sacarlo por pantalla
combinatorio = factorialN / (factorialNM * factorialM)
print("El combinatorio de " + str(n) + " y " + str(m) + " es " + str(combinatorio) + ".")
