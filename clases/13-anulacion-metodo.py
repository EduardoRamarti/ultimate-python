class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela ave")


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = True

    def vuevla(self):
        print("vuela pato")
        # super nos entrega acceso inmediato a los metodos y proiedades que tiene la clase padre
        super().vuela()


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
