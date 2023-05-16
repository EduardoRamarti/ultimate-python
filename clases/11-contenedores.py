# meter objetos dentro de otros objetos

class Producto:  # creamos clase de producto
    # definimos el constructo
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # el método __str__ te permite definir cómo quieres que se vea un objeto cuando lo conviertes en una cadena de texto, lo que facilita la lectura y depuración del código.
    def __str__(self):
        return f"Producto: {self.nombre} - precio {self.precio}"


class Categoria:  # generamos la clase contenedora
    productos = []  # creamos la lista (vacia) donde se guardaran los productos

    # creamos el constructor que recibira el nombre de la categoria y el producto
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    # este metodo agregar sirve para añadir más productos a la lista
    def agregar(self, producto):
        self.productos.append(producto)

    # este metodo imprime los productos que existan dentro de la lista de productos
    def imprimir(self):
        for producto in self.productos:
            # cuando llamo a imprimir mi objeto, estoy llamando al metodo str el cual regresa el string definido en ese metodo
            print(producto)


kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("surfboard", 750)
deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.agregar(surfboard)
deportes.imprimir()
