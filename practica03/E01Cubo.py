#
# Ejercicio 1 de clases
#
# Implementa en Python las clases GatoSimple, Cubo y Cuadrado vistas en el libro "Aprende Java con Ejercicios" y sus respectivos programas
# de prueba.
#
# Pablo
#

#
# Clase Cubo
#
class Cubo():
    
    def __init__(self, capacidad):
        
        self.capacidad = capacidad
        self.contenido = 0
    
    def getCapacidad(self):
        
        return self.capacidad
    
    def getContenido(self):
        
        return self.contenido
    
    def setContenido(self, litros):
        
        self.contenido = litros
    
    def vacia(self):
        
        self.contenido = 0
    
    def llena(self):
        
        self.contenido = self.capacidad
    
    def pinta(self):
        
        nivel = self.capacidad
        while nivel > 0:
            
            if self.contenido >= nivel:
                print("#~~~~#")     
            else:
                print("#    #")
            
            nivel -= 1
        
        print ("######")
    
    def vuelcaEn(self, destino):
        
        libres = destino.getCapacidad() - destino.getContenido()
        
        if libres > 0:
            if self.contenido <= libres:
                destino.setContenido(destino.getContenido() + self.contenido)
                self.vacia()
            else:
                self.vacia()
        else:
            self.contenido -= libres
            destino.llena()

#
# Programa principal
#
cubito = Cubo(2)
cubote = Cubo(7)
print ("Cubito:\n")
cubito.pinta()
print()
print ("Cubote:\n")
cubote.pinta()
print()
print("Lleno el cubito:\n")
cubito.llena()
cubito.pinta()
print()
print("El cubote sigue vacío:\n")
cubote.pinta()
print()
print("Ahora vuelco lo que tiene el cubito en el cubote.\n")
cubito.vuelcaEn(cubote)
print ("Cubito:\n")
cubito.pinta()
print()
print ("Cubote:\n")
cubote.pinta()
print()
print("Ahora vuelco lo que tiene el cubote en el cubito.\n")
cubote.vuelcaEn(cubito)
print ("Cubito:\n")
cubito.pinta()
print()
print ("Cubote:\n")
cubote.pinta()
