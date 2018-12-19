#
# Ejercicio 4 de Arrays bidimensionales
#
# Modifica el programa anterior de tal forma que las sumas parciales y la suma total aparezcan en la pantalla con un pequeño retardo,
# dando la impresión de que el ordenador se queda “pensando” antes de mostrar los números
#
# Pablo

from time import sleep

# Pedir valores
numeros = [[0 for x in range(5)] for y in range(4)]
for x in range(0,4):
    for y in range (0,5):
        numeros[x][y]=int(input("Introduce el numero para la posicion "+str(x)+"x"+str(y)+": "))
print("")

# Resultado
suma=0
sumaTotal=0
for x in range(0,4):
    for y in range (0,5):
        print(str(numeros[x][y]).ljust(5), end="")
        suma=suma+numeros[x][y]
        y+=1
    sleep(1)
    print(suma)
    sumaTotal=sumaTotal+suma
    suma=0
    print("")
sumaColumna=0
for y in range (0,5):
    for x in range(0,4):
        sumaColumna=sumaColumna+numeros[x][y]
    sleep(1)
    print(str(sumaColumna).ljust(5), end="")
    sumaColumna=0
sleep(3)
print(sumaTotal)
