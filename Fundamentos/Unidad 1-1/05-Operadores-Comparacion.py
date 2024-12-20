#######################################################
# ¿Qué son los operadores de comparación en Python?
#######################################################

# Los operadores de comparación en Python se utilizan para comparar dos valores. 
# Devuelven un resultado booleano (`True` o `False`) dependiendo de si la comparación es verdadera o no.

#######################################################
# Tipos de operadores de comparación
#######################################################

# Igualdad (==): Comprueba si dos valores son iguales.
es_igual_que = 3 == 3  # True, porque 3 es igual a 3
print(f"3 == 3: {es_igual_que}")  # Imprime: True

# Desigualdad (!=): Comprueba si dos valores son diferentes.
es_distinto_que = 2 != 5  # True, porque 2 no es igual a 5
print(f"2 != 5: {es_distinto_que}")  # Imprime: True

# Mayor que (>): Comprueba si un valor es mayor que otro.
mayor_que = 4 > 1  # True, porque 4 es mayor que 1
print(f"4 > 1: {mayor_que}")  # Imprime: True

# Menor que (<): Comprueba si un valor es menor que otro.
menor_que = 7 < 10  # True, porque 7 es menor que 10
print(f"7 < 10: {menor_que}")  # Imprime: True

# Mayor o igual que (>=): Comprueba si un valor es mayor o igual a otro.
mayor_o_igual = 6 >= 6  # True, porque 6 es igual a 6
print(f"6 >= 6: {mayor_o_igual}")  # Imprime: True

# Menor o igual que (<=): Comprueba si un valor es menor o igual a otro.
menor_o_igual = 3 <= 5  # True, porque 3 es menor que 5
print(f"3 <= 5: {menor_o_igual}")  # Imprime: True

#######################################################
# Ejemplos prácticos de comparación
#######################################################

# Comparación con variables
a = 5
b = 19
c = 20

comparacion = a + b == c  # Comprueba si la suma de 'a' y 'b' es igual a 'c'
print(f"a + b == c: {comparacion}")  # Devuelve: False

# Comparación de cadenas (case-sensitive)
contraseña_guardada = "DaltoMaestro"
contraseña_tipeada = "DaltoMaestro"

# Comprueba si las contraseñas coinciden
es_correcta = contraseña_guardada == contraseña_tipeada
print(f"Contraseña correcta: {es_correcta}")  # Devuelve: True

# Comparación numérica con condicionales
edad = 18
mayoria_edad = 18

es_mayor_de_edad = edad >= mayoria_edad
if es_mayor_de_edad:
    print("Es mayor de edad.")  # Imprime: Es mayor de edad.
else:
    print("No es mayor de edad.")

#######################################################
# Ejemplos avanzados
#######################################################

# Comparaciones encadenadas
x = 5
y = 10
z = 15

# Verifica si x < y < z (x es menor que y, y es menor que z)
encadenada = x < y < z
print(f"x < y < z: {encadenada}")  # Devuelve: True

# Comparación con listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = [4, 5, 6]

# Comprueba si dos listas tienen los mismos elementos
print(f"Lista1 es igual a Lista2: {lista1 == lista2}")  # Devuelve: True
print(f"Lista1 es igual a Lista3: {lista1 == lista3}")  # Devuelve: False

# Comparación de tipos
numero = 42
cadena = "42"

# Comprueba si un número y una cadena son iguales (no lo son porque tienen tipos diferentes)
print(f"¿'42' es igual a 42?: {cadena == numero}")  # Devuelve: False

#######################################################
# Aplicación práctica: Validación
#######################################################

# Validar una entrada de usuario
usuario_esperado = "admin"
usuario_ingresado = "Admin"

# Comparación sin importar mayúsculas/minúsculas
es_valido = usuario_esperado.lower() == usuario_ingresado.lower()
print(f"Usuario válido: {es_valido}")  # Devuelve: True
