"""
Ejercicio 6 de ficheros

Realiza un programa que diga cuántas ocurrencias de una palabra hay en un
fichero. Tanto el nombre del fichero como la palabra se deben pasar como
argumentos en la línea de comandos.
"""

import sys

if len(sys.argv) != 3:
    print("Se deben especificar como argumentos el nombre del archivo y la palabra a buscar.")
    exit(-1)
NOMBRE_ARCHIVO = sys.argv[1]
PALABRA = sys.argv[2]
try:
    palabras = []
    with open(NOMBRE_ARCHIVO, "r") as a:
        for linea in a:
            palabras.append(linea.rstrip("\n"))
    print("Se han encontrado " + str(palabras.count(PALABRA)) + " ocurrencias de la palabra '" + PALABRA + "' en '" + NOMBRE_ARCHIVO + "'.")
except FileNotFoundError:
    print("No se ha encontrado el archivo '" + NOMBRE_ARCHIVO + "'.")
