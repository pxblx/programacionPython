"""
Ejercicio 3 (Cuadrado)
"""

from src.examen03.ejercicio03.src.Rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    @property
    def lado(self):
        return self.alto

    @lado.setter
    def lado(self, lado):
        self.alto = lado
        self.ancho = lado

    def __eq__(self, other):
        if isinstance(other, Cuadrado):
            if self.lado == other.lado:
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, Cuadrado):
            if self.lado > other.lado:
                return True
        return False

    def __ge__(self, other):
        if isinstance(other, Cuadrado):
            if self.lado > other.lado or self.lado == other.lado:
                return True
        return False
