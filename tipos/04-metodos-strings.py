animal = "chanchito feliz"

print(animal.upper())  # convertir el string en mayusculas todas

print(animal.lower())  # convertir el string en minusculas todas

print(animal.capitalize())  # hacer mayuscula la SOLO primera letra del string

print(animal.title())  # haciendo la primera letra de cada palabra a mayusculas

# remueve los espacios en blanco que se encuentren a la derecha o izquierda del string
print(animal.strip())

# hacinedo uso de dos metodos al mismo tiempo, primero realiza el strip y luego el capitalize
print(animal.strip().capitalize())

# quitar los espacios en blanco que esten a la izquierda del string
print(animal.lstrip())
# quitar los espacios en blanco que esten a la derecha del string
print(animal.rstrip())

# busca un string dentro de otro string, devolviendo un numero entero (el indiice) o un numero negativo (el cual significa que no lo encontro)
print(animal.find("ch"))

# para cambiar un string por otro dentro del string principal (o el string entero)
print(animal.replace("nch", "j"))

# busca y nos devuelve un boleano si es que esta dentro del string
print("nch" in animal)

# busca si NO se encuentra dentro del string devolviendo un booleano
print("nch" not in animal)
