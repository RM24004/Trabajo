# Ejercicio 1 nombre y edad si es mayor
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print(f"{nombre}, usted es mayor de edad.")
else:    
    print(f"{nombre}, usted es menor de edad.")
