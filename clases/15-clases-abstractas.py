"""Clases abstractas"""
# Importamos las clases ABC y abstractmethod del módulo abc. Estas clases nos permiten definir clases abstractas y métodos abstractos.
from abc import ABC, abstractmethod


class Model(ABC):  # Definimos una clase llamada Model que hereda de la clase abstracta ABC. Esto indica que Model es una clase abstracta y no se puede instanciar directamente.
    tabla = False

    # el contructor se ejecuta automáticamente cuando se crea una instancia de la clase.
    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    # El decorador @property convierte el método en una propiedad de solo lectura, y el decorador @abstractmethod indica que el método es abstracto y debe ser implementado por las clases derivadas.
    @property
    @abstractmethod
    def table(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    # @classmethod indicando que es un método de clase. Puede ser invocado en la clase misma, en lugar de una instancia de la clase.
    @classmethod
    def buscar_por_id(cls, _id):
        print(f"Buscando por id {_id} en la tabla {cls.tabla}")


class Usuario(Model):
    tabl = "Usuario"

    # Definimos el método guardar en la clase Usuario. Aunque es abstracto en la clase Model, ahora proporcionamos una implementación vacía para este método en la clase Usuario utilizando la declaración pass.
    def guardar(self):
        # Implementación del método guardar para la clase Usuario
        pass


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(123)
