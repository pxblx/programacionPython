#
# Ejercicio 18 de funciones
# 
# Escribe un programa que pase de decimal a binario.
# 
# Pablo
#

from practica02.funciones.Matematicas import pega_por_detras, voltea

numero = int(input("Introduce un número decimal: "))

resultado = numero%2
numero //= 2

while numero > 0:
    resto = numero%2
    resultado = pega_por_detras(resultado, resto)
    numero //= 2

print ("El número en binario es "+str(voltea(resultado))+".")
