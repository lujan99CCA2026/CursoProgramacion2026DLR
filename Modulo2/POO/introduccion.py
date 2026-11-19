

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        return self.nota >= 61

    def mostrar(self):
        print(self.nombre, "-", self.nota)

    def subir(self, notaNueva):
        self.nota = self.nota + notaNueva
        if self.nota > 100:
            self.nota = 100
# instancias de la clase 
curso = [
    Estudiante("Ana", 85),
    Estudiante("Luis", 58),
    Estudiante("Eva", 90)
]
 
aprobados = 0
for e in curso:
    e.mostrar()
    if e.aprobo():
        aprobados += 1
print("Aprobados:", aprobados)
# ana = Estudiante("Ana", 85)
# luis = Estudiante("Luis", 58)
# david = Estudiante("David", 50)

# ana.subir(150)
# ana.mostrar

# luis.subir(50)
# luis.mostrar()
# 1
# Clase Producto con nombre, precio y stock; creen dos productos.
# 2
# Método mostrar(): «Arroz - Bs 8.5 - stock 20».
# 3
# Método vender(cantidad): resta del stock, o avisa «No hay suficiente».
# 4
# Método valor_total(): devuelve precio × stock.

class Producto:
    # def __init__(self, nombre, nota):
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar(self):
        print(self.nombre, "-", self.precio, "-", self.stock)

    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock = self.stock - cantidad
            print("QUeda ", self.stock, "en stock")
        else:
            print("No hay suficiente")
    def valor_total(self):
        return self.precio * self.stock

prodcutto1 = Producto("arroz", 10, 70)
prodcutto2 = Producto("papa", 100, 7)

# prodcutto2.mostrar()
# print(prodcutto2.valor_total())
# # prodcutto2.vender(10)

prodcutto1.mostrar()
print(prodcutto1.valor_total())
prodcutto1.vender(20)
print(prodcutto1.valor_total())
# prodcutto1.vender(10)

        




