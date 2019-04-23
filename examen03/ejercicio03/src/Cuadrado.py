"""
Ejercicio 3 (Cuadrado)
"""

from src.examen03.ejercicio03.src.Rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def __eq__(self, other):
        if isinstance(other, Cuadrado):
            if self.alto == other.alto:
                return True
        return False
