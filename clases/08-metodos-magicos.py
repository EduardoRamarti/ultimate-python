class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chao perro {self.nombre}")

    def __str__(self):
        return f"Class Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Broom", 2)
print(perro)
del perro

"""
Un método mágico, también conocido como método especial o método dunder (del inglés "double underscore"), es un tipo especial de método en Python que sigue una convención de nomenclatura específica utilizando doble guion bajo (__) al principio y al final del nombre del método.

Estos métodos mágicos son implementados por clases y se utilizan para definir el comportamiento especial o personalizado de los objetos en contextos específicos. Estos métodos son invocados automáticamente por el intérprete de Python en respuesta a ciertos eventos o acciones, como operaciones aritméticas, acceso a atributos, creación de objetos, entre otros.

Algunos ejemplos comunes de métodos mágicos incluyen:

__init__: Este método mágico es utilizado para inicializar un objeto cuando se crea una nueva instancia de una clase.
__str__: Este método mágico se utiliza para devolver una representación legible como cadena de un objeto y se invoca al usar la función str(objeto).
__len__: Este método mágico se utiliza para devolver la longitud de un objeto y se invoca al usar la función len(objeto).
__getitem__ y __setitem__: Estos métodos mágicos se utilizan para acceder y asignar valores a elementos individuales de un objeto, y se invocan al utilizar la sintaxis de indexación, como objeto[indice].
Los métodos mágicos permiten que las clases personalicen su comportamiento y proporcionen una interfaz intuitiva para interactuar con los objetos. Al implementar estos métodos en una clase, se puede definir cómo se deben realizar las operaciones comunes en los objetos de esa clase, lo que mejora la flexibilidad y la usabilidad del código.

"""
