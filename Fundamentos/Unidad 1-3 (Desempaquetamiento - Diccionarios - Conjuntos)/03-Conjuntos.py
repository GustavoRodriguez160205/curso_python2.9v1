#####################################################
### Conjuntos en Python (Sets)
#####################################################

## Un conjunto en Python es una estructura de datos incorporada que implementa la teoría de conjuntos de la matemática.
## Sirve para almacenar colecciones de elementos únicos y no ordenados. Los conjuntos son especialmente útiles cuando necesitamos:
## - Eliminar duplicados de una colección.
## - Realizar operaciones de conjunto como unión, intersección, diferencia o diferencia simétrica.
## Características principales de los conjuntos en Python:
## - Los elementos son únicos (sin duplicados).
## - No tienen un orden específico (no son indexados).
## - Son mutables (pueden cambiar sus elementos después de ser creados).
## Los conjuntos son ideales para gestionar elementos únicos en aplicaciones que requieren un manejo eficiente 
## de datos y operaciones rápidas relacionadas con pertenencia y combinaciones.

#####################################################

# 01. Creación de un conjunto utilizando la función `set()`
conjunto = set(["Dato1", "Dato2", "Dato2"])  # 'Dato2' se eliminará automáticamente, ya que los conjuntos no permiten duplicados.
print(f"Creamos nuestro primer conjunto (sin duplicados): {conjunto}")    

#####################################################

# 02. Intento de poner un conjunto dentro de otro conjunto
# Esto dará error porque los conjuntos deben tener elementos "hashables" (inmutables).
# Los conjuntos son mutables, lo que genera un error si intentamos incluir uno dentro de otro.

try:
    conjunto1 = {"Dato1", "Dato2"}
    conjunto2 = {conjunto1, "Dato3"}  # Esto dará error: TypeError: unhashable type: 'set'
except TypeError as e:
    print(f"Error al intentar agregar un conjunto dentro de otro: {e}")

# Explicación:
# Los elementos de un conjunto deben ser "hashables", es decir, inmutables. Los conjuntos son mutables, por lo que no pueden ser elementos de otros conjuntos.

#####################################################
# 03. Forma correcta de incluir un conjunto dentro de otro conjunto
# Usamos `frozenset`, que es un conjunto inmutable (no se puede modificar).
conjunto1 = frozenset(["Dato1", "Dato2"])  # 'frozenset' crea un conjunto inmutable.
conjunto2 = {conjunto1, "Dato3"}  # Ahora 'conjunto1' es inmutable y puede ser un elemento de otro conjunto.
print(f"Conjunto con frozenset dentro: {conjunto2}")  # Salida: {frozenset({'Dato1', 'Dato2'}), 'Dato3'}

#####################################################
# 04. Teoría de Conjuntos: Operaciones de conjunto
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

# Verificamos si conjunto2 es un subconjunto de conjunto1
es_subconjunto = conjunto2.issubset(conjunto1)  # También se puede usar `conjunto2 <= conjunto1`
print(f"¿Es conjunto2 un subconjunto de conjunto1?: {es_subconjunto}")  # Salida: True

# Verificamos si conjunto2 es un superconjunto de conjunto1
es_superconjunto = conjunto2.issuperset(conjunto1)  # También se puede usar `conjunto2 >= conjunto1`
print(f"¿Es conjunto2 un superconjunto de conjunto1?: {es_superconjunto}")  # Salida: False

# Verificamos si los conjuntos tienen elementos en común
hay_comun = conjunto2.isdisjoint(conjunto1)  # Devuelve True si no hay elementos en común, False si los hay.
print(f"¿Hay elementos en común entre conjunto1 y conjunto2?: {not hay_comun}")  # Salida: True

#####################################################

# 05. Añadir elementos a un conjunto
conjunto = {1, 2, 3}
conjunto.add(4)  # 
print(f"Conjunto después de agregar un elemento: {conjunto}")  
#####################################################


# 06. Eliminar un elemento de un conjunto

conjunto = {1, 2, 3}
conjunto.remove(2)  # Elimina el elemento '2'. Si no existe, lanzará un error.
print(f"Conjunto después de eliminar el elemento '2': {conjunto}")  

# Nota: Si intentamos eliminar un elemento que no existe, lanzará un `KeyError`.
try:
    conjunto.remove(5)  # Intentamos eliminar un elemento que no existe en el conjunto.
except KeyError as e:
    print(f"Error al intentar eliminar un elemento que no existe: {e}")

#####################################################

# 07. Eliminar un elemento sin error si no existe
conjunto = {1, 2, 3}
conjunto.discard(4)  # Elimina el elemento '4' si existe. Si no, no hace nada y no lanza error.
print(f"Conjunto después de intentar eliminar un elemento no existente: {conjunto}")  



#####################################################

# 08. Otras operaciones útiles con conjuntos
# Uso de frozenset para crear conjuntos inmutables (útil para claves en diccionarios).
frozen_set = frozenset([10, 20, 30])
print(f"Un conjunto inmutable: {frozen_set}") 

# Verificando la longitud de un conjunto
print(f"Longitud del conjunto: {len(conjunto)}")  

# Verificando si un elemento está en el conjunto
print(f"¿Está el elemento 3 en el conjunto?: {3 in conjunto}")  # Salida: True


################################################

