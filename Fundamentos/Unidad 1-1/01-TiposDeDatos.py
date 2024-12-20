# TIPOS DE DATOS SIMPLES EN PYTHON
# Python tiene varios tipos de datos simples que se utilizan para almacenar valores básicos en un programa.

###################################################
# 01. Strings (Cadenas de texto)
###################################################

# Las cadenas de texto o strings se utilizan para representar texto.
# En Python, puedes definir strings con comillas simples, dobles o triples (para cadenas multilínea).

# Ejemplos:
string_1 = "Este es un string con comillas dobles"
string_2 = 'Este es un string con comillas simples'
string_multilinea = """
Tus datos:
  nombre: Lucas
  apellido: Dalto
"""  # Un string de varias líneas, útil para textos largos o formateados.

print(string_1)  # Imprime: Este es un string con comillas dobles
print(string_multilinea)  # Imprime el texto de varias líneas

###################################################
# 02. Números (enteros y flotantes)
###################################################

# Los números en Python pueden ser de dos tipos: enteros (int) y flotantes (float).

# Enteros (int) son números sin decimales:
numero_entero = 40

# Flotantes (float) son números con decimales:
numero_flotante = 4.4

print(f'Número entero: {numero_entero}')  # Imprime: Número entero: 40
print(f'Número flotante: {numero_flotante}')  # Imprime: Número flotante: 4.4

###################################################
# 03. Booleanos (True/False)
###################################################

# Los valores booleanos son un tipo de datos que representan dos estados posibles: True (verdadero) o False (falso).
# Son especialmente útiles en estructuras de control (condicionales) y en la lógica de los programas.

es_verdadero = True
es_falso = False

print(f'El valor es verdadero: {es_verdadero}')  # Imprime: El valor es verdadero: True
print(f'El valor es falso: {es_falso}')  # Imprime: El valor es falso: False

###################################################
# Resumen:
# - Strings: Cadenas de texto, se definen con comillas simples, dobles o triples.
# - Números: Enteros (int) y decimales (float).
# - Booleanos: True o False, utilizados en decisiones lógicas.
