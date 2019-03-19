#
# Ejercicio 16 de funciones
# 
# Muestra los números capicúa que hay entre 1 y 99999.
# 
# Pablo
#

from src.practica02.funciones.Matematicas import es_capicua

print("| ", end = "")
for i in range (1, 100000):
    if es_capicua(i):
        print(str(i)+" | ", end = "")
