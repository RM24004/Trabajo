#division con validacion
print("Ingrese el dividendo:")
dividendo = float(input())
print("Ingrese el divisor:")
divisor = float(input())
if divisor != 0:
    resultado = dividendo / divisor
    print(f"El resultado de la división es: {resultado.__round__(2)}") #.round(2) redondea el resultado a 2 decimales
else:
    print("Error: No se puede dividir por cero.")
