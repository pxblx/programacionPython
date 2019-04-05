from src.examen03.Ejercicio03.src.Rectangulo import Rectangulo

"""
Cuadrado (Ejercicio 3)
"""
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def __eq__(self, other):
        if isinstance(other, Cuadrado):
            if self.alto == other.alto:
                return True
        return False
