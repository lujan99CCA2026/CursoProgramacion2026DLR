alumno = {
    "nombre": "Ana Garcia",
    "edad": 19,
    "nota": 85
}
print(alumno["nombre"])  # Ana
# cambiar valores
print(alumno["nota"])
alumno["nota"] = 100

print(alumno["nota"])

# Agregar valores
alumno["ciudad"] = "sucre"
print( alumno)
# Eliminar

del alumno["edad"]
print(alumno)