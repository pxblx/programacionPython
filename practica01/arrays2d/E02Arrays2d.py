#
# Ejercicio 2 de Arrays bidimensionales
#
# Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5 columnas. El programa
# mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara. La suma total debe aparecer en la
# esquina inferior derecha.
#
# Pablo

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
    print(suma)
    sumaTotal=sumaTotal+suma
    suma=0
    print("")
sumaColumna=0
for y in range (0,5):
    for x in range(0,4):
        sumaColumna=sumaColumna+numeros[x][y]
    print(str(sumaColumna).ljust(5), end="")
    sumaColumna=0
print(sumaTotal)
