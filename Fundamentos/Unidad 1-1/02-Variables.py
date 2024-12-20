#######################################################
# ¿Qué son las variables en Python?
#######################################################

# Las variables son espacios reservados en la memoria que se utilizan para almacenar datos.
# Los datos almacenados en una variable pueden reutilizarse y modificarse a lo largo de un programa.

#######################################################

# Declaración y uso de variables

#######################################################

# Ejemplo con texto: Mostrar un nombre por consola
nombre = "Javier"
print(f"El nombre almacenado en la variable es: {nombre}")

# Ejemplo con números: Realizamos una suma de variables
a = 4
b = 12
c = a + b  # Sumar los valores de 'a' y 'b' y almacenarlos en 'c'
print(f"La suma de {a} y {b} es: {c}")

# Otro ejemplo con operadores compuestos
numero = 10
numero += 5  # Incrementa en 5
numero += 5  # Incrementa nuevamente en 5
numero -= 3  # Decrementa en 3
print(f"El valor final de la variable 'numero' es: {numero}")

#######################################################

# Concatenación de variables

#######################################################

# La concatenación consiste en unir dos cadenas de texto (strings).
# Ejemplo básico (no recomendado porque no funciona con números):
nombre = "Lucas"
bienvenida = "Hola " + nombre + ", ¿cómo estás?"
print(bienvenida)

# Forma recomendada: f-strings
nombre = "Pedro"
bienvenida = f"Hola {nombre}, ¿cómo estás?"
print(bienvenida)

#######################################################

# Uso del operador DEL

#######################################################

# El operador 'del' elimina una variable, liberando el espacio que ocupaba en memoria.
nombre = "Ana"
bienvenida = f"Hola {nombre}, ¿cómo estás?"
del nombre  # Elimina la variable 'nombre'
print(bienvenida)  # Funciona porque 'nombre' ya fue utilizada en 'bienvenida'

#######################################################

# Operadores de pertenencia e identidad

#######################################################

# Operadores de pertenencia (`in` y `not in`):
# Se utilizan para comprobar si un elemento está presente en una secuencia (como una cadena de texto).

nombre = "Lucas"
bienvenida = f"Hola {nombre}, ¿cómo estás?"

# Comprueba si "Lucas" está en la cadena de texto
print("Lucas" in bienvenida)  # True, porque "Lucas" está en 'bienvenida'

# Comprueba si "Mario" no está en la cadena de texto
print("Mario" not in bienvenida)  # True, porque "Mario" no está en 'bienvenida'

# Operadores de identidad (`is` y `is not`):
# Se utilizan para comprobar si dos variables apuntan al mismo objeto en memoria.
x = [1, 2, 3]
y = x  # Ambas variables apuntan al mismo objeto
z = [1, 2, 3]  # Es un objeto diferente, aunque tenga el mismo contenido

print(x is y)  # True, porque apuntan al mismo objeto
print(x is z)  # False, porque son objetos distintos
print(x == z)  # True, porque tienen el mismo contenido

#######################################################

# Estilos de escritura de variables

#######################################################

# CamelCase: La primera palabra es en minúscula y cada palabra subsecuente comienza con mayúscula.
nombreCompleto = "Lucas Dalto"

# Snake_case: Las palabras están separadas por guiones bajos. Este estilo es el recomendado en Python.
nombre_completo = "Leonel Andrés Messi"

print(f"CamelCase: {nombreCompleto}")
print(f"Snake_case: {nombre_completo}")
