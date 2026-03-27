##funcion para las operaciones basicas y solicitar al usuario los numeros y la operacion a realizar
def operaciones_basicas():
    print("Bienvenido a la calculadora básica")
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Ingrese el número de la operación que desea realizar: ")

    if operacion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == '1':
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")
        elif operacion == '2':
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
        elif operacion == '3':
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
        elif operacion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Error: No se puede dividir por cero.")
    else:
        print("Operación no válida. Por favor, seleccione una opción del 1 al 4.")
# Llamar a la función para ejecutar la calculadora
operaciones_basicas()

