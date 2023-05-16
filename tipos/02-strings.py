nombre_curso = "Ultimate Python"  # string de una sola linea
description_course = """ 
Utimate Python,
este curso contempla todo
lo que necesitas para conseguir 
un trabajo como programador
"""  # asi se crea un string de varias lineas

print(nombre_curso, description_course)

len(nombre_curso)  # contar la cantidad de caracteres dentro de esta variable

# accediendo al primer caracter del string de esta variable
print(nombre_curso[0])
# recorriendo el string desde el inicio hasta el caracter 8 del string
print(nombre_curso[0:8])
# recorriendo el string desde el caracter en la 9na posicion hasta el ultimo
print(nombre_curso[9:])
# recorriendo el string desde el primer caracter hasta el caracter en la posicion 8
print(nombre_curso[:8])
# recorriendo el string desde su caracter inicial hasta el final
print(nombre_curso[:])
