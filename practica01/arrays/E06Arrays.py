"""
Ejercicio 6 de arrays

Escribe un programa que lea 15 numeros por teclado y que los almacene en un array. Rota los elementos de ese array, es decir, el
elemento de la posicion 0 debe pasar a la posicion 1, el de la 1 a la 2, etc. El numero que se encuentra en la ultima posicion debe
pasar a la posicion 0. Finalmente, muestra el contenido del array.
"""

# Pedir valores
numeros = []
for i in range(0, 15):
    numeros.append(int(input("Introduce el " + str(i+1) + " numero: ")))
print("\nArray original:\n| ", end="")
for i in numeros:
    print(str(i)+" | ", end="")
print("\n")

# Resultado
aux = numeros[len(numeros)-1]
e = len(numeros)-1
while e > 0:
    numeros[e] = numeros[e-1]
    e -= 1
numeros[0] = aux
print("Array rotado una posicion a la derecha:\n| ", end="")
for i in numeros:
    print(str(i)+" | ", end="")
