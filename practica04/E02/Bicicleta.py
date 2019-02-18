"""
Ejercicio 2 de POO
"""
from practica04.E02.Vehiculo import Vehiculo;

"""
Subclase Bicicleta
"""
class Bicicleta(Vehiculo):
    """
    Constructor

    :param kilometros_recorridos: kilómetros recorridos
    """
    def __init__(self, kilometros_recorridos):
        super().__init__(kilometros_recorridos)
        self.haciendo_caballito = False

    """
    Hacer el caballito
    """
    def hacer_caballito(self):
        if self.haciendo_caballito:
            self.haciendo_caballito = False
        else:
            self.haciendo_caballito = True
