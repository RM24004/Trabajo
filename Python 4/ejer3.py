##funcion que retorne la longitud de una cadena ingresada por el usuario incluyendo los espacion el blancos contar vocales y consonantes y espacios en blanco
def contar_cadena():
    cadena = input("Ingrese una cadena de texto: ")
    longitud = len(cadena)
    vocales = sum(1 for char in cadena if char.lower() in 'aeiou')
    consonantes = sum(1 for char in cadena if char.lower() in 'bcdfghjklmnpqrstvwxyz')
    espacios_blancos = sum(1 for char in cadena if char.isspace())

    print(f"La longitud de la cadena es: {longitud}")
    print(f"Número de vocales: {vocales}")
    print(f"Número de consonantes: {consonantes}")
    print(f"Número de espacios en blanco: {espacios_blancos}")
# Llamar a la función para contar la cadena
contar_cadena()
