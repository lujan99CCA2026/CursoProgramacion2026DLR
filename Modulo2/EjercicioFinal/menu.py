from productos import Producto, Perecible

for inventario import Invetario

inv = Invetario()
inv.agregar(Producto("Arroz", 8, 20))
inv.agregar(Perecible("Leche", 6, 10, 2))
inv.agregar(Perecible("QUeso", 25, 4, 10))


opcion = ""

while opcion != "0":
    print()
    print("Esta es mi mini TIenda")
    print("1.ver 2. vender 3.valor 0.salir")
    opcion = input("Opcion: ")

    if opcion =="1":
        inv.mostrar()
    elif opcion == "2":
        produc = input("Ingrese el producto que quiere comprar")
        p = inv.buscar(produc)
        if p == None:
            print("ese producto no existe")
        else:
            n = int(input("Cuanto quiere comprar"))
            venta = p.vender(n)
            if venta == True:
                print("Vendido")
            else:
                print("No se vendio")
    elif opcion =="3":
        print(inv.valor_total())
    elif opcion == "0":
        print("hasta luego")
    else:
        print("Opcion no valida")




