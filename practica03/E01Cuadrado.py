#
# Ejercicio 1 de clases
#
# Implementa en Python las clases GatoSimple, Cubo y Cuadrado vistas en el libro "Aprende Java con Ejercicios" y sus respectivos programas
# de prueba.
#
# Pablo
#

#
# Clase Cuadrado
#
class Cuadrado():

    def __init__(self, lado):
        
        self.__lado = lado
    
    def __str__(self):
        
        resultado = ""
        
        c = 0
        while c < self.__lado:
            
            resultado += "##"
            c += 1
        
        resultado += "\n"
        
        c = 1
        while c < self.__lado-1:
            
            resultado += "##"
            
            espacios = 1
            while espacios < self.__lado-1:
                
                resultado += "  "
                espacios += 1
            
            resultado += "##\n"
            
            c +=1
        
        c = 0
        while c < self.__lado:
            
            resultado += "##"
            c += 1
        
        resultado += "\n"
        
        return resultado

#
# Programa principal
#
if __name__ == "__main__":
    miCuadradito = Cuadrado(5)
    print(miCuadradito)
