# set significa grupo o conjunto
# es una estructura de datos que representa una colección no ordenada de elementos únicos

primer = {1, 1, 2, 2, 3, 4}
print(primer)

# primer.add(5)
# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)
print(segundo)

# | (unión): Crea un nuevo set con todos los elementos que se encuentran en cualquiera de los sets que se están combinando
print(primer | segundo)  # {1,2,3,4,5}

# & (intersección): Crea un nuevo set con los elementos que se encuentran en ambos sets que se están combinando
print(primer & segundo)  # {3,4}

# - (diferencia): Crea un nuevo set con los elementos que se encuentran en el primer set pero no en el segundo.
print(primer - segundo)  # {1,2}

# ^ (diferencia simétrica): Crea un nuevo set con los elementos que se encuentran en los sets, pero NO los elementos en común.
print(primer ^ segundo)  # {1,2,5}
