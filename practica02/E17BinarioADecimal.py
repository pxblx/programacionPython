#
# Ejercicio 17 de funciones
# 
# Escribe un programa que pase de binario a decimal.
# 
# Pablo
#

resultado = 0

numero = int(input("Introduce un número binario: "))

for i in str(numero):
        resultado *= 2
        if i == '1':
            resultado +=1

print ("El número en decimal es "+str(resultado)+".")
