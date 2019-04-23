"""
Ejercicio 10 de POO4

Crea un mini-diccionario español-inglés que contenga, al menos, 20 palabras
(con su correspondiente traducción). Utiliza un objeto de la clase HashMap para
almacenar las parejas de palabras. El programa pedirá una palabra en español
y dará la correspondiente traducción en inglés.
"""

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
palabra = input("Introduce una palabra en español: ")
if palabra in diccionario:
    print("La traducción en inglés es: " + diccionario.get(palabra))
else:
    print("La palabra no está en el diccionario.")
