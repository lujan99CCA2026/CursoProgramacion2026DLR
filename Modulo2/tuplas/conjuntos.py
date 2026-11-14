# Esto es un conjunto porque trabaja con {}
colores = {"rojo", "azul", "rojo"}
print(colores)      # {'rojo', 'azul'}
 
colores.add("verde")
colores.add("verde")
colores.add("verde")

print(colores)  

print(len(colores)) # 3

print("rojo" in colores) # True
