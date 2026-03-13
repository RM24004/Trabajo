#calculadora de entrada a los juegos por edad
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad < 4:
    print(f"{nombre}, tu entrada es gratis.")

elif edad >=4 and edad < 18:
        print(f"{nombre}, tu entrada cuesta $5.")

elif edad >=18:
        print(f"{nombre}, tu entrada cuesta $10.")