####################################################

# Incremento del contador
contador = 0  # Variable que se va a ir incrementando

# Se ejecutará mientras el contador sea menor que 10
while contador < 10:
    contador += 1  # Incrementamos el contador en 1
    print(contador)

print("El bucle 'while' ha terminado")
####################################################

# Ejercicio: Cuenta regresiva

contador = 10

while contador > 0:  # Cambié >= 10 a > 0 para corregir la lógica
    contador -= 1
    print(contador)

print("¡Despegue!")

####################################################

# Suma de números del 1 al 50
suma = 0  # Acumulador
numero = 1  # Comenzamos desde 1

while numero <= 50:
    suma += numero  # Sumamos el número actual
    numero += 1  # Pasamos al siguiente número

print("La suma de los números del 1 al 50 es:", suma)

####################################################

# Pedir contraseña
contraseña = ""

while contraseña != '1234':  # Se ejecutará hasta que la contraseña sea '1234'
    contraseña = input("Ingresa la contraseña: ")

print("Acceso concedido")

####################################################

# Números pares
numero = 0

while numero <= 20:  # Se ejecutará mientras el número sea menor o igual a 20
    print(f"Los números pares son: {numero}")
    numero += 2  # Incrementamos en 2

####################################################

# Suma hasta que sea suficiente
suma_total = 0
numero = 0

while numero >= 0:  # Se ejecutará hasta que se ingrese un número negativo
    numero = int(input("Ingresa un número (negativo para salir): "))
    if numero >= 0:  # Si el número es positivo, lo sumamos
        suma_total += numero

print("La suma total de los números positivos es:", suma_total)


####################################################

# Contar la letra "a"
texto = input("Ingresa una cadena de texto: ")

contador = 0  # Índice para recorrer el texto
cantidad_a = 0  # Contador de la letra 'a'

while contador < len(texto):
    if texto[contador].lower() == "a":  # Comprobamos el carácter actual
        cantidad_a += 1
    contador += 1

print(f"La letra 'a' aparece {cantidad_a} veces en la cadena.")
####################################################

# Contador en reversa
numero = int(input("Ingresa un número para contar hacia atrás: "))

while numero >= 1:
    print(numero)
    numero -= 1
####################################################

# Suma de los primeros números
n = int(input("Ingresa un número: "))
suma = 0
i = 1

while i <= n:
    suma += i  # Acumulamos el valor de i
    i += 1  # Incrementamos i

print("La suma de los primeros", n, "números es:", suma)
####################################################

# Contar dígitos de un número
numero = int(input("Ingresa un número: "))
contador = 0

while numero > 0:  # Ajusté para manejar números positivos únicamente
    numero = numero // 10
    contador += 1

print("El número tiene", contador, "dígitos.")
####################################################

# Generar secuencia de Fibonacci
n = int(input("Ingresa un número para generar la secuencia de Fibonacci: "))
a, b = 0, 1

while a <= n:
    print(a, end=" ")  # Imprimimos el número actual
    a, b = b, a + b  # Actualizamos los valores de a y b
