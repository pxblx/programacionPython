"""
Ejercicio 2 de ficheros

Realiza un programa que lea el fichero creado en el ejercicio anterior y que
muestre los números por pantalla.
"""

NOMBRE_ARCHIVO = "primos.dat"
try:
    with open(NOMBRE_ARCHIVO, "r") as a:
        for linea in a:
            print(linea, end="")
except FileNotFoundError:
    print("No se ha encontrado el archivo '" + NOMBRE_ARCHIVO + "'.")
