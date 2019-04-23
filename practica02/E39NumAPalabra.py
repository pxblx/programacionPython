"""
Ejercicio 39 de funciones

Esta función convierte los dígitos del número n en las correspondientes palabras y lo devuelve todo en una cadena de
caracteres. Por ejemplo, el 470213 convertido a palabras sería: cuatro, siete, cero, dos, uno, tres.
Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por
pantalla, solo se debe usar print desde el programa principal. Fíjate que hay una coma detrás de cada palabra
salvo al final.
"""

def digito_escrito(n):
    if n == 0:
        return "cero"
    elif n == 1:
        return "uno"
    elif n == 2:
        return "dos"
    elif n == 3:
        return "tres"
    elif n == 4:
        return "cuatro"
    elif n == 5:
        return "cinco"
    elif n == 6:
        return "seis"
    elif n == 7:
        return "siete"
    elif n == 8:
        return "ocho"
    elif n == 9:
        return "nueve"
    else:
        return "?"

def num_a_palabra(n):
    res = digito_escrito(int(str(n)[0]))
    for i in range(1, len(str(n))):
        res = res + ", " + digito_escrito(int(str(n)[i]))
    res = res + "."
    return res
