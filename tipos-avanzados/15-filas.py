from collections import deque

fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)

print(fila)


# Elimina el elemento de la izquierda (es decir, el primer elemento que se agregó a la fila).
fila.popleft()

if not fila:
    print("fila vacia")
