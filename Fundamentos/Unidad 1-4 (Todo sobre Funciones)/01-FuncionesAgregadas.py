# Introducción a funciones integradas en Python
# Python incluye muchas funciones integradas (built-in) que puedes usar sin necesidad de importar módulos adicionales.
# Estas funciones facilitan tareas comunes como buscar valores máximos/mínimos, redondear números, evaluar condiciones lógicas, y más.

#######################################################
# Ejemplo 1: Usando `max` para encontrar el número más alto en una lista

numeros = [4, 7, 1, 42, 15]

# La función `max` retorna el elemento más grande de un iterable (como una lista)
numero_mayor = max(numeros)
print(f"El número más alto de la lista {numeros} es: {numero_mayor}")

#######################################################
# Ejemplo 2: Usando `min` para encontrar el número más bajo en una lista

# La función `min` retorna el elemento más pequeño de un iterable
numero_menor = min(numeros)
print(f"El número más bajo de la lista {numeros} es: {numero_menor}")

#######################################################
# Ejemplo 3: Redondear números con `round`

# Redondeo a un número específico de decimales
numero = 12.345678

# Redondear a 6 decimales
numero_redondeado = round(numero, 6)  # El segundo argumento indica la cantidad de decimales
print(f"El número {numero} redondeado a 6 decimales es: {numero_redondeado}")

# Otra forma: Redondear al entero más cercano
# Multiplicamos y luego dividimos para simular un redondeo a 2 decimales manualmente
numero_redondeado_2_decimales = round(numero * 100) / 100
print(f"El número {numero} redondeado manualmente a 2 decimales es: {numero_redondeado_2_decimales}")

#######################################################
# Ejemplo 4: Usando `bool` para evaluar valores como True o False

# La función `bool` convierte un valor a su equivalencia lógica:
# - `False` para: 0, cadenas vacías (""), listas vacías ([]), None, etc.
# - `True` para: números distintos de 0, cadenas no vacías, listas con elementos, etc.

# Ejemplo 4.1: Evaluar un número igual a 0
resultado = bool(0)
print(f"Evaluar 0 con `bool` da como resultado: {resultado}")  # False

# Ejemplo 4.2: Evaluar un número distinto de 0
resultado = bool(42)
print(f"Evaluar 42 con `bool` da como resultado: {resultado}")  # True

# Ejemplo 4.3: Evaluar una cadena vacía
resultado = bool("")
print(f"Evaluar una cadena vacía con `bool` da como resultado: {resultado}")  # False

# Ejemplo 4.4: Evaluar una lista no vacía
resultado = bool([1, 2, 3])
print(f"Evaluar una lista no vacía con `bool` da como resultado: {resultado}")  # True

#######################################################
# Ejemplo 5: Usando `all` para evaluar todos los elementos de un iterable

# La función `all` retorna True si **todos** los elementos de un iterable son verdaderos (equivalen a `True`).
# Retorna False si al menos un elemento equivale a `False`.

# Ejemplo con una lista donde todos los elementos son "verdaderos"
resultado_all = all([123, "True", "False"])  # Todos los elementos son no vacíos, así que son True
print(f"Evaluar una lista con `all([123, 'True', 'False'])` da como resultado: {resultado_all}")  # True

# Ejemplo con una lista que contiene al menos un elemento falso
resultado_all = all([123, "", "False"])  # La cadena vacía ("") equivale a False
print(f"Evaluar una lista con `all([123, '', 'False'])` da como resultado: {resultado_all}")  # False

################################################################

# Ejemplo 6: Usando 'Sum' Suma todos los valores de un iterable

numero = [12 , 44 , 11 , 55 , 44 , 33 , 22 , 11]

suma = sum(numero)
print(f"La suma total con sum es: {suma}")