##olicitar lista de numeros mostrar positivos y negativos y la suma de los positivos y negativos
numeros = input("Ingrese una lista de números separados por comas: ")
numeros_lista = numeros.split(",")
positivos = []
negativos = []
for num in numeros_lista:
    numero = int(num.strip())
    if numero > 0:
        positivos.append(numero)
    elif numero < 0:
        negativos.append(numero)
print("Números positivos:", positivos)
print("Números negativos:", negativos)
print("Total de números positivos:", len(positivos))
print("Total de números negativos:", len(negativos))
