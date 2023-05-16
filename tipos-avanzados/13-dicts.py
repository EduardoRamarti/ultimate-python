punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45  # agregando otro punto

# print(punto, punto["lala"])
if "lala" in punto:
    print("encontre lala", punto["lala"])

# El método get() en los diccionarios de Python se utiliza para obtener el valor asociado con una clave en un diccionario. Si la clave no existe en el diccionario, el método devuelve un valor predeterminado en lugar de generar un error.

print(punto.get("x"))
print(punto.get("lala", 97))
# En el anterior busca traer el valor de lala, pero como no existe entonces regresa el valor 97 por default

# Borrar elementos del dict
del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])
# z 45
# x 25


for valor in punto.items():
    print(valor)
# ('z', 45)
# ('x', 25)


for llave, valor in punto.items():
    print(llave, valor)
# z 45
# x 25

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"}
]

for usuario in usuarios:
    print(usuario["nombre"])
