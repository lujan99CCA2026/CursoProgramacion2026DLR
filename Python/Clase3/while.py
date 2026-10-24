i = 1000
while i != 0:
    nomero = int(input("Ingrese su gasto "))
    if nomero > i:
        print("No tienes esa cantidad de dinero")
    else :
        i = i - nomero
    print(i)

    
print("Se te acabo el dinero ")