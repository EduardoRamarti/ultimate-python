mascotas = ["Pelusa", "Wolfgang", "Pulga",
            "Felipe", "Wolfgang", "Chanchito feliz"]

print(mascotas.count("Wolfgang"))  # Cuantas veces esta "Wolfgang" en la lista
# 2


if "Wolfgang" in mascotas:  # si "Wolfgang" esta en mascotas
    print(mascotas.index("Wolfgang"))  # imprime su indice
    # pero solamente imprime el indice de la primera coincidencia
