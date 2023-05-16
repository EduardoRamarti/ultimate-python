mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]

for mascota in mascotas:
    print(mascota)
    # pelusa
    # pulga
    # felipe

for mascota in enumerate(mascotas):
    print(mascota)
    # (0, 'pelusa')
    # (1, 'pulga')
    # (2, 'felipe')


for mascota in enumerate(mascotas):
    print(mascota[0])
    # 0
    # 1
    # 2


for mascota in enumerate(mascotas):
    print(mascota[1])
    # pelusa
    # pulga
    # felipe

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
    # 1 pelusa
    # 2 pulga
    # 3 felipe
