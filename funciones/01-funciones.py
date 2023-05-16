def hola():  # creando la funcion
    print("Hola Mundo!")
    print("Ultimate Python")


hola()  # ejecutando la funcion


def hola_nom(nombre):  # agregando parametro
    print("Hola Mundo!")
    print(f"Bienvenido {nombre}")


hola_nom("Eduardo")  # agregando argumento


def holas(nombre, apellido="Feliz"):  # agregando parametro opcional
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")


holas("Eduardo")  # agregando solo un argumento


# Argumentos nombrados
holas(apellido="Ramirez", nombre="Eduardo")
# basicamente es establecer que argumento le estas dando a un parametro en especifico
