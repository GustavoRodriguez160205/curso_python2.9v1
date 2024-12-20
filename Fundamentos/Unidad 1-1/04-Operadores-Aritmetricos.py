###################################################
# OPERADORES ARITMÉTICOS EN PYTHON
###################################################

# Los operadores aritméticos en Python se utilizan para realizar operaciones matemáticas con números.

###################################################
# 01. Suma (+) y Resta (-)
###################################################

# La suma y la resta son operaciones básicas que se realizan con los operadores `+` y `-`.

suma = 12 + 5  # Suma de dos números
resta = 12 - 5  # Resta de dos números

print(f'El resultado de la suma es: {suma} y de la resta es: {resta}')
# Imprime: El resultado de la suma es: 17 y de la resta es: 7

###################################################
# 02. Multiplicación (*) y División (/)
###################################################

# La multiplicación y la división se realizan con los operadores `*` y `/`.

multiplicar = 3 * 5  # Multiplicación de dos números
dividir = 2 / 4  # División de dos números

print(f'El resultado de la multiplicación es: {multiplicar} y de la división es: {dividir}')
# Imprime: El resultado de la multiplicación es: 15 y de la división es: 0.5

###################################################
# 03. Potenciación (**)
###################################################

# La potenciación se realiza utilizando el operador `**`.

exponente = 12 ** 5  # 12 elevado a la 5
print(f'El resultado de la potenciación es: {exponente}')
# Imprime: El resultado de la potenciación es: 248832

###################################################
# 04. División baja (//)
###################################################

# La división baja, también conocida como "floor division", devuelve el cociente de la división redondeado hacia abajo al número entero más cercano.
# Se realiza con el operador `//`.

divicion_baja = 12 // 5  # División de 12 entre 5 con redondeo hacia abajo
print(f'El resultado de la división baja es: {divicion_baja}')
# Imprime: El resultado de la división baja es: 2

###################################################
# 05. Resto o Módulo (%)
###################################################

# El operador módulo `%` devuelve el residuo de la división de dos números.

resto = 12 % 8  # Resto de la división de 12 entre 8
print(f'El resultado del resto es: {resto}')
# Imprime: El resultado del resto es: 4

###################################################
# Notas importantes:
###################################################

# - El operador `/` siempre devuelve un número decimal (float), incluso si la división es exacta.
# - El operador `//` devuelve el cociente entero de la división (sin decimales).
# - El operador `%` devuelve el residuo de la división.
# - Los operadores aritméticos siguen las reglas matemáticas estándar de precedencia (PEMDAS).
#   Es decir, multiplicación y división tienen mayor precedencia que la suma y la resta, 
#   y las operaciones entre paréntesis se ejecutan primero.

