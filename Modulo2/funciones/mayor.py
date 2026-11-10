# El mayor
# mayor(a, b) muestra cuál de los dos números es mayor, o si son iguales.


def mayor(a, b):
    if a > b:
        print("El mayor es el primer numero")
    elif a == b:
        print("son iguales")
    else:
        print("el segundo es el mayor")


# mayor(8,9)
# mayor(1,1)
# mayor(10,4)


def mayor_retorno(a, b):
    if a > b:
        return a
    elif a == b:
        return 0
    else:
       return b

print(mayor_retorno(8,9))
print(mayor_retorno(1,1))
print(mayor_retorno(10,4))