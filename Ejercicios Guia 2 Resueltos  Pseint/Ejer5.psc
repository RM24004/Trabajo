Algoritmo Ejer5
		Definir nota Como Real
		Repetir
			
			Escribir "Ingrese una nota entre 0 y 10:"
			Leer nota
			
			Si nota < 0 O nota > 10 Entonces
				Escribir "Nota inválida."
			FinSi
			
		Hasta Que nota >= 0 Y nota <= 10
		
		Escribir "Nota registrada correctamente."
		Escribir "La nota ingresada es: ", nota
		
FinAlgoritmo
