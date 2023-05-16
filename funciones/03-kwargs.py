def get_product(**datos):  # cuando trabajamos con los kwargs se usan los **
    print(datos["id"], datos["name"])


# Cada que utilizo una funcion que utiliza kwargs, debemos de nombrar los argumentos
get_product(id="id",
            name="iPhone",
            desc="Designed in CAlifornia")
