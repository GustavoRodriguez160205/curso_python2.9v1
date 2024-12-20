# FUNCIONES INTEGRADAS EN PYTHON
# Python incluye una gran cantidad de funciones integradas que puedes utilizar sin necesidad de importar módulos adicionales.
# Estas funciones simplifican tareas comunes y hacen que el código sea más eficiente y fácil de escribir.

#######################################################
# Ejemplo 1: Usando `max` para encontrar el número más alto en una lista
#######################################################

numeros = [4, 7, 1, 42, 15]

# La función `max` retorna el valor más grande de un iterable, como una lista
numero_mayor = max(numeros)
print(f"El número más alto de la lista {numeros} es: {numero_mayor}")  # Imprime: El número más alto de la lista [4, 7, 1, 42, 15] es: 42

#######################################################
# Ejemplo 2: Usando `min` para encontrar el número más bajo en una lista
#######################################################

# La función `min` retorna el valor más pequeño de un iterable
numero_menor = min(numeros)
print(f"El número más bajo de la lista {numeros} es: {numero_menor}")  # Imprime: El número más bajo de la lista [4, 7, 1, 42, 15] es: 1

#######################################################
# Ejemplo 3: Redondear números con `round`
#######################################################

numero = 12.345678

# Redondear un número a una cantidad específica de decimales
numero_redondeado = round(numero, 6)  # Redondea a 6 decimales
print(f"El número {numero} redondeado a 6 decimales es: {numero_redondeado}")  # Imprime: El número 12.345678 redondeado a 6 decimales es: 12.345678

# Redondear a 2 decimales de forma manual
numero_redondeado_2_decimales = round(numero * 100) / 100  # Redondea a 2 decimales
print(f"El número {numero} redondeado manualmente a 2 decimales es: {numero_redondeado_2_decimales}")  # Imprime: El número 12.345678 redondeado manualmente a 2 decimales es: 12.35

#######################################################
# Ejemplo 4: Usando `bool` para evaluar valores como True o False
#######################################################

# La función `bool` convierte un valor en su equivalente booleano (True o False).
# Algunos valores que son equivalentes a False: 0, cadenas vacías (""), listas vacías ([]), None, etc.
# Otros valores se consideran equivalentes a True: números diferentes de 0, cadenas no vacías, listas con elementos, etc.

# Evaluar el valor 0, que equivale a False
resultado = bool(0)
print(f"Evaluar 0 con `bool` da como resultado: {resultado}")  # Imprime: Evaluar 0 con `bool` da como resultado: False

# Evaluar un número distinto de 0, que equivale a True
resultado = bool(42)
print(f"Evaluar 42 con `bool` da como resultado: {resultado}")  # Imprime: Evaluar 42 con `bool` da como resultado: True

# Evaluar una cadena vacía, que equivale a False
resultado = bool("")
print(f"Evaluar una cadena vacía con `bool` da como resultado: {resultado}")  # Imprime: Evaluar una cadena vacía con `bool` da como resultado: False

# Evaluar una lista no vacía, que equivale a True
resultado = bool([1, 2, 3])
print(f"Evaluar una lista no vacía con `bool` da como resultado: {resultado}")  # Imprime: Evaluar una lista no vacía con `bool` da como resultado: True

#######################################################
# Ejemplo 5: Usando `all` para evaluar todos los elementos de un iterable
#######################################################

# La función `all` retorna True si **todos** los elementos de un iterable son verdaderos (equivalentes a `True`).
# Retorna False si al menos un elemento equivale a `False`.

# Lista con todos los elementos "verdaderos"
resultado_all = all([123, "True", "False"])  # Todos los elementos son no vacíos, así que son True
print(f"Evaluar una lista con `all([123, 'True', 'False'])` da como resultado: {resultado_all}")  # Imprime: Evaluar una lista con `all([123, 'True', 'False'])` da como resultado: True

# Lista con un elemento falso (cadena vacía "")
resultado_all = all([123, "", "False"])  # La cadena vacía ("") equivale a False
print(f"Evaluar una lista con `all([123, '', 'False'])` da como resultado: {resultado_all}")  # Imprime: Evaluar una lista con `all([123, '', 'False'])` da como resultado: False

#######################################################
# Ejemplo 6: Usando `sum` para sumar todos los valores de un iterable
#######################################################

# La función `sum` suma todos los valores de un iterable, como una lista de números.

numero = [12, 44, 11, 55, 44, 33, 22, 11]

# Sumar los elementos de la lista
suma = sum(numero)
print(f"La suma total con `sum` es: {suma}")  # Imprime: La suma total con `sum` es: 232
