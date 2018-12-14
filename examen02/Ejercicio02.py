#
# Ejercicio 2 de Python
#
# Pablo
#

# Función para comprobar la letra
def comprobar_letra (dni):
    
    # Variables
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    posic = letras.find(dni[8])
    
    # Validación
    if (posic == -1):
        return False
    elif ((int(dni[0:8])%23) != letras.find(dni[8])):
        return False
    
    return True

# Función para validar los números
def validar_dni (dni):
    
    # Variables
    numeros = "0123456789"
    
    for i in range (0,7):
        if not (dni[i] in numeros):
            return False
    
    if not (comprobar_letra(dni)):
            return False
    
    return True

# Pedir el DNI
dni = input("Introduce un DNI para validar: ")

# Validar el DNI
if (validar_dni(dni)):
    print("Es válido.")
else:
    print("No es válido.")
