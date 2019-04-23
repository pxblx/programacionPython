"""
Ejercicio 1 de clases

Implementa en Python las clases GatoSimple, Cubo y Cuadrado vistas en el libro "Aprende Java con Ejercicios" y sus
respectivos programas de prueba (Estilo Java).
"""

class GatoSimple:
    def __init__(self, sexo):
        self.__sexo = sexo
    
    def get_sexo(self):
        return self.__sexo

    @staticmethod
    def maulla():
        print("Miauuuu")

    @staticmethod
    def ronronea():
        print("mrrrrrr")
    
    @staticmethod
    def come(comida):
        if comida == "pescado":
            print("Hmmmm, gracias")
        else:
            print("Lo siento, yo solo como pescado")
    
    def pelea_con(self, contrincante):
        if self.get_sexo() == "hembra":
            print("no me gusta pelear")
        else:
            if contrincante.get_sexo() == "hembra":
                print("no peleo contra gatitas")
            else:
                print("ven aquí que te vas a enterar")

# Principal
if __name__ == "__main__":
    garfield = GatoSimple("macho")
    print("hola gatito")
    garfield.maulla()
    print("toma tarta")
    garfield.come("tarta selva negra")
    print("toma pescado, a ver si esto te gusta")
    garfield.come("pescado")

    tom = GatoSimple("macho")
    print("Tom, toma sopita de verduras")
    tom.come("sopa de verduras")

    lisa = GatoSimple("hembra")
    print("gatitos, a ver cómo maulláis")
    garfield.maulla()
    tom.maulla()
    lisa.maulla()
    garfield.pelea_con(lisa)
    lisa.pelea_con(tom)
    tom.pelea_con(garfield)
