numeros = [2, 4, 1, 45, 75, 22]

# El método .sort() es un método de lista que ordena la lista original en su lugar. Esto significa que la lista original se modifica directamente y se ordena de forma ascendente (por defecto) o de forma descendente (si se especifica el argumento reverse=True)
numeros.sort(reverse=True)

# La función sorted() es una función de Python que toma una secuencia (por ejemplo, una lista) como argumento y devuelve una nueva lista ordenada sin modificar la secuencia original. Por defecto, la función sorted() ordena la lista de forma ascendente, pero también se puede especificar el argumento reverse=True
numeros2 = sorted(numeros)

print(numeros)
print(numeros2)


usuarios = [
    [4, "Chanchito"],
    [1, "Felipe"],
    [5, "Pulga"]
]
usuarios.sort()
print(usuarios)


usuarios2 = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# esta funcion recibe una lista, y toma el elemento con el indice 1 de dicha lista, regresandolo


def ordena(elemento):
    return elemento[1]


# para ordenarlo, le decimos que el key (o indice con el que va a ordenar) sera lo que retorne ordena. Entonces la funcion de ordena realiza su proceso con las listas dentro de usuarios2
usuarios2.sort(key=ordena)
print(usuarios2)
