## verificar longitud del numero de documento del usuario solicitarnombre y dui
def verificar_documento():
    nombre = input("Ingrese su nombre: ")
    dui = input("Ingrese su número de documento (DUI): ")

    if len(dui) == 8 and dui.isdigit():
        print(f"Bienvenido, {nombre}. Su número de documento es válido.")
    else:
        print("Número de documento no válido. El DUI debe tener 8 dígitos.")
# Llamar a la función para verificar el documento
verificar_documento()

