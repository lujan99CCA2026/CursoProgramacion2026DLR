# notas.py · pedir 5 notas con un for y mostrar el promedio

suma = 0
for i in range(1, 6):
    valor = int(input("Ingrese la nota "))
    suma = suma + valor
print(suma/5)