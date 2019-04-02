"""
Ejercicio 4 de ficheros

Realiza un programa que sea capaz de ordenar alfabéticamente las palabras
contenidas en un fichero de texto. El nombre del fichero que contiene las
palabras se debe pasar como argumento en la línea de comandos. El nombre
del fichero resultado debe ser el mismo que el original añadiendo la coletilla
sort, por ejemplo palabras_sort.txt. Suponemos que cada palabra ocupa una
línea.
"""
import sys
import os

if len(sys.argv) != 2:
    print("Se debe especificar como argumento el nombre del archivo.")
    exit(-1)
archivo = sys.argv[1]
archivo_nuevo = os.path.splitext(archivo)[0]+"_sort.txt"
palabras = []

try:
    with open(archivo, "r") as f:
        linea = f.readline()
        while linea:
            palabras.append(linea)
            linea = f.readline()
    palabras.sort()

    f = open(archivo_nuevo, "w")
    for palabra in palabras:
        f.write(palabra)
    f.close()
except FileNotFoundError:
    print("No se ha encontrado el archivo '" + archivo + "'.")
except IOError:
    print("No se ha podido escribir en el archivo '" + archivo_nuevo + "'.")
print("Archivo '" + archivo_nuevo + "' creado.")
