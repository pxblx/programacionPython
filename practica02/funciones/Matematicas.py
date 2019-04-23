"""
Ejercicios 1 - 14

Crea una biblioteca de funciones matemáticas que contenga las siguientes funciones. Recuerda que puedes usar unas
dentro de otras si es necesario.
Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho
trabajo. Por ejemplo, la función esCapicua resulta trivial teniendo voltea y la función siguientePrimo también es muy
fácil de implementar teniendo esPrimo.

    1. esCapicua: Devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
    2. esPrimo: Devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
    3. siguientePrimo: Devuelve el menor primo que es mayor al número que se pasa como parámetro.
    4. potencia: Dada una base y un exponente devuelve la potencia.
    5. digitos: Cuenta el número de dígitos de un número entero.
    6. voltea: Le da la vuelta a un número.
    7. digitoN: Devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y
    de izquierda a derecha.
    8. posicionDeDigito: Da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se
    encuentra, devuelve -1.
    9. quitaPorDetras: Le quita a un número n dígitos por detrás (por la derecha).
    10. quitaPorDelante: Le quita a un número n dígitos por delante (por la izquierda).
    11. pegaPorDetras: Añade un dígito a un número por detrás.
    12. pegaPorDelante: Añade un dígito a un número por delante.
    13. trozoDeNumero: Toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo
    correspondiente.
    14. juntaNumeros: Pega dos números para formar uno.
"""

def es_capicua(n):
    if n == voltea(n):
        return True
    else:
        return False

def es_primo(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

def siguiente_primo(n):
    ++n
    while not es_primo(n):
        ++n
    return n

def potencia(b, e):
    return b ** e

def digitos(n):
    return len(str(n))

def voltea(n):
    return str(n)[:: - 1]

def digito_n(n, d):
    return int(str(n)[d + 1])

def posicion_de_digito(n, d):
    return int(str(n).find(d))

def quita_por_detras(n, d):
    return int(str(n)[0:(len(str(n))) - d])

def quita_por_delante(n, d):
    return voltea(quita_por_detras(voltea(n), d))

def pega_por_detras(n, m):
    return int(str(n) + str(m))

def pega_por_delante(n, m):
    return int(str(m) + str(n))

def trozo_de_numero(n, i, f):
    return int(str(n)[i + 1:f + 1])

def junta_numeros(n, m):
    return pega_por_detras(n, m)
