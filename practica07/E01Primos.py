"""
Ejercicio 1 de ficheros

Escribe un programa que guarde en un fichero con nombre primos.dat los
números primos que hay entre 1 y 500.
"""

NOMBRE_ARCHIVO = "primos.dat"
try:
    with open(NOMBRE_ARCHIVO, "w") as a:
        for i in range(2, 501):
            contador = 0
            for j in range(1, i+1):
                if i % j == 0:
                    contador += 1
            if contador < 3:
                a.write(str(i) + "\n")
    print("Archivo '" + NOMBRE_ARCHIVO + "' creado.")
except IOError:
    print("No se ha podido escribir en el archivo '" + NOMBRE_ARCHIVO + "'.")
