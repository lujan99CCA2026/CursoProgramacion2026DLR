

def area_rectangulo(base, altura):
    print(base*altura)
    print("La base es:", base)
    print("La altura es: ", altura)

def area_rectangulo_retorno(base, altura):
    return base*altura

# area_rectangulo(45, 100)

# resultad = area_rectangulo_retorno(45, 100)
# print(resultad)


def saludar(nombre, apellido):
    return ("saludos", nombre, "de apellido",  apellido)

salida = saludar("david", "lujan")
print(salida)