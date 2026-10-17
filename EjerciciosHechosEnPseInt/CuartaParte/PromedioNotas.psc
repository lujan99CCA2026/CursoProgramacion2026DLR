Algoritmo PromedioNotas
	Definir suma, num Como Entero
	Definir promedio Como Real
	suma <- 0
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Escribir "Ingrese la nota ",i
		Leer num
		suma <- suma + num 
	Fin Para
	promedio <- suma/5
	Escribir "El primedio es ", promedio
FinAlgoritmo
