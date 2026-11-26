#  Esta clase esta definiendo que todas las clases hija deben de tener la funcion area 
class Figura:
    def area(self):
        return 0
class Rectangulo(Figura):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return self.b * self.h
class Circulo(Figura):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

class Triangulo(Figura):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return self.b * self.h /2 


figuras = [
    Rectangulo(3, 4),
    Circulo(2),
    Rectangulo(5, 1),
    Triangulo(5, 10)
]
for f in figuras:
    print(f.area())


def informe(f):
    print("Área:", f.area())
 
def area_total(lista):
    total = 0
    for f in lista:
        total += f.area()
    return total
 
informe(Circulo(1))        # Área: 3.14
print(area_total(figuras)) # 35.56