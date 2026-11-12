

# notas = [80, 20, 90, 10]
# #        0   1   2   3
# # print(notas[0])

# # print(notas[3])

# # print(notas[2])
# # Como cambiar una nota en especifico
# notas[1] = 1000

# # print(notas)
# # print(notas[1])
# # Agregar una nueva nota

# notas.append(78)

# # print(notas)
# # print(notas[4])

# # eliminar un valor 

# notas.remove(1000)

# print(notas)


# # # contar cuantas notas tengo

# # print(len(notas))


# # imprimir notas 
# suma = 0
# for hola in notas:
#     print(hola)
#     suma = suma + hola
# print(suma)
# print(suma/len(notas))


# for i in range(len(notas)):
#     print(i, notas[i])



# print(sum(notas))
# print(max(notas))
# print(min(notas))




numeros = []
print(numeros)

for i in range(5):
    num = float(input("Ingrese un numero"))
    numeros.append(num)

print(numeros)


def promedio(lista):
    return sum(lista) / len(lista)

print(promedio(numeros))

