"""Ejercicio de calculadora"""

print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, multi, div y resta")

num1 = int(input("Ingresa número: "))
while True:
    ope = input("Ingresa operacion: ").lower()
    if ope == "suma":
        num2 = int(input("Ingresa el siguiente numero: "))
        print(f"El resultado es: {num1 + num2}")
    elif ope == "resta":
        num2 = int(input("Ingresa el siguiente numero: "))
        print(f"El resultado es: {num1 - num2}")
    elif ope == "multi":
        num2 = int(input("Ingresa el siguiente numero: "))
        print(f"El resultado es: {num1 * num2}")
    elif ope == "div":
        num2 = int(input("Ingresa el siguiente numero: "))
        print(f"El resultado es: {num1 / num2}")
    else:
        break
