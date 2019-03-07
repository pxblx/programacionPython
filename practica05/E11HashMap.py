"""
Ejercicio 11 de POO4

Realiza un programa que escoja al azar 5 palabras en español del minidiccionario del ejercicio anterior. El programa
irá pidiendo que el usuario teclee la traducción al inglés de cada una de las palabras y comprobará si
son correctas. Al final, el programa deberá mostrar cuántas respuestas son
válidas y cuántas erróneas.

__author__ = Pablo
"""
import random


diccionario = {
    "hola": "hello",
    "adiós": "goodbye",
    "por favor": "please",
    "nombre": "name",
    "hoy": "today",
    "ayer": "yesterday",
    "semana": "week",
    "día": "day",
    "mes": "month",
    "lunes": "monday",
    "martes": "tuesday",
    "miércoles": "wednesday",
    "jueves": "thursday",
    "viernes": "friday",
    "sábado": "satuday",
    "domingo": "sunday",
    "enero": "january",
    "febrero": "february",
    "marzo": "march",
    "abril": "april"
}
correctas = 0
incorrectas = 0

for i in range(0, 5):
    palabra_aleatoria = random.choice(list(diccionario))
    prueba = input("Introduce la traducción de "+palabra_aleatoria+": ")
    if diccionario.get(palabra_aleatoria) == prueba:
        correctas = correctas + 1
    else:
        incorrectas = incorrectas + 1

print("\nHas acertado "+str(correctas)+" palabras y has fallado "+str(incorrectas)+".")
