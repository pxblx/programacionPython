# Ejercicio 19 de Alternativas
#
# Escribe un programa que pida 10 numeros por teclado y que luego muestre los numeros introducidos junto con las palabras maximo
# y minimo al lado del maximo y del minimo respectivamente.
#
# pablo

# Pedir valores
mes = int(input("Introduce el numero del mes: "))

# Resultado
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    print("El mes tiene 31 dias.")
elif mes==2:
    print("El mes tiene 28 dias o 29 si es bisiesto.")
elif mes==4 or mes==6 or mes==9 or mes==11:
    print("El mes tiene 30 dias.")
else:
    print("Mes incorrecto.")
