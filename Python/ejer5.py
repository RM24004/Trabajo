# mayoria de edad e impuestos si salario es mayor a 360

edad = int(input("Ingrese su edad: "))
salario = float(input("Ingrese su salario: "))

if edad >= 18 and salario > 360:
    print("Usted es mayor de edad y debe pagar renta.")
elif edad >= 18 and salario <= 360:
    print("Usted es mayor de edad pero no debe pagar renta.")
else:
    print("Usted es menor de edad y no deberia trabajar.")
