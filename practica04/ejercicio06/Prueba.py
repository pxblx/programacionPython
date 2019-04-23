"""
Ejercicio 6 de POO
"""

from src.practica04.ejercicio06.Tiempo import Tiempo

prueba = Tiempo(15, 59, 60000000)
prueba2 = Tiempo(9, 67, 57)
print(prueba)
print(prueba2)
print(prueba.suma(prueba2))
