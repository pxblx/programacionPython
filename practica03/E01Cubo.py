"""
Ejercicio 1 de clases

Implementa en Python las clases GatoSimple, Cubo y Cuadrado vistas en el libro "Aprende Java con Ejercicios" y sus
respectivos programas de prueba (Estilo Java).
"""

class Cubo:
    def __init__(self, capacidad):
        self.__capacidad = capacidad
        self.__contenido = 0
    
    def get_capacidad(self):
        return self.__capacidad
    
    def get_contenido(self):
        return self.__contenido
    
    def set_contenido(self, litros):
        self.__contenido = litros
    
    def vacia(self):
        self.__contenido = 0
    
    def llena(self):
        self.__contenido = self.__capacidad
    
    def pinta(self):
        nivel = self.__capacidad
        while nivel > 0:
            if self.__contenido >= nivel:
                print("#~~~~#")     
            else:
                print("#    #")
            nivel -= 1
        print("######")

    def vuelca_en(self, destino):
        libres = destino.get_capacidad() - destino.get_contenido()
        if libres > 0:
            if self.__contenido <= libres:
                destino.set_contenido(destino.get_contenido() + self.__contenido)
                self.vacia()
            else:
                self.vacia()
        else:
            self.__contenido -= libres
            destino.llena()

# Principal
if __name__ == "__main__":
    cubito = Cubo(2)
    cubote = Cubo(7)
    print("Cubito:\n")
    cubito.pinta()
    print("\nCubote:\n")
    cubote.pinta()
    print("\nLleno el cubito:\n")
    cubito.llena()
    cubito.pinta()
    print("\nEl cubote sigue vacío:\n")
    cubote.pinta()
    print("\nAhora vuelco lo que tiene el cubito en el cubote.\n")
    cubito.vuelca_en(cubote)
    print("Cubito:\n")
    cubito.pinta()
    print("\nCubote:\n")
    cubote.pinta()
    print("\nAhora vuelco lo que tiene el cubote en el cubito.\n")
    cubote.vuelca_en(cubito)
    print("Cubito:\n")
    cubito.pinta()
    print("\nCubote:\n")
    cubote.pinta()
