# compra.py · 10% de descuento si la compra pasa de 200 Bs


numero = int(input("Ingrese el el valor de su compra"))

if numero >200 :
    print("Tiene un 10 de descuento ")
    print(numero * 0.90)
else:
    print("No tiene descuento") 
    print(numero)