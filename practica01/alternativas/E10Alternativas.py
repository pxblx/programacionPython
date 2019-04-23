"""
Ejercicio 10 de alternativas

Algoritmo que pida los puntos centrales x1, y1, x2, y2 y los radios r1,r2 de dos circunferencias y las clasifique en
uno de estos estados:
    - Exteriores.
    - Tangentes exteriores.
    - Secantes
    - Tangentes interiores.
    - Interiores.
    - Concentricas.
"""

import math

# Pedir valores
x1 = int(input("Introduce el valor para x1: "))
y1 = int(input("Introduce el valor para y1: "))
x2 = int(input("Introduce el valor para x2: "))
y2 = int(input("Introduce el valor para y2: "))
r1 = int(input("Introduce el valor para r1: "))
r2 = int(input("Introduce el valor para r2: "))

# Resultado
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
if (r1 + r2) < d:
    print("Exteriores.")
if (r1 + r2) == d:
    print("Tangentes exteriores.")
if (r1 + r2) > d > abs(r1 - r2):
    print("Secantes.")
if d == abs(r1 - r2):
    print("Tangentes interiores.")
if 0 < d < abs(r1 - r2):
    print("Interiores.")
if d == 0:
    print("Concentricas.")
