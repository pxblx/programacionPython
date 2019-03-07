"""
Ejercicio 2 de POO4

Realiza un programa que introduzca valores aleatorios (entre 0 y 100) en un
ArrayList y que luego calcule la suma, la media, el máximo y el mínimo de esos
números. El tamaño de la lista también será aleatorio y podrá oscilar entre 10
y 20 elementos ambos inclusive.

__author__ = Pablo
"""
import random


n = random.randint(10, 20)
r = random.randint(1, 100)
lista = []
suma = 0

for i in range(0, 5):
    lista.append(r)
    r = random.randint(1, 100)

for i in lista:
    suma = suma + r

print("Tamaño de la lista: "+str(len(lista)))
print("La suma es: "+str(suma))
print("La media es: "+str(suma/len(lista)))
print("El máximo es: "+str(max(lista)))
print("El mínimo es: "+str(min(lista)))
