"""
Ejercicio 2 de POO
"""

from src.practica04.ejercicio02.Vehiculo import Vehiculo;

class Coche(Vehiculo):
    def __init__(self, kilometros_recorridos):
        super().__init__(kilometros_recorridos)
        self.quemando_rueda = False

    def quemar_rueda(self):
        if self.quemando_rueda:
            self.quemando_rueda = False
        else:
            self.quemando_rueda = True
