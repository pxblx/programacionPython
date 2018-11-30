# Ejercicio 3 de Secuenciales
#
# pablo

import math

# Pedir el valor de los catetos
cateto1 = int(input("Cateto 1: "))
cateto2 = int(input("Cateto 2: "))

# Resultado
hipotenusa = math.sqrt(math.pow(cateto1,2)+math.pow(cateto2,2))

print("La hipotenusa es "+str(hipotenusa)+" cm.")
