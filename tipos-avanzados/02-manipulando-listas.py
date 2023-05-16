mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])  # seleccionar un item de la lista (aqui es el primero)

# modificar una lista
mascotas[0] = "Bicho"  # modificar el indice 0
print(mascotas)

print(mascotas[2:])  # recorrer la lista desde el indice 2

print(mascotas[-1])  # imprime el ultimo item de la lista

# muestra solo los items que tengan indices multiplos de 2
print(mascotas[::2])

# muestra solo los items que tengan indices multiplos de 2, empezando por el indice 1
print(mascotas[1::2])


numeros = list(range(21))
print(numeros[::2])
print(numeros[1::2])
