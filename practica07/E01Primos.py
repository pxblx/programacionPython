"""
Ejercicio 1 de ficheros

Escribe un programa que guarde en un fichero con nombre primos.dat los
números primos que hay entre 1 y 500.
"""
archivo = "primos.dat"

try:
    f = open(archivo, "w")
    for i in range(2, 501):
        contador = 0
        for j in range(1, i+1):
            if i % j == 0:
                contador += 1
        if contador < 3:
            f.write(str(i) + "\n")
    f.close()
except IOError:
    print("No se ha podido escribir en el archivo '" + archivo + "'.")
print("Archivo '" + archivo + "' creado.")
