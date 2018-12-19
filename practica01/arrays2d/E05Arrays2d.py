#
# Ejercicio 5 de Arrays bidimensionales
#
# Realiza un programa que rellene un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0 y 1000 (ambos
# incluidos). A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.
#
# Pablo

import random

# Definicion de variables
nMax=0
nMin=1000
numeros = [[0 for x in range(10)] for y in range(6)]
maxPos = []
minPos = []

# Resultado
for x in range(0,6):
    for y in range (0,10):
        aleatorio=random.randint(0,1001)
        numeros[x][y]=aleatorio
        if aleatorio>nMax:
            nMax=aleatorio
            maxX=x
            maxY=y
        if aleatorio<nMin:
            nMin=aleatorio
            minX=x
            minY=y
for x in range(0,6):
    for y in range (0,10):
        print(str(numeros[x][y]).ljust(5), end="")
    print("")
print("")
print("El maximo esta en la posicion "+str(maxX)+"x"+str(maxY)+" y el minimo en la "+str(minX)+"x"+str(minY)+".")
