#contraseña valida ignorando minusculas mayusculas
contra = "password"

print("Ingrese su contraseña:")
verificar = input()

if verificar.lower() == contra: #.lower() convierte la entrada a minusculas para comparar con la contraseña almacenada
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")