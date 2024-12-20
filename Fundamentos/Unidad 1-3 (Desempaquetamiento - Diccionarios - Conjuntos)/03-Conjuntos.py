#####################################################
# Conjuntos en Python (Sets)



# Un conjunto es una estructura de datos que implementa la teoría de conjuntos.
# Permite almacenar colecciones de elementos únicos y no ordenados.
# Utilidades principales:
# - Eliminar duplicados de una colección.
# - Operaciones como unión, intersección, diferencia o diferencia simétrica.

# Características principales:
# - Elementos únicos (sin duplicados).
# - No ordenados (no indexados).
# - Mutables (pueden cambiarse después de crearse).
# - Los elementos deben ser "hashables" (inmutables, como números, cadenas o tuplas).

#####################################################

# 01. Creación de un conjunto utilizando `set()`
conjunto = set(["Dato1", "Dato2", "Dato2"])  # 'Dato2' se elimina automáticamente
print(f"Primer conjunto (sin duplicados): {conjunto}")

#####################################################

# 02. Error al intentar incluir un conjunto dentro de otro
# Los conjuntos mutables no son hashables y no pueden ser elementos de otros conjuntos.
try:
    conjunto1 = {"Dato1", "Dato2"}
    conjunto2 = {conjunto1, "Dato3"}  # Esto genera TypeError
except TypeError as e:
    print(f"Error al agregar un conjunto dentro de otro: {e}")

#####################################################

# 03. Forma correcta: Usar `frozenset` (conjunto inmutable)
conjunto1 = frozenset(["Dato1", "Dato2"])  # frozenset crea un conjunto inmutable
conjunto2 = {conjunto1, "Dato3"}  # frozenset puede ser clave o elemento
print(f"Conjunto con frozenset dentro: {conjunto2}")

#####################################################

# 04. Operaciones de conjuntos (Teoría de Conjuntos)
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

# Subconjunto y superconjunto
es_subconjunto = conjunto2.issubset(conjunto1)
print(f"¿conjunto2 es un subconjunto de conjunto1?: {es_subconjunto}")

es_superconjunto = conjunto2.issuperset(conjunto1)
print(f"¿conjunto2 es un superconjunto de conjunto1?: {es_superconjunto}")

# Elementos en común
hay_comun = conjunto2.isdisjoint(conjunto1)  # True si no hay elementos en común
print(f"¿Hay elementos en común entre conjunto1 y conjunto2?: {not hay_comun}")

#####################################################

# 05. Agregar elementos a un conjunto
conjunto = {1, 2, 3}
conjunto.add(4)  # Agrega '4' al conjunto
print(f"Conjunto después de agregar un elemento: {conjunto}")

#####################################################

# 06. Eliminar elementos de un conjunto
conjunto = {1, 2, 3}
conjunto.remove(2)  # Elimina '2'. Si no existe, lanza KeyError.
print(f"Conjunto después de eliminar el elemento '2': {conjunto}")

# Manejo de errores al eliminar un elemento inexistente
try:
    conjunto.remove(5)  # Elemento inexistente
except KeyError as e:
    print(f"Error al eliminar un elemento inexistente: {e}")

#####################################################

# 07. Eliminar sin error con `discard`
conjunto = {1, 2, 3}
conjunto.discard(4)  # No lanza error si el elemento no existe
print(f"Conjunto después de intentar eliminar un elemento no existente: {conjunto}")

#####################################################

# 08. Otras operaciones útiles con conjuntos

# Conjunto inmutable (`frozenset`)
frozen_set = frozenset([10, 20, 30])
print(f"Conjunto inmutable (frozenset): {frozen_set}")

# Longitud del conjunto
print(f"Longitud del conjunto: {len(conjunto)}")

# Verificar si un elemento pertenece al conjunto
print(f"¿El elemento 3 está en el conjunto?: {3 in conjunto}")

#####################################################
