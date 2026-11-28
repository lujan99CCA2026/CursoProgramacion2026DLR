
DIAS_OFERTA = 3
DESCUENTO = 0.5
class Producto:
    """Este es el producto normal"""
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock


    def ver_nombre(self):
        return self.__nombre

    def ver_stock(self):
        return self.__stock

    def precio_final(self):
        return self.__precio

    def vender(self, cantidad):
        if cantidad <= self.__stock and cantidad >0:
            self.__stock = self.__stock - cantidad
            return True
        else:
            return False

    def __str__(self):
        precio = str(self.precio_final())
        return self.__nombre + " - Bs"+ precio+"- stock"+ str(self.__stock)


class Perecible(Producto):
    """Este producto es el mimo peor agregando el vencimiento """
    def __init__(self, nombre, precio, stock, dias):
        super().__init__(nombre, precio, stock)
        self.dias = dias
    # En esta funiocn se declarta el precio final pero con su descuento 
    def precio_final(self):
        precio =  super().precio_final()
        if self.dias <= DIAS_OFERTA:
            return precio * (1-DESCUENTO)
        else:
            return precio
