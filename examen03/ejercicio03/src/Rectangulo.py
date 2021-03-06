"""
Ejercicio 3 (Rectangulo)
"""

class Rectangulo(object):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        Rectangulo.__comprobar_alto_ancho(ancho)
        self.__ancho = ancho

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        Rectangulo.__comprobar_alto_ancho(alto)
        self.__alto = alto

    def __str__(self):
        resultado = ""
        for i in range(0, self.ancho):
            resultado += "[ ]"
        resultado += "\n"
        for i in range(1, self.alto - 1):
            resultado += "[ ]"
            for espacios in range(1, self.ancho - 1):
                resultado += "   "
            resultado += "[ ]\n"
        for i in range(0, self.ancho):
            resultado += "[ ]"
        resultado += "\n"
        return resultado

    @staticmethod
    def __comprobar_alto_ancho(valor):
        if valor <= 0 or valor > 10:
            raise ArithmeticError
