#
# Ejercicio 9 de Repetitivas
#
# Mostrar en pantalla los N primeros numero primos. Se pide por teclado la cantidad de numeros primos que queremos mostrar.
#
# Pablo

import math

# Pedir valores
n = int(input("Numero de numeros primos a generar: "))

# Resultado
print(2)
contador=0
actual=3
i=3
while contador < n:
    primo = True
    while i<=math.sqrt(actual) and primo:
        if actual%i==0:
            primo=False
        i+=2
    if primo:
        contador+=1
        print(actual)
    actual+=2
