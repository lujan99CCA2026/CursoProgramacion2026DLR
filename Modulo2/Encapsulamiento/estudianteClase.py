# 1
# Clase Estudiante con nombre y nota 
# privados, y ver_nombre() y ver_nota().
# 2
# cambiar_nota(nueva): solo acepta 
# de 0 a 100; si no, «Nota inválida».
# 3
# aprobo() usando el atributo privado.
# 4
# Prueben cambiar_nota(150) y 
# print(e.__nota): ¿qué pasa?

class Estudiante:
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    def ver_nombre(self):
        return self.__nombre
    def ver_nota(self):
        return self.__nota

    def cambiar_nota(self, notaNueva):
        if notaNueva <0 or notaNueva >100:
            print("Nota invalida")
        else:
            self.__nota = notaNueva

    def aprobo(self):
        if self.__nota >=61:
            print("aprobo")
        else:
            print("reprobo")



m = Estudiante("ana", 67)
print(m.ver_nombre(), m.ver_nota())

m.cambiar_nota(90)
print(m.ver_nombre(), m.ver_nota())

m.aprobo()
