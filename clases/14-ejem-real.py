class Model():  # se crea la clase model
    tabla = False  # se establece como false la tabla

    def __init__(self):  # creamos el constructor
        if not self.tabla:  # si no existe la tabla
            print("Erro, tienes que definir una tabla")

    def guardar(self):  # se crea el metodo para guardar la bd
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod  # metodo dirigido a la clase
    def buscar_por_id(cls, _id):  # metodo para buscar por id
        print(f"Buscando por id {_id} en la tabla {cls.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()


usuario.guardar()
usuario.buscar_por_id(123)
