Algoritmo Ejer1
		Definir opcion Como Entero
		Definir numero1, numero2, resultado Como Real
		
		Escribir "===== MENU DE OPERACIONES ====="
		Escribir "1. Sumar"
		Escribir "2. Retar"
		Escribir "3. Multiplicar"
		Escribir "4. Dividir"
		Escribir "5. Salir"
		Escribir "Seleccione una opción:"
		Leer opcion
		
		Si opcion >= 1 Y opcion <= 4 Entonces
			
			Escribir "Ingrese el primer número:"
			Leer numero1
			
			Escribir "Ingrese el segundo número:"
			Leer numero2
			
		FinSi
		
		Segun opcion Hacer
			
			1:
				resultado <- numero1 + numero2
				Escribir "El resultado de la suma es: ", resultado
				
			2:
				resultado <- numero1 - numero2
				Escribir "El resultado de la resta es: ", resultado
				
			3:
				resultado <- numero1 * numero2
				Escribir "El resultado de la multiplicación es: ", resultado
				
			4:
				Si numero2 <> 0 Entonces
					resultado <- numero1 / numero2
					Escribir "El resultado de la división es: ", resultado
				SiNo
					Escribir "No se puede dividir entre cero."
				FinSi
				
			5:
				Escribir "Programa finalizado."
				
			De Otro Modo:
				Escribir "Opción no válida."
				
		FinSegun
		
FinAlgoritmo
