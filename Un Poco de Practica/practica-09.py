### Repaso General

## Suma y resta

num1 = int(input("Introduce el primer número:"))
num2 = int(input("Introduce el segundo número:"))

suma = num1 + num2
resta = num1 - num2

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")


## Multiplicación y Divición

num1 = int(input("Introduce el primer número:"))
num2 = int(input("Introduce el segundo número:"))

multiplicacion = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    print("No se puede dividir por cero")

print(f"La multiplicación es: {multiplicacion}")


## Potencia

base = float(input("Introduce la base:"))
exponente = float(input("Introduce el exponente:"))

potencia = base ** exponente

print(f"{base} elevado a la potencia {exponente} es: {potencia}")


## Promedio

num1 = float(input("Introduce el primer número:"))
num2 = float(input("Introduce el segundo número:"))
num3 = float(input("Introduce el tercer número:"))


promedio = (num1 + num2 + num3) / 3

print(f"El promedio es: {promedio}")


## Formúlas Matemáticas

import math

radio = float(input("Introduce el radio del círculo:"))
area = math.pi * radio ** 2
print(f"El area del círculo con radio {radio} es: {area}")


## Factorial

numero = int(input("Introduce un número para calcular su factorial:"))

if numero >= 0:
    factorial = math.factorial(numero)
    print(f"El factorial de {numero} es: {factorial}")

else:
    print("El factorial no está definido para números negativos.")


## Area de un Triángulo

base = float(input("Introduce la base del triángulo:"))
altura = float(input("Introduce la altura del triángulo:"))

area = base * altura / 2

print(f"El área del triángulo es: {area}")


## Calcular Perímetro de un Rectángulo

largo = float(input("Introduce el largo del rectángulo:"))
ancho = float(input("Introduce el ancho del rectángulo"))

perimetro = 2 * (largo + ancho)
print(f"el perímetro del rectángulo es: {perimetro}")

