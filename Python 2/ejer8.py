#horas trabajadas ingresando nombre, horas trabajadas y pago por hora
nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))
salario = horas_trabajadas * pago_por_hora
print(f"El salario de {nombre} es: {salario.__round__(2)}")

