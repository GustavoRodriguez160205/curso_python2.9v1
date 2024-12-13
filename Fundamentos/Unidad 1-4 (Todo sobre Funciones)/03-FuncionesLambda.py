###########################################################
# Funciones Lambda en Python (Funciones Anónimas)
###########################################################

# Las funciones lambda son funciones anónimas (sin nombre) que se 
## definen en una sola línea. Se utilizan para tareas simples y suelen 
## ser útiles como argumentos para funciones como filter(), map(), o reduce().

# Lista de números para los ejemplos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

###########################################################

# 1. Función Lambda simple

# Esta función lambda toma un valor x y lo multiplica por 2.
multiplicar_por_dos = lambda x: x * 2

# Prueba de la función lambda
print("Multiplicar por dos:", multiplicar_por_dos(5))  # Salida: 10

###########################################################

# 2. Función común para verificar si un número es impar

# Definimos una función tradicional que devuelve True si el número es impar.
def es_impar(num):
    return num % 2 == 1

# Prueba de la función
print("¿Es 5 impar?", es_impar(5))  # Salida: True
print("¿Es 4 impar?", es_impar(4))  # Salida: False


###########################################################

# 3. Usando filter() con una función común

# La función filter() filtra elementos de una lista usando una función que
# devuelve True o False para cada elemento.
numeros_impares = filter(es_impar, numeros)

# Convertimos el resultado a una lista y lo imprimimos
print("Números impares (función común):", list(numeros_impares))


###########################################################


# 4. Usando filter() con una función lambda

# Aquí hacemos lo mismo que en el ejemplo anterior, pero usamos una
# función lambda en lugar de una función común.
numeros_pares = filter(lambda numero: numero % 2 == 0, numeros)

# Convertimos el resultado a una lista y lo imprimimos
print("Números pares (función lambda):", list(numeros_pares))

