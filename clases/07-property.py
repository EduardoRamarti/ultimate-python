class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property  # con este decorador estamos indicando que lo convierta en una propiedad el metodo siguiente. En pocas palabras es un getter que se convierte en propiedad
    def nombre(self):
        return self.__nombre

    # Este es un decorador que indica que el método siguiente es el setter para el atributo nombre. El nombre del método debe coincidir con el nombre del atributo al que se refiere.
    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre
        return  # Esta línea es opcional en un método setter. En este caso, no hace nada, ya que el objetivo principal del setter es asignar el valor al atributo y no necesariamente devolver algo.


perro = Perro("Choclo")
print(perro.nombre)
