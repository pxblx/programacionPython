# Ejercicio 11 de Alternativas
#
# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triangulo.
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
# - Si se cumple Pitagoras entonces es triangulo rectangulo
# - Si solo dos lados del triangulo son iguales entonces es isosceles.
# - Si los 3 lados son iguales entonces es equilatero.
# - Si no se cumple ninguna de las condiciones anteriores, es escaleno.
#
# pablo

# Pedir valores
a = int(input("Introduce el valor para A: "))
b = int(input("Introduce el valor para B: "))
c = int(input("Introduce el valor para C: "))

# Resultado
if a==b and a==c:
    print("Equilatero.")
elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("Triangulo rectangulo.")
elif (a==b and a!=c) or (b==c and b!=a) or (c==a and c!=b):
    print("Isosceles.")
else:
    print("Escaleno.")
