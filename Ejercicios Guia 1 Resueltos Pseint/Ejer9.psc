Algoritmo Ejer9
	Definir val1, val2, resul, opera Como Real
	Escribir "Calculadora"
	
	Escribir "Ingrese el valor 1"
	Leer val1
	Escribir "Ingrese el valor 2"
	Leer val2
	
	Escribir "Seleccione la operacion"
	Escribir "1. Suma"
	Escribir "2. Resta"
	Escribir "3. Multiplicacion"
	Escribir "4. Division"
	Leer opera
	
	Si opera = 1 Entonces
		resul<-val1 + val2
		Escribir "Ël resultado de la operacion suma es: ", resul
	SiNo
		si opera = 2 Entonces
			resul<-val1 - val2
			Escribir "Ël resultado de la operacion resta es: ", resul
		SiNo
			si opera = 3 Entonces
				resul<-val1 * val2
				Escribir "Ël resultado de la operacion multiplicacion es: ", resul
			SiNo
				resul<-val1 / val2
				Escribir "Ël resultado de la operacion division es: ", resul
			FinSi
		FinSi
	Fin Si
FinAlgoritmo
