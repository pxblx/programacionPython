"""
Ejercicio 1 de Excepciones

Realiza un programa que pida 6 números por teclado y nos diga cuál es el
máximo. Si el usuario introduce un dato erróneo (algo que no sea un número
entero) el programa debe indicarlo y debe pedir de nuevo el número.
"""

numeros = []
while len(numeros) < 6:
    try:
        numero = int(input("Introduce el " + str(len(numeros) + 1) + " número: "))
        numeros.append(numero)
    except ValueError:
        print("Los valores a introducir deben ser números enteros.")
print("\nEl máximo es " + str(max(numeros)) + ".")
print("El mínimo es " + str(min(numeros)) + ".")
