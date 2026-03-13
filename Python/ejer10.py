#pizzeria vegetariana y no vegetaria mostrando los ingredientes al final 
nombre = input("Ingrese su nombre: ")
print("Bienvenido a la pizzería, por favor elija su tipo de pizza:")
print("1. Pizza Vegetariana")
print("2. Pizza No Vegetariana")

opcion = input("Ingrese el número de su opción (1 o 2): ")
if opcion == "1":
    print(f"{nombre}, has elegido la Pizza Vegetariana. Eliga los ingredientes adicionales:")
    print("a. Pimiento")
    print("b. Tofu")
    input_select = input("Ingrese el número de su opción (a o b): ")
    if input_select == "a":
        print(f"{nombre}, tu pizza vegetariana incluirá: Salsa de Tomate, Queso, Pimiento.")
    elif input_select == "b":   
        print(f"{nombre}, tu pizza vegetariana incluirá: Salsa de Tomate, Queso, Tofu.")

elif opcion == "2":
    print(f"{nombre}, has elegido la Pizza No Vegetariana. Eliga los ingredientes adicionales:")
    print("a. Pepperoni")
    print("b. Jamón")
    print("c. Salmon")
    input_select = input("Ingrese el número de su opción (a, b o c): ")
    if input_select == "a":
        print(f"{nombre}, tu pizza no vegetariana incluirá: Salsa de Tomate, Queso, Pepperoni.")
    elif input_select == "b":   
        print(f"{nombre}, tu pizza no vegetariana incluirá: Salsa de Tomate, Queso, Jamón.")
    elif input_select == "c":
        print(f"{nombre}, tu pizza no vegetariana incluirá: Salsa de Tomate, Queso, Salmon.")
  