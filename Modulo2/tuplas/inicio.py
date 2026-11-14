
# en vez de usar [] estamos usando parentesis ()
fecha = (15,10,2026)

print(fecha)

print(fecha[0])

print(fecha[2])
# fecha[0] = 45



fecha = (13, 11, 2026)
dia, mes, david = fecha
print(david)  # 11
print(fecha[1])



def extremos(lista):
    return min(lista), max(lista)
 
a, b = extremos([70, 85, 64])
print(a, b)  # 64 85



def suma_y_promedio(lista):
    return sum(lista), (sum(lista)/len(lista))
 
a, b = suma_y_promedio([70, 85, 64])
print(a, b)  # 64 85



numeros = {3, 7, 3, 9, 7, 3}
print(numeros)
print(len(numeros))


frutas1 = {"manzana", "papay", "uva"}
frutas2 = {"manzana", "papay", "pera"}


print(frutas1 | frutas2)
print(frutas1 & frutas2)
print(frutas1 - frutas2)
print(frutas2 - frutas1)