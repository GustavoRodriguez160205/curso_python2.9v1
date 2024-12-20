##############################################

# Introducción a los diccionarios
# Un diccionario es una estructura de datos que almacena pares de clave-valor,
# permitiendo acceder rápidamente al valor asociado a una clave.

# Características principales:
# - Claves únicas: Cada clave debe ser única, y las claves duplicadas sobrescriben el valor anterior.
# - Acceso rápido: Buscar valores por claves es eficiente, en promedio de tiempo constante.
# - Mutable: Los diccionarios pueden modificarse después de crearse.
# - Ordenados (a partir de Python 3.7): Mantienen el orden de inserción.

##############################################

# Métodos de creación de diccionarios

# Método 1: Usando dict()
diccionario = dict(nombre="Gustavo", apellido="Rodriguez")
print("Diccionario creado con dict():", diccionario)

# Método 2: Usando fromkeys() para crear un diccionario con claves pero sin valores
diccionario = dict.fromkeys(["Nombre", "Apellido"])
print("Diccionario con valores None:", diccionario)

# Método 3: Usando fromkeys() con un valor por defecto
diccionario = dict.fromkeys(["Nombre", "Apellido"], "No se")
print("Diccionario con valores por defecto:", diccionario)

##############################################

# Claves no mutables en diccionarios
# Las listas no pueden ser claves porque son mutables,
# pero podemos usar `frozenset` para crear claves inmutables.

# Usando frozenset como clave
diccionario_conjunto = {frozenset(["Dalto", "Rancio"]): "Jajaja"}
print("Diccionario con frozenset como clave:", diccionario_conjunto)

##############################################
