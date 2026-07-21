Algoritmo Ejer7
	Definir compra, desc Como Real
	Escribir "Ingrese el Total de la compra"
	Escribir "Por compras mayores de $100 se le aplicara un descuento del 10%"
	Leer compra
	Si compra > 100 Entonces
		Escribir "Su compra es de : $", compra
		desc<-compra * 0.10
		Escribir "Su descuento es de: $", desc
		Escribir "Su total a pagar es: $", compra - desc
	SiNo
		Escribir "Su compra es de menor a $100"
		Escribir "No recibe descuento"
		Escribir "Su total a pagar es: $", compra
	Fin Si
FinAlgoritmo
