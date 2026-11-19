def agregar(lista):
    nombre = input("Ingrese el Nombre:")
    nota = float(input("Ingrese la Nota:"))
    lista.append({"nombre": nombre, "nota": nota})

def mostrar(lista):
    if len(lista)==0:
        print("Lista vacia")
    else : 
        for est in lista:
            print(est["nombre"], "=", est["nota"])

def promedio(lista):
    total = 0
    for est in lista:
        total = total + est["nota"]
    return total / len(lista)



def aprobados(lista):
    total = 0
    for est in lista:
        if est["nota"] >= 61:
            total = total +1
    return total 


def mejor(lista):
    el_mejor = lista[0]
    for est in lista:
        if est["nota"] >= el_mejor["nota"]:
            el_mejor = est
    return el_mejor 


def buscar(lista, nombre):
    for est in lista:
        if est['nombre'] == nombre:
            return est
    return None

# Primero tenemos que definir las varibles iniciales
# Declaramos el diccionario para poder guardar s nuestros con sus notas
# estudiantes = []
estudiantes = [
    {"nombre": "Ana", "nota": 85.0, "Apellido Paterno": "Condori"},
    {"nombre": "Luis", "nota": 58.0},
    {"nombre": "Eva", "nota": 90.0}
] 
#opcion ayuda a seleccionar la accion que quiere la persona 
opcion = ""

# Esqueleto de la funcion

while opcion != "0":
    print("=== REGISTRO DE NOTAS ===")
    print("1. Agregar  2. Mostrar")
    print("3. Estadísticas  4. Buscar")
    print("0. Salir")
    opcion = input("Opción: ")

    if opcion == "0":
        print("Hasta Luego")
    elif opcion == "1":
        agregar(estudiantes)
    elif opcion == "2":
        mostrar(estudiantes)
    elif opcion == "3":
        if len(estudiantes)== 0:
            print("No ha estudiantes para sacar estaadisticas")
        else:
            print("El promedio es:" , promedio(estudiantes))
            print("Aprobados son:", aprobados(estudiantes))
            m = mejor(estudiantes)
            print("Ele mejor es:", m["nombre"], "Con la nota de", m["nota"])
    elif opcion == "4":
        nombre = input("Ingrese el estudiante que quiere buscar")
        e = buscar(estudiantes, nombre)
        if e == None:
            print("Ese estudiante no existe")
        else: 
            print("El estudiante es:", e["nombre"], "Con la nota de", m["nota"])
    else:
        print("Opcion no valida")
        
print("Fin")  