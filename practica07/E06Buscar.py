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
archivo = sys.argv[1]
palabra = sys.argv[2]
palabras = []

try:
    with open(archivo, "r") as f:
        linea = f.readline()
        while linea:
            palabras.append(linea.rstrip("\n"))
            linea = f.readline()
        f.close()
except FileNotFoundError:
    print("No se ha encontrado el archivo '" + archivo + "'.")
print("Se han encontrado " + str(palabras.count(palabra)) + " ocurrencias de la palabra '" + palabra + "' en '" + archivo + "'.")
