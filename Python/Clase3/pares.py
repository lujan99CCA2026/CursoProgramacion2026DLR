# pares.py · sumar los números pares del 1 al n

limite = int(input("Ingrese el limite "))
suma = 0 

for j in range (2, limite+2, 2):
    print(j)
    suma = suma + j
print(suma)