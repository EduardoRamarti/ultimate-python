class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):  # para eliminar objetos
        print(f"Chao perro {self.nombre}")

    def __str__(self):
        return f"Class Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Broom", 2)
print(perro)
del perro
