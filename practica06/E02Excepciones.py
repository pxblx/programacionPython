"""
Ejercicio 2 de Excepciones

Modifica la clase Gato vista anteriormente añadiendo el método apareaCon.
Este método debe comprobar que los gatos son de distinto sexo, tras lo
cual, genera un nuevo gato. Por ejemplo, sería válido algo como Gato cria
= garfield.apareaCon(lisa). En caso de que los gatos sean del mismo sexo,
el método debe generar la excepción ExcepcionApareamientoImposible. Crea un
programa desde el que se pruebe el método.
"""

from src.practica03.E01GatoSimple import GatoSimple
from random import randint

class ExcepcionApareamientoImposible(Exception):
    def __init__(self):
        super(ExcepcionApareamientoImposible, self).__init__(
            "El apareamiento es imposible porque los gatos son del mismo sexo.")

class GatoSimpleMejorado(GatoSimple, object):
    def __init__(self, sexo):
        super().__init__(sexo)

    def aparea_con(self, gato):
        if self.get_sexo() == gato.get_sexo():
            raise ExcepcionApareamientoImposible
        else:
            sexos = ["macho", "hembra"]
            return GatoSimpleMejorado(sexos[randint(0, 1)])

# Principal
if __name__ == "__main__":
    garfield = GatoSimpleMejorado("macho")
    tom = GatoSimpleMejorado("macho")
    lisa = GatoSimpleMejorado("hembra")

    gatito = garfield.aparea_con(tom)
    gatito.maulla()
