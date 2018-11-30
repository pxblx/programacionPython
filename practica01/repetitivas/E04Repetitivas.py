# Ejercicio 4 de Repetitivas
#
# Escribir un programa que imprima todos los numeros pares entre dos numeros que se le pidan al usuario.
#
# pablo

# Pedir valores
numero1 = int(input("Desde: "))
numero2 = int(input("Hasta: "))

# Resultado
if numero1%2 != 0:
    numero1=numero1+1

aux=numero1
while aux<=numero2:
    print(aux)
    aux=aux+2
