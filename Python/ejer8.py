#bono de merito de empleados por evaluacion de desempeño
nombre = input("Ingrese su nombre: ")
salario = float(input("Ingrese su salario mensual: "))
puntaje = float(input("Ingrese su puntaje de desempeño (0.0 a 0.6): "))

if puntaje <= 0.0:
    bono = 0.0
    salario_total = salario + bono
    print(f"{nombre}, su bono de mérito inaceptable y de: ${bono:.2f}. Su salario total es: ${salario_total:.2f}.")

elif puntaje > 0.0 and puntaje <= 0.4:
    bono = puntaje * 100
    salario_total = salario + bono
    print(f"{nombre}, su bono de mérito es aceptable y de: ${bono:.2f}. Su salario total es: ${salario_total:.2f}.")

elif puntaje >= 0.6:
    bono = puntaje * 100
    salario_total = salario + bono
    print(f"{nombre}, su bono de mérito es meritorio y de: ${bono:.2f}. Su salario total es: ${salario_total:.2f}.")   