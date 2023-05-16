usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# La función map() es muy útil cuando se desea aplicar una función a cada elemento de una lista sin tener que escribir un bucle for para recorrer cada elemento y aplicar la operación manualmente.

# map syntax: map(function, list)
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# La función filter() es muy útil cuando se desea filtrar elementos de una secuencia según un criterio determinado sin tener que escribir un bucle for para recorrer cada elemento y aplicar la función manualmente.

# filter syntax: filter(function, list)
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
