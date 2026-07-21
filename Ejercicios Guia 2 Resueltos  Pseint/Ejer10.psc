Funcion promedio <- CalcularPromedio(nota1, nota2, nota3)
	
    promedio <- (nota1 + nota2 + nota3) / 3
	
FinFuncion

Algoritmo Ejer10
	
    Definir cantidad, i Como Entero
    Definir nota1, nota2, nota3, promedio Como Real
	
    Escribir "Ingrese la cantidad de estudiantes:"
    Leer cantidad
	
    Para i <- 1 Hasta cantidad Hacer
		
        Escribir ""
        Escribir "===== ESTUDIANTE ", i, " ====="
		
        Escribir "Ingrese la primera nota:"
        Leer nota1
		
        Escribir "Ingrese la segunda nota:"
        Leer nota2
		
        Escribir "Ingrese la tercera nota:"
        Leer nota3
		
        promedio <- CalcularPromedio(nota1, nota2, nota3)
		
        Escribir "Promedio: ", promedio
		
        Si promedio >= 9 Entonces
            Escribir "Clasificación: Excelente"
        SiNo
            Si promedio >= 7 Entonces
                Escribir "Clasificación: Bueno"
            SiNo
                Si promedio >= 6 Entonces
                    Escribir "Clasificación: Regular"
                SiNo
                    Escribir "Clasificación: Reprobado"
                FinSi
            FinSi
        FinSi
		
    FinPara
	
FinAlgoritmo