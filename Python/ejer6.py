#grupos de trabajo A mujeres B hombres
nombre = input("Ingrese su nombre: ")
print("Las mujeres ingresan al grupo A y los hombres al grupo B.")
genero = input("Ingrese su género (Masculino = M/Femenino = F): ")
if genero.upper() == "F":
    print(f"{nombre}, usted pertenece al grupo A de las mujeres.")
elif genero.upper() == "M":
    print(f"{nombre}, usted pertenece al grupo B de los hombres.")
else:
    print("Género no reconocido. Por favor ingrese 'M' para masculino o 'F' para femenino.")