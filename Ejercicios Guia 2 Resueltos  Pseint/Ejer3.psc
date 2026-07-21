Algoritmo Ejer3
		Definir numero, suma, cantidad Como Entero
		
		suma <- 0
		cantidad <- 0
		
		Escribir "Ingrese números."
		Escribir "Ingrese 0 para finalizar."
		
		Leer numero
		
		Mientras numero <> 0 Hacer
			
			Si numero > 0 Entonces
				suma <- suma + numero
				cantidad <- cantidad + 1
			FinSi
			
			Escribir "Ingrese otro número:"
			Leer numero
			
		FinMientras
		
		Escribir "Cantidad de números positivos: ", cantidad
		Escribir "Suma de números positivos: ", suma
		
FinAlgoritmo