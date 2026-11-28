



class Invetario:
    def __init__(self):
        self.__productos = []

    def agregar(self, producto):
        self.__productos.append(producto)

    def buscar(self, nombre):
        for p in self.__productos:
            if p.ver_nombre()== nombre:
                return p
        return None

    def valor_total(self):
        total = 0 
        for p in self.__productos:
            total = total + (p.precio_final()* p.ver_stock())
        return total
    
    def mostrar(self):
        for p in self.__productos:
            print(p)



