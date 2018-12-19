#
# Ejercicio 15 de funciones
# 
# Muestra los números primos que hay entre 1 y 1000.
# 
# Pablo
#

from practica02.funciones.Matematicas import es_primo

print("| ", end = "")
for i in range (1, 1001):
    if es_primo(i):
        print(str(i)+" | ", end = "")
