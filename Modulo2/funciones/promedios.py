def pedir_nota(): return float(input("Nota: "))


def promedio(a, b, c):
    return (a + b + c) / 3
def mostrar(p):
    print("Promedio:", round(p, 2))
    if p >= 61: print("Aprobado")


n1 = pedir_nota()
n2 = pedir_nota()
n3 = pedir_nota()
p = promedio(n1, n2, n3)
mostrar(p)