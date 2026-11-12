# Escriban contar_pares(lista) que devuelva cuántos números pares tiene.


def contar_pares(ren):
    pares = 0
    for i in ren:
        if i % 2 == 0:
            pares = pares + 1

    return pares


lista = [2, 4, 8, 1, 9, 12, 78, 99, 45,88,45,79,80,12]
# 2,4,8,12,78
print(contar_pares(lista))
