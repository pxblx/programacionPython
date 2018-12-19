#
# Ejercicio 12 de Secuenciales
#
# Pablo

import math

# Pedir valores
x1 = int(input("Introduce el valor para x1: "))
y1 = int(input("Introduce el valor para y1: "))
x2 = int(input("Introduce el valor para x2: "))
y2 = int(input("Introduce el valor para y2: "))

# Resultado
distancia=math.sqrt(math.pow((x2-x1),2)+math.pow(y2-y1,2))

print("La distancia entre los puntos es "+str(distancia)+".")
