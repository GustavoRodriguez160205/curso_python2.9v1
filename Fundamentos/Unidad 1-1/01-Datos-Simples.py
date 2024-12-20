#######################################################
# TIPOS DE DATOS EN PYTHON
#######################################################

# Python tiene varios tipos de datos que se usan para diferentes propósitos. 
# A continuación, se presentan los más comunes, junto con ejemplos prácticos.

#######################################################

# 01. Cadenas de texto (String)

#######################################################

# Las cadenas de texto se utilizan para representar información textual.
# Se pueden definir con comillas simples (' '), dobles (" ") o triples (''' ''' o """ """).
cadena1 = "Hola, mundo"  # Comillas dobles
cadena2 = 'Python es divertido'  # Comillas simples
cadena_multilinea = """
Tus datos:
  Nombre: Lionel
  Apellido: Messi
"""  # Comillas triples para texto multilínea

print(cadena1)
print(cadena2)
print(cadena_multilinea)

#######################################################

# 02. Números

#######################################################

# Python soporta varios tipos de números:
# a) Enteros (int): Representan números sin parte decimal.
# b) Decimales (float): Representan números con parte decimal.
# c) Complejos (complex): Representan números en forma de 'a + bj', donde 'a' y 'b' son números reales.

# Enteros
entero = 12
print(f"Entero: {entero}")

# Decimales
decimal = 12.3
print(f"Decimal: {decimal}")

# Números complejos
numero_complejo = 3 + 5j
print(f"Número complejo: {numero_complejo}")

#######################################################

# 03. Valores Booleanos (bool)

#######################################################

# Los valores booleanos representan estados lógicos: verdadero (True) o falso (False).
# Son útiles para estructuras de control como condicionales y bucles.
verdadero = True  # Representa "verdadero"
falso = False  # Representa "falso"

print(f"Valor booleano verdadero: {verdadero}")
print(f"Valor booleano falso: {falso}")

# Ejemplo práctico
edad = 18
es_mayor_de_edad = edad >= 18
print(f"¿Es mayor de edad? {es_mayor_de_edad}")

#######################################################

# Resumen de otros tipos de datos importantes

#######################################################

# 04. Listas: Colección ordenada y mutable.
lista = [1, 2, 3, 4, 5]
print(f"Lista: {lista}")

# 05. Tuplas: Colección ordenada e inmutable.
tupla = (10, 20, 30)
print(f"Tupla: {tupla}")

# 06. Conjuntos (Set): Colección desordenada y sin elementos duplicados.
conjunto = {1, 2, 2, 3}
print(f"Conjunto (sin duplicados): {conjunto}")

# 07. Diccionarios: Colección de pares clave-valor.
diccionario = {"nombre": "Lionel", "apellido": "Messi", "edad": 36}
print(f"Diccionario: {diccionario}")
