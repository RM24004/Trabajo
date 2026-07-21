Algoritmo Ejer8
		Definir cantidad, i Como Entero
		Definir nota1, nota2, nota3, promedio Como Real
		Definir aprobados, reprobados Como Entero
		
		aprobados <- 0
		reprobados <- 0
		
		Escribir "Ingrese la cantidad de estudiantes:"
		Leer cantidad
		
		Para i <- 1 Hasta cantidad Hacer
			
			Escribir ""
			Escribir "Estudiante número ", i
			
			Escribir "Ingrese la primera nota:"
			Leer nota1
			
			Escribir "Ingrese la segunda nota:"
			Leer nota2
			
			Escribir "Ingrese la tercera nota:"
			Leer nota3
			
			promedio <- (nota1 + nota2 + nota3) / 3
			
			Escribir "Promedio del estudiante: ", promedio
			
			Si promedio >= 6 Entonces
				Escribir "Estado: Aprobado"
				aprobados <- aprobados + 1
			SiNo
				Escribir "Estado: Reprobado"
				reprobados <- reprobados + 1
			FinSi
			
		FinPara
		
		Escribir ""
		Escribir "===== RESUMEN ====="
		Escribir "Estudiantes aprobados: ", aprobados
		Escribir "Estudiantes reprobados: ", reprobados
		
FinAlgoritmo	

