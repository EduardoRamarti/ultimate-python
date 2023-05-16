class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        # es una convencion utilizar __ (doble guion bajo) para volver privado a un atributo o un metodo
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Broom", 4)


perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())

# es un diccionario que tiene dentro el nombre de los atributos y sus valores
print(perro1.__dict__)

# de esta  manera estamos accediendo al valor del atributo privdado
# print(perro1._Perro__nombre)
