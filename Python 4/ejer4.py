##funcion para verificar email debe de verificar que tenga un @ y un .com
def verificar_email():
    email = input("Ingrese su correo electrónico: ")

    if "@" in email and email.endswith(".com"):
        print("Correo electrónico válido.")
    else:
        print("Correo electrónico no válido. Debe contener '@' y terminar con '.com'.")
# Llamar a la función para verificar el email
verificar_email()
