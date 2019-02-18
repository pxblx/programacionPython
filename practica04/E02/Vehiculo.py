"""
Ejercicio 2 de POO

Crea la clase Vehiculo, así como las clases Bicicleta y Coche como subclases de la primera. Para la clase Vehiculo,
crea los atributos de clase vehiculosCreados y kilometrosTotales, así como el atributo de instancia
kilometrosRecorridos. Crea también algún método específico para cada una de las subclases. Prueba las clases creadas
mediante un programa con un menú como el que se muestra a continuación:

VEHÍCULOS
=========
1. Anda con la bicicleta
2. Haz el caballito con la bicicleta
3. Anda con el coche
4. Quema rueda con el coche
5. Ver kilometraje de la bicicleta
6. Ver kilometraje del coche
7. Ver kilometraje total
8. Salir
Elige una opción (1-8):
"""

"""
Clase Vehiculo
"""
class Vehiculo(object):
    vehiculos_creados = 0
    kilometros_totales = 0

    """
    Constructor
    """
    def __init__(self, kilometros_recorridos):
        self.en_marcha = False
        self.kilometros_recorridos = kilometros_recorridos
        Vehiculo.vehiculos_creados = Vehiculo.vehiculos_creados + 1
        Vehiculo.kilometros_totales = Vehiculo.kilometros_totales + kilometros_recorridos

    """
    Arrancar el vehículo
    """
    def arrancar(self):
        if self.en_marcha:
            self.en_marcha = False
        else:
            self.en_marcha = True
