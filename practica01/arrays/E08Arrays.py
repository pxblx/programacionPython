"""
Ejercicio 8 de arrays

Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y que muestre a
continuacion un diagrama de barras horizontales con esos datos. Las barras del diagrama se pueden dibujar a base de
asteriscos o cualquier otro caracter.
"""

# Pedir valores
temperaturas = []
for i in range(0, 12):
    temperaturas.append(int(input("Introduce la temperatura del mes " + str(i + 1) + ": ")))

# Resultado
print("\nGrafico de temperaturas medias: ")
for i in temperaturas:
    print("*" * i)
