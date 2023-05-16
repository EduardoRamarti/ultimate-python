# ¿Qué es un constructor?
# En Python, un constructor es como un conjunto de instrucciones especiales que se usan para construir objetos. Los objetos son como esos bloques de construcción que te permiten crear cosas más grandes y útiles.

# Cuando usas un constructor en Python, le estás diciendo al programa cómo construir un objeto específico. Es como si le estuvieras dando instrucciones al programa sobre cómo ensamblar todos los bloques para crear algo especial.

class Perro:
    def __init__(self, nombre, edad):
        # self se refiere a la instancia actual en la que se encuentra
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Brook", 10)
mi_perro2 = Perro("Feli", 6)
print(mi_perro.nombre)
print(mi_perro2.nombre)
