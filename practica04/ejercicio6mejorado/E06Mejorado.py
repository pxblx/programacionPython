"""
Ejercicio 6 de POO mejorado
"""

from _datetime import datetime, timedelta

formato = "%H:%M:%S"

tiempo1 = datetime.strptime("06:30:10", formato)
tiempo2 = datetime.strptime("13:23:55", formato)
tiempo3 = datetime.strptime("14:32:11", formato)

print("Tiempo 1: " + datetime.strftime(tiempo1, formato))
print("Tiempo 2: " + datetime.strftime(tiempo2, formato))
print("Tiempo 3: " + datetime.strftime(tiempo3, formato))

print("\nSuma de 1 + 2: " + datetime.strftime((tiempo1 + timedelta(seconds=tiempo2.second, hours=tiempo2.hour, minutes=tiempo2.minute)), formato))
print("Suma de 1 + 3: " + datetime.strftime((tiempo1 + timedelta(seconds=tiempo3.second, hours=tiempo3.hour, minutes=tiempo3.minute)), formato))
print("Suma de 3 + 1: " + datetime.strftime((tiempo3 - timedelta(seconds=tiempo1.second, hours=tiempo1.hour, minutes=tiempo1.minute)), formato))
