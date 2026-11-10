
# Lo que usamos dentro de una def Solo sirve dentro de la misma
def calcular():
    resultado = 10 * 2
    return resultado


x = calcular()
print(x)          # 20
# print(resultado)  # NameError