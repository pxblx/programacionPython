"""
Ejercicio 2 de POO
"""
from practica04.E02.Vehiculo import Vehiculo
from practica04.E02.Bicicleta import Bicicleta
from practica04.E02.Coche import Coche

"""
Programa de prueba
"""
bicicleta = Bicicleta(450)
coche = Coche(138984)

while True:
    print("VEHÍCULOS\n" +
        "=========\n" +
        "1. Anda con la bicicleta\n" +
        "2. Haz el caballito con la bicicleta\n" +
        "3. Anda con el coche\n" +
        "4. Quema rueda con el coche\n" +
        "5. Ver kilometraje de la bicicleta\n" +
        "6. Ver kilometraje del coche\n" +
        "7. Ver kilometraje total\n" +
        "8. Salir\n")
    opcion = int(input("Elige una opción (1-8): "))

    if opcion == 1:
        bicicleta.arrancar()
        if bicicleta.en_marcha:
            print("Bicicleta en marcha")
        else:
            print("Bicicleta parada")
    elif opcion == 2:
        bicicleta.hacer_caballito()
        if bicicleta.haciendo_caballito:
            print("Bicicleta haciendo el caballito")
        else:
            print("Bicicleta dejando de hacer el caballito")
    elif opcion == 3:
        coche.arrancar()
        if coche.en_marcha:
            print("Coche arrancado")
        else:
            print("Coche parado")
    elif opcion == 4:
        coche.quemar_rueda()
        if coche.quemando_rueda:
            print("Coche quemando rueda")
        else:
            print("Coche dejando de quemar rueda")
    elif opcion == 5:
        print("La bicicleta ha recorrido "+str(bicicleta.kilometros_recorridos)+" kilómetros.")
    elif opcion == 6:
        print("El coche ha recorrido "+str(coche.kilometros_recorridos)+" kilómetros.")
    elif opcion == 7:
        print("El conjunto de "+str(Vehiculo.vehiculos_creados)+" vehículos ha recorrido "+str(Vehiculo.kilometros_totales)+" kilómetros.")
    elif opcion == 8:
        print("Saliendo")
        break
    else:
        print("Error: Opción incorrecta.")
