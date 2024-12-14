## Practica de Funciones

# 1. Número al cuadrado
def al_cuadrado(num):
    return num ** 2

numero = int(input("Ingresa un número por favor para elevarlo al cuadrado: "))
resultado = al_cuadrado(numero)
print(f"El número {numero} elevado al cuadrado es: {resultado}")


# 2. Saludo personalizado

def saludo(nombre, apellido):
    return f"Hola {nombre} {apellido}, ¿cómo estás?"

resultado = saludo("Juan", "Manuel")
print(resultado)


# 3. Suma de dos números

def suma(a,b):
    resultado = a + b
    return resultado

resultado = suma(3 , 5)
print(f"La suma es: {resultado}")


# 4. Multiplicar 3 números

def multiplicar(a, b, c):
    resultado = a * b * c
    return resultado  

resultado = multiplicar(2, 3, 4)
print("El resultado de la multiplicación es:", resultado) 



# 5. Conversión de grados Celcius a Fahrenheit

def convertir(celcius):

    fahrenheit = (celcius * 9/5 )+ 32
    return fahrenheit

resultado = convertir(25)
print(f"25 grados a Celcius son {resultado} grados Fahrenheit")


####################################################


## Ejercicios de Funciones Anonimas

# 3. Elevar un número al cuadrado con función lambda
elevar_cuadrado = lambda x: x ** 2
print(f"El número elevado al cuadrado con funciones lambda es: {elevar_cuadrado(5)}")



# 4. Suma de dos números
sumar = lambda a, b: a + b
print(sumar(3, 5))


# 5. Número par o impar
es_par = lambda x: x % 2 == 0
print(es_par(4))  # Debería devolver True
print(es_par(5))  # Debería devolver False


# 6. Calcular la longitud de la cadena
longitud = lambda s: len(s)
print(longitud("Hola"))  # Debería devolver 4


# 7. Filtrar números pares
numeros = [1, 2, 4, 5, 6, 7, 8]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Debería imprimir [2, 4, 6, 8]


# 8. Producto de 3 números
producto = lambda a, b, c: a * b * c
print(producto(2, 3, 4))  # Debería devolver 24


# 9. Texto a mayúsculas
a_mayusculas = lambda s: s.upper()
print(a_mayusculas("hola mundo"))  # Debería devolver "HOLA MUNDO"


# 10. Filtrar mayores de edad
edad = [10, 20, 17, 18, 25, 30]
mayores = list(filter(lambda x: x >= 18, edad))
print(f"Las personas mayores de edad son: {mayores}")  # Debería devolver [20, 18, 25, 30]


# 11. Calcular el área de un rectángulo
area_rect = lambda ancho, alto: ancho * alto
print(area_rect(5, 4))  # Debería devolver 20
print(area_rect(10, 5))  # Debería devolver 50


# 12. Calcular el resto de un número
modulo = lambda dividiendo, divisor: dividiendo % divisor
print(modulo(10, 4))  # Debería devolver 2
print(modulo(15, 4))  # Debería devolver 3


# 13. Filtrar cadenas con más de N caracteres
cadenas = ["Hola", "Python", "Lambda", "Ejercicio", "Corto"]
n = 5
largas = list(filter(lambda s: len(s) > n, cadenas))
print(largas)  # Debería devolver ['Python', 'Lambda', 'Ejercicio']


# 14. Ordenar números de mayor a menor
numeros = [5, 2, 9, 1, 7, 3]
ordenados = sorted(numeros, key=lambda x: -x)  # Es una forma de invertir el orden
print(ordenados)  # Debería devolver [9, 7, 5, 3, 2, 1]

############################################################