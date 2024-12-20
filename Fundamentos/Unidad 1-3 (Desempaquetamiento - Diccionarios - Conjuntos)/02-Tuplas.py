#####################################################
# Introducción a las Tuplas en Python


# Las tuplas son una estructura de datos inmutable, útil para almacenar colecciones ordenadas de elementos.
# Al ser inmutables, proporcionan seguridad adicional en datos que no deben cambiarse.

#####################################################
# Características de las tuplas:
# 1. **Inmutables:** No se pueden modificar después de su creación.
# 2. **Ordenadas:** Mantienen el orden de los elementos.
# 3. **Accesibles por índice:** Se puede acceder a elementos específicos usando índices.
# 4. **Permiten duplicados:** Puedes tener elementos repetidos.
# 5. **Sintaxis:** Se definen usando paréntesis `()` o simplemente separando elementos por comas.

#####################################################
# Métodos de creación de tuplas

# 01. Creando una tupla usando la función `tuple()`
tupla_desde_funcion = tuple(["Dato1", "Dato2"])  # Convierte una lista a tupla
print(f"Tupla creada con la función tuple: {tupla_desde_funcion}")

# 02. Creando una tupla sin paréntesis
tupla_sin_parentesis = "Dato1", "Dato2"  # Paréntesis opcionales
print(f"Tupla creada sin paréntesis: {tupla_sin_parentesis}")

# 03. Creando una tupla vacía
tupla_vacia = ()
print(f"Tupla vacía: {tupla_vacia}")

# 04. Creando una tupla con un solo elemento
tupla_un_elemento = ("Dato1",)  # Se necesita la coma final para diferenciar de un valor entre paréntesis
print(f"Tupla con un solo elemento: {tupla_un_elemento}")

#####################################################
# Operaciones básicas con tuplas

# Acceso por índice
tupla = (10, 20, 30, 40, 50)
print(f"Elemento en el índice 2: {tupla[2]}")  # Salida: 30

# Acceso con índices negativos
print(f"Último elemento: {tupla[-1]}")  # Salida: 50

# Rebanadas (slicing)
print(f"Elementos del índice 1 al 3: {tupla[1:4]}")  # Salida: (20, 30, 40)

#####################################################
# Métodos y funciones útiles con tuplas

# 01. `count()`: Cuenta cuántas veces aparece un elemento en la tupla.
tupla = (1, 2, 3, 1, 4, 1)
print(f"El número 1 aparece {tupla.count(1)} veces en la tupla.")  # Salida: 3

# 02. `index()`: Devuelve el índice de la primera aparición de un elemento.
print(f"El índice del número 3 es: {tupla.index(3)}")  # Salida: 2

# 03. `len()`: Obtiene la cantidad de elementos en la tupla.
print(f"La longitud de la tupla es: {len(tupla)}")  # Salida: 6

# 04. `in`: Verifica si un elemento está en la tupla.
print(f"¿Está el número 4 en la tupla?: {4 in tupla}")  # Salida: True

# 05. `tuple()`: Convierte una lista u otro iterable en una tupla.
lista = [5, 6, 7]
nueva_tupla = tuple(lista)
print(f"Lista convertida a tupla: {nueva_tupla}")  # Salida: (5, 6, 7)

#####################################################
# Iteración y desempaquetado

# Iterar sobre una tupla
for elemento in tupla:
    print(f"Elemento: {elemento}")

# Desempaquetado de tuplas
tupla = (100, 200, 300)
a, b, c = tupla
print(f"Desempaquetado: a={a}, b={b}, c={c}")

# Desempaquetado con valores sobrantes
tupla = (1, 2, 3, 4, 5)
x, *y, z = tupla
print(f"x={x}, y={y}, z={z}")  # Salida: x=1, y=[2, 3, 4], z=5

#####################################################
# Uso avanzado de tuplas

# Tuplas anidadas
tupla_anidada = ((1, 2), (3, 4), (5, 6))
print(f"Tupla anidada: {tupla_anidada}")
print(f"Acceso al primer elemento del segundo par: {tupla_anidada[1][0]}")  # Salida: 3

# Tuplas como claves en un diccionario
diccionario = {
    (1, 2): "Par 1",
    (3, 4): "Par 2"
}
print(f"Valor para la clave (1, 2): {diccionario[(1, 2)]}")  # Salida: "Par 1"

#####################################################
# Ejemplo práctico: Coordenadas
# Las tuplas son útiles para representar datos como coordenadas o puntos fijos.
coordenadas = (40.7128, -74.0060)  # Latitud y longitud de Nueva York
print(f"Coordenadas de Nueva York: {coordenadas}")

#####################################################
