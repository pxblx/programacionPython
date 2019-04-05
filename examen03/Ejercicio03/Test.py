from src.examen03.Ejercicio03.src.Cuadrado import Cuadrado
from src.examen03.Ejercicio03.src.Rectangulo import Rectangulo

"""
Programa de prueba para las clases Rectángulo y Cuadrado (Ejercicio 3)
"""
# Prueba Rectángulo
rectangulo1 = Rectangulo(10, 5)
print("Rectángulo 1:\n" + str(rectangulo1))
try:
    rectangulo2 = Rectangulo(6, -4)
    print("Rectángulo 2:\n" + str(rectangulo2))
except ArithmeticError:
    print("Las medidas no pueden tomar valores negativos o 0.\n")

# Prueba Cuadrado
cuadrado1 = Cuadrado(5)
cuadrado2 = Cuadrado(8)
print("Cuadrado 1:\n" + str(cuadrado1))
print("Cuadrado 2:\n" + str(cuadrado2))
print("¿Son iguales los dos cuadrados?\n" + str(cuadrado1.__eq__(cuadrado2)))
