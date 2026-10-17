Algoritmo LaEdad
	Escribir "Ingrese anio de nacimiento"
	Leer nacimiento
	Escribir "Ingrese el anio actual"
	Leer actual
	edad <- actual - nacimiento
	Si edad >= 18 Entonces
		Escribir "La persona tiene ",edad ," y es mayor de edad"
	SiNO 
		Escribir "La persona tiene", edad , " y no es mayor de edad"
	FinSi
FinAlgoritmo
