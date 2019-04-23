"""
Ejercicio 2

Haz un programa en Java y Python que calcule el elemento N (se pide al usuario) de la serie de Fibonacci.
"""

# Pedir el valor de N
n = int(input("Numero de elemento de la serie Fibonacci: "))

# Calcular la serie de Fibonacci
if n < 3:
    fibonacci = 1
else:
    aux1 = 1
    aux2 = 1
    for x in range(2, n):
        fibonacci = aux1 + aux2
        aux1 = aux2
        aux2 = fibonacci

# Resultado
print("El " + str(n) + " numero de la serie Fibonacci es " + str(fibonacci) + ".")
