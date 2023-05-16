class Animal:
    def comer(self):
        print("comiendo")


class Perro:
    def pasear(self):
        print("paseando")


# Aca en la herencia multiple, se hereda de derechaa izquierda.
# Es decir, se hereda todo de animal y si se repite un metodo en la siguiente herencia (perro), lo remplaza por este ultimo

class Chanchito(Perro, Animal):
    def programar(self):
        print("programando")


chanchito = Chanchito()
chanchito.comer()
chanchito.pasear()


class Caminardor:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Pato(Volador, Nadador, Caminardor):
    def programar(self):
        print("programando")
