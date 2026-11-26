
class Animal:
    def __init__(self, n):
        self.nombre = n
    def hablar(self):
        print("...")

class Perro(Animal):
    def hablar(self):
        print("Guagu Guagu")    

class Gato(Animal):
    def hablar(self):
        print("Miau Miau")


class Vaca(Animal):
    def hablar(self):
            print("Muuu Muuu")


v = Vaca("Lola")
v.hablar()

p = Perro("Firilais")
p.hablar()

g = Gato("Copito")
g.hablar()