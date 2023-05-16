usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# La siguiente linea tambien es conocida como map
nombres = [usuarios[0] for usuarios in usuarios]
print(nombres)
# filtrar -> tambien conocido como filter
nombres2 = [usuario for usuario in usuarios if usuario[1] > 2]

# transformando lista
nombres3 = [usuario[0] for usuario in usuarios if usuario[1] > 2]
