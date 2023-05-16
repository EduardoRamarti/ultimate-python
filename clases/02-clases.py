class Perro:  # usar el UpperCamelCase
    def habla(self):
        print("Guau!")


# instanciar la clase o crear objeto
mi_perro = Perro()
# print(type(mi_perro)) devuleve class

mi_perro.habla()

# saber si mi objeto es una instancia de una clase
print(isinstance(mi_perro, Perro))  # Devuelve True
