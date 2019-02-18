"""
Ejercicio 2 de POO
"""
from practica04.E02.Vehiculo import Vehiculo;

"""
Subclase Coche
"""
class Coche(Vehiculo):
    """
    Constructor

    :param kilometros_recorridos: kilómetros recorridos
    """
    def __init__(self, kilometros_recorridos):
        super().__init__(kilometros_recorridos)
        self.quemando_rueda = False

    """
    Quemar rueda
    """
    def quemar_rueda(self):
        if self.quemando_rueda:
            self.quemando_rueda = False
        else:
            self.quemando_rueda = True
