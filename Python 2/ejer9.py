#evaluar si el usuario es mayor de edad
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print(f"{nombre}, usted es mayor de edad.")
else:
    print(f"{nombre}, usted es menor de edad.")