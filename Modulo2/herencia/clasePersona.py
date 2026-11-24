class Personas:
    # constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
 
    def presentarse(self):
        print("Soy", self.nombre, "y tengo", self.edad, "años")


class Estudiante(Personas):
    def __init__(self, nombre, edad, carrera, nota):
        # Atributos que esta heredando de la persona
        super().__init__(nombre, edad)
        # Atributo nuevo que voy a tener como estudiante 
        self.carrera = carrera
        self.nota = nota

    def aprobo(self):
        return self.nota >= 61

class Docente(Personas):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre,edad)
        self.materia = materia

        
    def presentarse(self):
        super().presentarse()
        print("Enseño", self.materia)





e = Estudiante("Pedro", 18, "Sistemas", 20)


e.presentarse()
print(e.aprobo())

f = Docente("Bruno", 55, "calculo" )
f.presentarse()


# Docente
# p = Personas("Juan", 21)
# # Estudiante 
# a = Personas("Maria", 25)
# a.presentarse()
# p.presentarse()