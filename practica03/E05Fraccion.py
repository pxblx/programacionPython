#
# Ejercicio 5 de clases
# 
# Crea una clase Fraccion de forma que podamos hacer las siguientes operaciones:
# - Contruir un objeto Fraccion pasándole al constructor el numerador y el denominador.
# - Obtener la fracción.
# - Obtener y modificar numerador y denominador. No se puede dividir por cero.
# - Obtener resultado de la fracción (número real).
# - Multiplicar la fracción por un número.
# - Multiplicar, sumar y restar fracciones.
# - Simplificar la fracción.
# 
# Pablo
#
class E05Fraccion():
    
    #
    # Método constructor
    #
    def __init__(self, numerador, denominador):
        while True:
            self.numerador = numerador
            self.denominador = denominador
            if self.denominador == 0:
                print("No se puede dividir por 0.")
                self.denominador = int(input("Introduce el nuevo denominador:"))
            else:
                break
    
    #
    # Muestra la fracción por pantalla
    #
    def getFraccion(self):
        print(self.numerador,"/",self.denominador)
    
    #
    # Modifica la fracción
    #
    def modificar(self):
        print("Modificar: ",self.numerador,"/",self.denominador)
        while True:
            self.numerador = int(input("Introduce el nuevo numerador: "))
            self.denominador = int(input("Introduce el nuevo denominador: "))
            if self.denominador == 0:
                print("No se puede dividir por 0.")
            else:
                break
    
    #
    # Muestra por pantalla el resultado de dividir la fracción
    #
    def getResultado(self):
        print(self.numerador/self.denominador)
    
    #
    # Multiplica la fracción por el número que se pasa como parámetro
    #
    def multiplicarEntero(self, numero):
        print((self.numerador*numero),"/",self.denominador)
    
    #
    # Multiplica una fracción por otra que se pasa como parámetro
    #
    def multiplicar(self, fraccion):
        print((self.numerador*fraccion.numerador),"/",(self.denominador*fraccion.denominador))
    
    #
    # Calcula el MCD de dos números que se pasan como parámetro
    #
    def mcd(self, n1, n2):
        minimo = min(n1, n2)
        for i in range (1, minimo+1):
            if n1%i == 0 and n2%i == 0:
                mcd = i
        return mcd
    
    #
    # Suma una fracción por otra que se pasa como parámetro
    #
    def sumar(self, fraccion):
        mcm = (self.denominador*fraccion.denominador)/(E05Fraccion.mcd(self,self.denominador,fraccion.denominador))
        print(int(((mcm/self.denominador)*self.numerador)+((mcm/fraccion.denominador)*fraccion.numerador)),"/",int(mcm))
    
    #
    # Resta una fracción por otra que se pasa como parámetro
    #
    def restar(self, fraccion):
        print(int(((self.numerador*fraccion.denominador)-(self.denominador*fraccion.numerador))),"/",int((self.denominador*fraccion.denominador)))
    
    #
    # Simplifica una fracción
    #
    def simplificar(self):
        mcd = E05Fraccion.mcd(self,self.numerador,self.denominador)
        print(int(self.numerador/mcd),"/",int(self.denominador/mcd))
