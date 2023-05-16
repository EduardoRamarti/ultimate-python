try:
    n1 = int(input("Ingresa primer número: "))
except Exception as e:  # manejar todas las excepciones, no importa el tipo
    print("Ocurrio un error")
else:
    print("No ocurrio ningun erro")
finally:
    print("se ejecuta siempre")  # al final
