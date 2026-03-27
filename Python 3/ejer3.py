## pedir un numero mayor que 0 al usuario y mostrar sus divisores exactos
numero = int(input("Ingrese un número mayor que 0: "))
if numero <= 0:
    print("Por favor, ingrese un número mayor que 0.")
else:
    print("Los divisores exactos de", numero, "son:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
        