# Esta es una convencion para escribir este tipo de listas conocida como multi-line statement
mascotas = [
    "Wolfgang",
    "Pelusa",
    "Felipe",
    "Pulga",
    "Chanchito feliz"
]

# AGREGA el argumento que le pasas en el indice que le indicas (recorriendo el resto)
mascotas.insert(1, "Melvin")
# Agrega otro elemento a la lista, pero lo coloca AL FINAL
mascotas.append("Chanchito triste")

# Este método se utiliza para eliminar un elemento de una lista utilizando su valor. Toma un argumento, que es el valor del elemento que se eliminará
mascotas.remove("Pulga")
# Este método se utiliza para eliminar un elemento de una lista utilizando su índice. Si se llama sin argumentos, elimina el último elemento de la lista.
mascotas.pop()
mascotas.pop(1)
# La palabra clave del se utiliza para eliminar un elemento de una lista utilizando su índice. En este caso, se está eliminando el primer elemento de la lista.
del mascotas[0]
# Este método se utiliza para eliminar todos los elementos de una lista, dejándola vacía. No toma argumentos.
mascotas.clear()

print(mascotas)
