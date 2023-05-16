# lambdas o tambien conocidos como funciones anonimas
usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]
# la syntax de lambda es: lambda arguments: expression
# aqui la lambda recibe como argumento la lista y retorna el item del indice 1 de la lista que esta analizando
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
