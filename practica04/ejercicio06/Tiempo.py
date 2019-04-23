"""
Ejercicio 6 de POO

Crea la clase Tiempo con los métodos suma y resta. Los objetos de la clase Tiempo son intervalos de tiempo y se
crean de la forma Tiempo t = new Tiempo(1, 20, 30) donde los parámetros que se le pasan al constructor son las
horas, los minutos y los segundos respectivamente. Crea el método toString para ver los intervalos de tiempo de la
forma 10h 35m 5s. Si se suman por ejemplo 30m 40s y 35m 20s el resultado debería ser 1h 6m 0s. Realiza un programa
de prueba para comprobar que la clase funciona bien.
"""

class Tiempo:
    def __init__(self, h, m, s):
        if s >= 59:
            m = m + (s // 60)
            s = s % 60
        if m >= 59:
            h = h + (m // 60)
            m = m % 60

        self.horas = h
        self.minutos = m
        self.segundos = s

    def __str__(self):
        return str(self.horas) + "h " + str(self.minutos) + "m " + str(self.segundos) + "s"

    def suma(self, t):
        segundos = self.segundos+t.segundos
        minutos = self.minutos+t.minutos
        horas = self.horas+t.horas
        return Tiempo(horas, minutos, segundos)

    def resta(self, t):
        segundos = self.segundos - t.segundos
        minutos = self.minutos - t.minutos
        horas = self.horas - t.horas
        if segundos < 0:
            segundos = segundos + 60
            minutos = minutos - 1
        if minutos < 0:
            minutos = minutos + 60
            horas = horas - 1
        return Tiempo(horas, minutos, segundos)
