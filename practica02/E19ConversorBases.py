#
# Ejercicio 19 de funciones
# 
# Une y amplía los dos programas anteriores de tal forma que se permita convertir un número entre cualquiera de las siguientes
# bases: decimal, binario, hexadecimal y octal.
# 
# Pablo
#

from practica02.funciones.Matematicas import pega_por_detras, voltea

#
# Funciones
#
def binariooctal_a_decimal (n, b):
    
    res = 0
    pos = 0
    
    while n != 0:
        d = n%10
        res += d * (b**pos)
        pos += 1
        n //= 10
    
    return res

def decimal_a_binariooctal (n, b):
    
    res = n%b
    n //= b
    
    while n > 0:
        rest = n%b
        res = pega_por_detras(res, rest)
        n //= b
    
    return voltea(res)

def decimal_a_hexadecimal (n):
    
    hexadecimal = "0123456789ABCDEF"
    res = ""
    
    while True:
        rest = n%16
        res += hexadecimal[rest]
        n //= 16
        if n <= 0:
            break
    
    return voltea(res)

def hexadecimal_a_decimal (n):
    
    hexadecimal = "0123456789ABCDEF"
    res = 0
    
    for i in range (0, (len(str(n)))):
        pos = hexadecimal.find(str(n)[i])
        res = res*16 + pos;
    
    return res

#
# Principal
#
print("(1) Decimal a binario.")
print("(2) Decimal a octal.")
print("(3) Decimal a hexadecimal.")
print("(4) Binario a decimal.")
print("(5) Binario a octal.")
print("(6) Binario a hexadecimal.")
print("(7) Octal a decimal.")
print("(8) Octal a binario.")
print("(9) Octal a hexadecimal.")
print("(10) Hexadecimal a decimal.")
print("(11) Hexadecimal a binario.")
print("(12) Hexadecimal a octal.")
print()
opcion = int(input("Selecciona una de las opciones: "))
print()
if opcion < 10:
    numero = int(input("Introduce el número a convertir: "))
else:
    numero = input("Introduce el número a convertir: ")
print()

if opcion == 1:
    print(str(numero)+" en binario es "+str(decimal_a_binariooctal(numero, 2)))

elif opcion == 2:
    print(str(numero)+" en octal es "+str(decimal_a_binariooctal(numero, 8)))

elif opcion == 3:
    print(str(numero)+" en hexadecimal es "+decimal_a_hexadecimal(numero))

elif opcion == 4:
    print(str(numero)+" en decimal es "+str(binariooctal_a_decimal(numero, 2)))

elif opcion == 5:
    print(str(numero)+" en octal es "+decimal_a_binariooctal(binariooctal_a_decimal(numero, 2), 8))

elif opcion == 6:
    print(str(numero)+" en hexadecimal es "+decimal_a_hexadecimal(binariooctal_a_decimal(numero, 2)))

elif opcion == 7:
    print(str(numero)+" en decimal es "+str(binariooctal_a_decimal(numero, 8)))

elif opcion == 8:
    print(str(numero)+" en binario es "+decimal_a_binariooctal(binariooctal_a_decimal(numero, 8), 2))

elif opcion == 9:
    print(str(numero)+" en hexadecimal es "+decimal_a_hexadecimal(binariooctal_a_decimal(numero, 8)))

elif opcion == 10:
    print(str(numero)+" en decimal es "+str(hexadecimal_a_decimal(numero)))

elif opcion == 11:
    print(str(numero)+" en binario es "+decimal_a_binariooctal(hexadecimal_a_decimal(numero), 2))

elif opcion == 12:
    print(str(numero)+" en octal es "+decimal_a_binariooctal(hexadecimal_a_decimal(numero), 8))
    
else:
    print("La opción que has especificado no existe.")
