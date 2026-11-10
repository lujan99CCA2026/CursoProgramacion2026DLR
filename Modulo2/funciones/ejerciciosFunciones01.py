# cuadrado(n) · devolver n × n y mostrar los cuadrados del 1 al 5

def cuadrado(n):
    return n*n
# print(cuadrado(1))
# print(cuadrado(2))
# print(cuadrado(3))
# print(cuadrado(4))
# print(cuadrado(5))

# for i in range(1,6):
#     print(cuadrado(i))

# es_mayor(edad) · devolver True o False y usarlo en un if

def es_mayor(edad):
    return edad>=18

# if es_mayor(80):
#     print("Es mayor de edad")
# else:
#     print("No es mayor de edad")



# precio_final(precio, descuento=10) · devolver el precio con descuento

def precio_final(precio, descuento=10):
    return precio - descuento


# print(precio_final(100))

# promedio(a, b, c) · devolverlo y decir si aprobó (61 o más)


def promedio(a, b, c):
    promedio = (a+b+c)/3
    return promedio>=61

print(promedio(57, 61, 61))

if promedio(29,47,56):
    print("Aprobado")
else:
    print("reprobado")