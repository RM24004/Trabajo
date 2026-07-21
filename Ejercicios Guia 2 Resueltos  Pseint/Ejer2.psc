Algoritmo Ejer2
	Definir opc Como Entero
    Definir val, resultado Como Real
	
    Escribir "===== CONVERSOR DE UNIDADES ====="
    Escribir "1. Metros a centímetros"
    Escribir "2. Kilómetros a metros"
    Escribir "3. Kilogramos a gramos"
    Escribir "4. Horas a minutos"
	
    Escribir "Seleccione una opción:"
    Leer opc
	
    Escribir "Ingrese el valor:"
    Leer val
	
    Segun opc Hacer
		
        1:
            resultado <- val * 100
            Escribir valor, " metros equivalen a ", resultado, " centímetros."
			
        2:
            resultado <- val * 1000
            Escribir valor, " kilómetros equivalen a ", resultado, " metros."
			
        3:
            resultado <- val * 1000
            Escribir valor, " kilogramos equivalen a ", resultado, " gramos."
			
        4:
            resultado <- val * 60
            Escribir val, " horas equivalen a ", resultado, " minutos."
			
        De Otro Modo:
            Escribir "Opción no válida."
			
    FinSegun
	
FinAlgoritmo