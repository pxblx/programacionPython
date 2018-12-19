#
# Ejercicio 8 de Arrays
#
# Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y que muestre a continuacion un diagrama
# de barras horizontales con esos datos. Las barras del diagrama se pueden dibujar a base de asteriscos o cualquier otro caracter.
#
# Pablo

# Pedir valores
temperaturas = []
for i in range(0,12):
    temperaturas.append(int(input("Introduce la temperatura del mes "+str(i+1)+": ")))

# Resultado
print("")
print("Grafico de temperaturas medias: ")
for e in temperaturas:
    print("*"*e)
