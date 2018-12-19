#
# Ejercicio 15 de Repetitivas
#
# Introducir una cadena de caracteres e indicar si es un palindromo. Una palabra palindroma es aquella que se lee igual adelante que atras.
#
# Pablo

# Pedir valores
cadena = input("Introduce una cadena: ")

# Resultado
i=0
j=len(cadena)-1
while cadena[i]==cadena[j] and j>i:
    i+=1
    j-=1
if i>=j:
    print("La cadena es palindroma.")
else:
    print("La cadena no es palindroma.")
