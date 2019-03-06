"""
Ejercicio 3 de POO4

Escribe un programa que ordene 10 números enteros introducidos por teclado
y almacenados en un objeto de la clase ArrayList.

__author__ = Pablo
"""
lista = []

for i in range(0, 10):
    valor = int(input("Introduce el "+str(i+1)+" valor: "))
    lista.append(valor)

lista.sort()

print("\n| ", end="")
for i in lista:
    print(str(i)+" | ", end="")
