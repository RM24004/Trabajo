#convertir de colones salvadoreños a dólares
tasa_cambio = 8.75  # Tasa de cambio actual
colones = float(input("Ingrese la cantidad en colones salvadoreños: "))
dolares = colones / tasa_cambio
print(f"{colones} colones salvadoreños equivalen a {dolares.__round__(2)} dólares.")
