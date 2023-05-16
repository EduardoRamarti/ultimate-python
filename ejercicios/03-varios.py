# 1. Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes
import re
first = input("Ingresa una frase: ")
first_arg = list(first)
list_c = [c for c in first_arg if c != " "]
print(list_c)


# 2. Contar en un diccionario cuanto se repiten los caracteres de un string
patron = "[a-zA-Z]"
recorrer = re.findall(patron, first)
el_dict = {}
for l in recorrer:
    if l in el_dict:
        continue
    else:
        el_dict[l] = recorrer.count(l)

print(el_dict)


# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas [("a",3),("b",2),("c",4),("d",4)]
tuples_list = [tuple([k, i]) for k, i in el_dict.items()]
print(tuples_list)


# 4. De un listado de tuplas, devolver las tuplas que tengan el mayor valor
# [("a",3),("b",2),("c",4),("d",4)] -> [("c",4), ("d",4)]
tuples_list.sort(key=lambda tpl: tpl[1], reverse=True)
major_tuple = tuples_list[0]
print(major_tuple)

# 5. Crear un mensaje que diga:
# Los caracteres que mas se repiten con 4 repeticiones son:
# - C
# - D
top_tuples = list(filter(lambda tup: tup[1] >= tuples_list[0][1], tuples_list))
print(top_tuples)
print(
    f"""Los mensajes que más se repiten con {top_tuples[0][1]} repeticiones son:""")
for t in top_tuples:
    print(f"- {t[0]}")


# 6. Juntar la solucion de los ejercicios anteriores para encontrar los caracteres que más se repiten de un string
