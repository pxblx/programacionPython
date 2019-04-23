"""
Ejercicio 2 de POO
"""

from src.practica04.ejercicio02.Vehiculo import Vehiculo;

class Bicicleta(Vehiculo):
    def __init__(self, kilometros_recorridos):
        super().__init__(kilometros_recorridos)
        self.haciendo_caballito = False

    def hacer_caballito(self):
        if self.haciendo_caballito:
            self.haciendo_caballito = False
        else:
            self.haciendo_caballito = True
