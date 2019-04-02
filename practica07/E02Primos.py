"""
Ejercicio 2 de ficheros

Realiza un programa que lea el fichero creado en el ejercicio anterior y que
muestre los números por pantalla.
"""
archivo = "primos.dat"

try:
    with open(archivo, "r") as f:
        linea = f.readline()
        while linea:
            print(linea, end="")
            linea = f.readline()
        f.close()
except FileNotFoundError:
    print("No se ha encontrado el archivo '" + archivo + "'.")
