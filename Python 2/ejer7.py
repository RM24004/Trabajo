#promedio del estudiante 
nombre = input("Ingrese el nombre del estudiante: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio de {nombre} es: {promedio.__round__(2)}")
