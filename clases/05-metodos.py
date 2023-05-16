class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        # self se refiere a la instancia actual en la que se encuentra
        self.nombre = nombre
        self.edad = edad

# @classmethod se utiliza para definir métodos especiales en una clase que están relacionados con la clase en general y no con objetos individuales. Estos métodos pueden realizar acciones que se aplican a toda la clase y pueden ser llamados directamente desde la clase sin tener que crear objetos específicos.
    @classmethod
    def habla(cls):
        # cls hace referencia a la clase (en este caso cls = Perro)
        print("Guau!")

    @classmethod
    # este es un factory method en el cual se esta encapsulando la creacion de nuevos objetos. En general es un patron de diseño c¡en el cual se tiene un comportamiento similar al constructor
    def factory(cls):
        return cls("Broom", 4)


Perro.habla()

perro1 = Perro("Brook", 1)
perro2 = Perro("Black", 2)
perro3 = Perro.factory()

print(perro3.edad, perro3.nombre)
