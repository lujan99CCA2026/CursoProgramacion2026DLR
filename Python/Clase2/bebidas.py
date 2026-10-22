# Python · bebida.py
opcion = input("1 o 2: ")
match opcion:
    case "1":
        print("Café")
    case "2":
        print("Té")
    case _:
        print("Opción inválida")