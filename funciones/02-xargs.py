# Usango xargs, cuando pasamos un numero no exacto de parametros
# para eso usamos el * seguido del nombre del parametro
def suma(*numeros):
    # el parametro se vuevle un iterable por la cantidad de argumentos que podemos pasarle
    # por eso es que hacemos uso de for (para recorrer ese iterable)
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 5, 7, 54, 32)
