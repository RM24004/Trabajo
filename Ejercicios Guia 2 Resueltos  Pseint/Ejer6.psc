Algoritmo Ejer6
		Definir opcion Como Entero
		Definir saldo, cantidad Como Real
		saldo <- 500
		
		Repetir
			
			Escribir ""
			Escribir "===== CAJERO AUTOMÁTICO ====="
			Escribir "1. Consultar saldo"
			Escribir "2. Depositar dinero"
			Escribir "3. Retirar dinero"
			Escribir "4. Salir"
			Escribir "Seleccione una opción:"
			Leer opcion
			
			Segun opcion Hacer
				
				1:
					Escribir "Su saldo actual es: $", saldo
					
				2:
					Escribir "Ingrese la cantidad a depositar:"
					Leer cantidad
					
					Si cantidad > 0 Entonces
						saldo <- saldo + cantidad
						Escribir "Depósito realizado correctamente."
						Escribir "Nuevo saldo: $", saldo
					SiNo
						Escribir "La cantidad debe ser mayor que cero."
					FinSi
					
				3:
					Escribir "Ingrese la cantidad a retirar:"
					Leer cantidad
					
					Si cantidad > saldo Entonces
						Escribir "Fondos insuficientes."
					SiNo
						Si cantidad > 0 Entonces
							saldo <- saldo - cantidad
							Escribir "Retiro realizado correctamente."
							Escribir "Nuevo saldo: $", saldo
						SiNo
							Escribir "La cantidad debe ser mayor que cero."
						FinSi
					FinSi
					
				4:
					Escribir "Gracias por utilizar el cajero automático."
					
				De Otro Modo:
					Escribir "Opción no válida."
					
			FinSegun
			
		Hasta Que opcion = 4
		
FinAlgoritmo
