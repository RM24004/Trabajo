Algoritmo Ejer10
	Definir saldo, ret, opera, depo, trans Como Real
	saldo = 500
	Escribir "Bienvenido al Cajero Automatico"
	Escribir "Su saldo inicial es de: $", saldo
	
	Escribir "Operacion a realizar" 
	Escribir "1. Depositar" 
	Escribir "2. Retirar" 
	Leer opera
	
	Si opera = 1 Entonces
		Escribir "Cuanto va a depositar"
		Leer depo
		trans<-saldo + depo
		Escribir "Su nuevo saldo es de: $", trans
	SiNo
		Si opera = 2 Entonces
			Escribir "Cuanto va a retirar"
			Leer ret
			si ret > saldo Entonces
				Escribir "Su saldo Actual $", saldo ," es insuficiente"
			sino
				trans<-saldo - ret
			Escribir "Su nuevo saldo es de: $", trans
			FinSi
		FinSi
	Fin Si
FinAlgoritmo
