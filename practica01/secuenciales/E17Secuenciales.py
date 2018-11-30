# Ejercicio 17 de Secuenciales
#
# pablo

# Pedir valores
horaSalida = int(input("Hora de salida: "))
minutoSalida = int(input("Minuto de salida: "))
segundoSalida = int(input("Segundo de salida: "))
tiempoInvertido = int(input("Tiempo invertido en segundos: "))

# Resultado
llegadaSegundos = horaSalida*3600+minutoSalida*60+segundoSalida+tiempoInvertido
horaLlegada = llegadaSegundos//3600;
minutoLlegada = (llegadaSegundos%3600)//60;
segundoLlegada = (llegadaSegundos%3600)%60;

print("Llegara a las "+str(horaLlegada)+":"+str(minutoLlegada)+":"+str(segundoLlegada)+".")
