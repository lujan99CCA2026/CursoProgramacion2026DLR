# mayor.py · pedir 5 números y mostrar el mayor
mayor = 0 
for i in range (1, 6 ):
    numero = int(input("Ingrese un numero"))
    if numero > mayor :
        mayor = numero 

print(mayor)
