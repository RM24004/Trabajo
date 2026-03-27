##calcular factorial del numero ingresado mayor que 0 por el usuario
numero = int(input("Ingrese un número mayor que 0 para calcular su factorial: "))
if numero <= 0:
    print("Por favor, ingrese un número mayor que 0.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print("El factorial de", numero, "es:", factorial)
