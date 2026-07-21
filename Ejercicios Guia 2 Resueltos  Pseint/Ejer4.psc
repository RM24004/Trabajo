Algoritmo Ejer4
		Definir contraseña Como Caracter
		Definir intentos Como Entero
		
		contraseña <- ""
		intentos <- 0
		
		Mientras contraseña <> "12345" Hacer
			
			Escribir "Ingrese la contraseña:"
			Leer contraseña
			
			intentos <- intentos + 1
			
			Si contraseña <> "12345" Entonces
				Escribir "Contraseña incorrecta."
			FinSi
			
		FinMientras
		
		Escribir "Acceso permitido."
		Escribir "Cantidad de intentos: ", intentos
		
FinAlgoritmo

