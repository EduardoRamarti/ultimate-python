"""Ejercicio de Calculadora"""
n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un numero: "))

suma = n1+n2
resta = n1-n2
multi = n1*n2
divi = n1/n2

mensjae = f"""
Para los numeros {n1} y {n2}
el resultado de la suma es {suma},
el resultado de la resta es {resta},
el resultado de la multiplicacion es {multi},
el resultado de la division es {divi}.
"""

print(mensjae)
