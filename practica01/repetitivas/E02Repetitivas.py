# Ejercicio 2 de Repetitivas
#
# Realizar un algoritmo que pida numeros (se pedira por teclado la cantidad de numeros a introducir). El programa debe informar de cuantos
# numeros introducidos son mayores que 0, menores que 0 e iguales a 0.
#
# pablo

# Pedir valores
cantidad = int(input("Introduce la cantidad de numeros que vas a guardar: "))

# Resultado
contador=0
contadorMayores=0
contadorMenores=0
contadorIguales=0
while contador<cantidad:
    numero = int(input("Introduce un numero: "))
    if numero>0:
        contadorMayores+=1
    if numero<0:
        contadorMenores+=1
    if numero==0:
        contadorIguales+=1
    contador+=1

print("Has introducido "+str(contadorMayores)+" numeros mayores a 0, "+str(contadorIguales)+" iguales a 0 y "+str(contadorMenores)+" menores a 0.")
