# Importamos el módulo re para trabajar con expresiones regulares
import re

# Definimos un texto de ejemplo
texto = """ Hola maestro, esta es la cadena 1, como estas mi capitan 
Esta es la linea 2 de texto
Y Esta es la final (linea 3) definitiva mi capitan"""

# 01. **re.search()**: Busca la primera coincidencia del patrón en el texto

# Buscamos la primera ocurrencia de la palabra "Hola"
# Devuelve un objeto match con información sobre la coincidencia
resultado = re.search("Hola", texto)
print("Resultado de re.search():", resultado)

# Si hay coincidencia, devuelve el objeto match, sino devuelve None
# En este caso, "Hola" está al inicio del texto, por lo que se encuentra.

########################################

# 02. **re.findall()**: Busca todas las ocurrencias del patrón en el texto y las devuelve en una lista

# Buscamos todas las veces que aparece "esta" en el texto
# Ignorando mayúsculas/minúsculas con re.IGNORECASE
resultado = re.findall("esta", texto, re.IGNORECASE)
print("Resultado de re.findall() para 'esta':", resultado)

# Si no se encuentra ninguna coincidencia, devuelve una lista vacía.
# En este caso, "esta" aparece varias veces, por lo que la lista contiene esas ocurrencias.

#########################################

# 03. **\d**: Coincide con cualquier dígito numérico (0-9)

# Buscamos todos los dígitos en el texto (números de 0 a 9)
resultado = re.findall(r"\d", texto)
print("Resultado de re.findall(r'\\d'):", resultado)

# Esto encuentra todos los números en el texto, como el "1", "2", "3", etc.

# **\D**: Coincide con cualquier carácter que **no sea** un dígito
resultado = re.findall(r"\D", texto)
print("Resultado de re.findall(r'\\D'):", resultado)

# Esto encuentra todos los caracteres que no son números.

############################################

# 04. **\w**: Coincide con cualquier carácter alfanumérico (letras, números y guion bajo)

# Buscamos todos los caracteres alfanuméricos en el texto (letras y números)
resultado = re.findall(r"\w", texto)
print("Resultado de re.findall(r'\\w'):", resultado)

# Esto encontrará letras, números y guion bajo, pero no espacios ni puntuación.

# **\W**: Coincide con cualquier carácter que **no sea** alfanumérico
resultado = re.findall(r"\W", texto)
print("Resultado de re.findall(r'\\W'):", resultado)

# Esto encuentra los caracteres que no son letras, números o guion bajo.

############################################

# 05. **\s**: Coincide con cualquier espacio en blanco, incluyendo espacios, tabulaciones y saltos de línea

# Buscamos todos los espacios en blanco (espacios, tabulaciones, saltos de línea)
resultado = re.findall(r"\s", texto)
print("Resultado de re.findall(r'\\s'):", resultado)

# Esto encuentra todos los espacios y saltos de línea en el texto.

# **\S**: Coincide con cualquier carácter que **no sea** un espacio en blanco
resultado = re.findall(r"\S", texto)
print("Resultado de re.findall(r'\\S'):", resultado)

# Esto encuentra todo, excepto los espacios en blanco.

#################################################

# 06. **.**: Coincide con cualquier carácter **excepto** saltos de línea

# Busca todos los caracteres, pero **no incluye saltos de línea**
resultado = re.findall(r".", texto)
print("Resultado de re.findall(r'.'):", resultado)

# Esto encontrará todos los caracteres en el texto, pero no los saltos de línea. El salto de línea se omite.

##################################################

# 07. **\n**: Coincide con los saltos de línea

# Buscamos todos los saltos de línea en el texto
resultado = re.findall(r"\n", texto)
print("Resultado de re.findall(r'\\n'):", resultado)

# Esto encuentra todos los saltos de línea, ya que están representados por \n.

######################################################


# 07. **\\**: Cancela caracteres especiales

# Si quieres buscar el carácter de barra invertida (\), debes usar doble barra invertida (\\) 
# ya que \ es un carácter especial en expresiones regulares.

resultado = re.findall(r"\\", texto)
print("Resultado de re.findall(r'\\\\'):", resultado)

# En este caso, buscamos el carácter de barra invertida. No hay ninguna en el texto, así que la salida será una lista vacía.

#########################################################

# 08. Armando una cadena que busque un número seguido de un punto y un espacio

# Usamos el metacaracter \d para buscar un número y luego buscamos un punto y un espacio (\.\s)
resultado = re.findall(r"\d\.\s", texto)
print("Resultado de re.findall(r'\\d\\.\\s'):", resultado)

# Esto buscará un número, seguido de un punto y un espacio, como "1. ", "2. ", etc.
# En el texto de ejemplo, solo encontramos "1, ".

###########################################################

# 09. **^**: Coincide con el inicio de una línea o cadena

# Busca las cadenas que empiezan con "Hola" al inicio de una línea
resultado = re.findall(r"^Hola", texto)
print("Resultado de re.findall(r'^Hola'):", resultado)

# El símbolo ^ indica que la búsqueda debe comenzar al principio de la línea o cadena.

###########################################################

# 10. **$**: Coincide con el final de una línea o cadena

# Busca las cadenas que terminan con "capitan"
resultado = re.findall(r"capitan$", texto)
print("Resultado de re.findall(r'capitan$'):", resultado)

# El símbolo $ indica que la búsqueda debe coincidir con el final de la línea o cadena.

###########################################################

# 11. **()**: Agrupación de patrones

# Usamos paréntesis para agrupar partes del patrón y buscar repeticiones.
# Buscamos las palabras "Esta" seguidas de un número en el texto
resultado = re.findall(r"(Esta \w+)", texto)
print("Resultado de re.findall(r'(Esta \w+)'):", resultado)

# Esto devuelve todas las ocurrencias de "Esta" seguidas de una palabra, como "Esta es", "Esta linea", etc.

###########################################################

# 12. **|**: Alternancia (OR)

# Busca cadenas que sean "Hola" o "capitan"
resultado = re.findall(r"Hola|capitan", texto)
print("Resultado de re.findall(r'Hola|capitan'):", resultado)

# El símbolo | actúa como un operador OR, por lo que buscará cualquiera de los dos patrones.

###########################################################

# 13. **{n,m}**: Cuantificadores

# Busca una cadena con al menos 2 letras y hasta 4 letras en total
resultado = re.findall(r"\w{2,4}", texto)
print("Resultado de re.findall(r'\\w{2,4}'):", resultado)

# Esto busca todas las palabras que tienen entre 2 y 4 caracteres alfanuméricos.

###########################################################

# 14. **?**: Hace que el patrón anterior sea opcional

# Busca un número seguido de una letra (opcionalmente seguido de un punto)
resultado = re.findall(r"\d\w?", texto)
print("Resultado de re.findall(r'\\d\\w?'):", resultado)

# El símbolo ? hace que el patrón anterior (la letra) sea opcional, por lo que encontrará números seguidos de una letra o solo números.

