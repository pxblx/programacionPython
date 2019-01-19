#
# Ejercicio 1 de clases
#
# Implementa en Python las clases GatoSimple, Cubo y Cuadrado vistas en el libro "Aprende Java con Ejercicios" y sus respectivos programas
# de prueba.
#
# Pablo
#

#
# Clase GatoSimple
#
class GatoSimple():
    
    def __init__(self, sexo):
        
        self.sexo = sexo
    
    def getSexo(self):
        
        return self.sexo
    
    def maulla(self):
        
        print("Miauuuu")
    
    def ronronea(self):
        
        print("mrrrrrr")
    
    def come(self, comida):
        
        if comida == "pescado":
            print("Hmmmm, gracias")
        else:
            print("Lo siento, yo solo como pescado")
    
    def peleaCon(self, contrincante):
        
        if self.getSexo() == "hembra":
            print("no me gusta pelear")
        else:
            if contrincante.getSexo() == "hembra":
                print("no peleo contra gatitas")
            else:
                print("ven aquí que te vas a enterar")

#
# Programa principal
#
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
    garfield.peleaCon(lisa)
    lisa.peleaCon(tom)
    tom.peleaCon(garfield)
