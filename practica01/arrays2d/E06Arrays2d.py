#
# Ejercicio 6 de Arrays bidimensionales
#
# Modifica el programa anterior de tal forma que no se repita ningún número en el array.
#
# Pablo

import random

# Definicion de variables
nMax=0
nMin=1000
numeros = [[0 for x in range(10)] for y in range(6)]

# Resultado
for x in range(0,6):
    for y in range (0,10):
        aleatorio=random.randint(0,1001)
        while any(aleatorio in sublist for sublist in numeros):
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
print("El maximo esta en la posicion "+str(maxX+1)+"x"+str(maxY+1)+" y el minimo en la "+str(minX+1)+"x"+str(minY+1)+".")
