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
NOMBRE_ARCHIVO = sys.argv[1]
NOMBRE_ARCHIVO_NUEVO = os.path.splitext(NOMBRE_ARCHIVO)[0] + "_sort.txt"
try:
    palabras = []
    with open(NOMBRE_ARCHIVO, "r") as a:
        for linea in a:
            palabras.append(linea)
    palabras.sort()
    with open(NOMBRE_ARCHIVO_NUEVO, "w") as a:
        for palabra in palabras:
            a.write(palabra)
    print("Archivo '" + NOMBRE_ARCHIVO_NUEVO + "' creado.")
except FileNotFoundError:
    print("No se ha encontrado el archivo '" + NOMBRE_ARCHIVO + "'.")
except IOError:
    print("No se ha podido escribir en el archivo '" + NOMBRE_ARCHIVO_NUEVO + "'.")
