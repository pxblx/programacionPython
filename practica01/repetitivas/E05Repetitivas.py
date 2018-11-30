# Ejercicio 5 de Repetitivas
#
# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el limite inferior es mayor que el superior lo tiene
# que volver a pedir. A continuacion se van introduciendo numeros hasta que introduzcamos el 0. Cuando termine el programa dara las
# siguientes informaciones:
# - La suma de los numeros que estan dentro del intervalo (intervalo abierto).
# - Cuantos numeros estan fuera del intervalo.
# - Informa si hemos introducido algun numero igual a los limites del intervalo.
#
# pablo

# Pedir valores
while True:
    desde = int(input("Desde: "))
    hasta = int(input("Hasta: "))
    if desde<hasta:
        break
numero = int(input("Introduce un numero: "))

# Resultado
suma=0
fuera=0
igual=0
while True:
    suma=suma+numero
    if numero<desde or numero>hasta:
        fuera+=1
    if numero==desde or numero==hasta:
        igual+=1
    numero = int(input("Introduce un numero: "))
    if numero==0:
        break

print("Has introducido "+str(fuera)+" numeros fuera del rango, "+str(igual)+" numeros iguales a los limites y la suma de todos es igual a "+str(suma)+".")
