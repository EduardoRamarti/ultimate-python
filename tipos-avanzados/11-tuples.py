# Una tuple es una estructura de datos que permite almacenar una secuencia de valores, de manera similar a una lista. La principal diferencia es que las tuplas son inmutables
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)

# se pueden utilizar los mismos metodos de las listas en las tuplas.
# los unicos que no se pueden utilizar es un append y pop, ya que las tuplas no se modifican
