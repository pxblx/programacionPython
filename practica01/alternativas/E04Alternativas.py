#
# Ejercicio 4 de Alternativas
#
# Crea un programa que pida al usuario dos numeros y muestre su division si el segundo no es cero, o un mensaje de aviso
# en caso contrario.
#
# Pablo

# Pedir valores
n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))

# Resultado
if n2==0:
    print("No se puede dividir entre 0.")
else:
    print("El resultado es "+str(n1/n2)+".")
