numeros = [1, 2, 3]

# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# La segunda línea del código es una lista llamada numeros que contiene los valores del 1 al 9. La siguiente línea utiliza la sintaxis de desempaquetado de secuencias para asignar la variable primero al primer elemento de la lista (1 en este caso), la variable ultimo al último elemento de la lista (9) y la variable otros a todos los elementos restantes de la lista (los valores 2 a 8 en este caso).

# El operador * antes de la variable otros en la asignación de desempaquetado indica que todos los valores restantes después de la asignación de primero y ultimo deben asignarse a la variable otros.
# * hace referencia a asignar un determinado valor o valores a una variable
primero, *otros, ultimo = numeros
print(primero, ultimo, otros)
