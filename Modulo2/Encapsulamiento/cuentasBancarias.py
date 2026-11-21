class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        # __atributo lo convierte en un atributo privado
        self.__saldo = saldo
    def retirar(self, monto):
        if monto <= self.saldo:
            self.__saldo -= monto

    def ver_saldo(self):
        return self.__saldo
 
    def ver_titular(self):
        return self.__titular
        
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("Monto inválido")
 
    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("No se puede retirar")

c = CuentaBancaria("Ana", 10000)
 
print(c.ver_titular(), c.ver_saldo())  # Ana 100

c.depositar(50)    # 150
print(c.ver_titular(), c.ver_saldo())  # Ana 100
c.retirar(500) 
print(c.ver_titular(), c.ver_saldo())  # Ana 100

