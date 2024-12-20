#######################################################
# DATOS COMPUESTOS EN PYTHON
#######################################################

# Los datos compuestos son estructuras que permiten almacenar múltiples valores, 
# que pueden ser de tipos diferentes, en una sola variable. A continuación, se presentan
# los tipos más comunes de datos compuestos en Python.

#######################################################
# 01. Listas
#######################################################

# Las listas son colecciones ordenadas y mutables (pueden modificarse). 
# Son ideales para almacenar datos que pueden cambiar a lo largo del programa.
lista = ['Lucas Dalto', 'Soy Dalto', False, 1.64]

# Accediendo a un elemento de la lista por índice
print(f"Primer elemento de la lista: {lista[0]}")  # 'Lucas Dalto'

# Modificando un elemento de la lista
lista[3] = 'Maquinola'
print(f"Lista después de la modificación: {lista}")  # ['Lucas Dalto', 'Soy Dalto', False, 'Maquinola']

# Método `type` para verificar el tipo de dato
print(f"Tipo de 'lista': {type(lista)}")  # <class 'list'>

#######################################################
# 02. Tuplas
#######################################################

# Las tuplas son colecciones ordenadas e inmutables (no pueden modificarse).
tupla = ('Lucas Dalto', 'Soy Dalto', True, 1.41)

# Accediendo a elementos por índice
print(f"Primer elemento de la tupla: {tupla[0]}")  # 'Lucas Dalto'

# Método `type`
print(f"Tipo de 'tupla': {type(tupla)}")  # <class 'tuple'>

# Nota: Si necesitas modificar una tupla, puedes convertirla a lista, modificarla, y luego volverla a tupla:
tupla_modificable = list(tupla)
tupla_modificable[1] = 'Modificado'
tupla = tuple(tupla_modificable)
print(f"Tupla modificada: {tupla}")

#######################################################
# 03. Conjuntos (Set)
#######################################################

# Los conjuntos son colecciones desordenadas, no indexadas y sin elementos duplicados.
# No se pueden acceder a los elementos por índice.
conjunto = {'Leonel Messi', 'El goat', True, 1.65}

# Los valores no tienen un orden fijo
print(f"Conjunto: {conjunto}")

# Ejemplo de verificación de pertenencia
print(f"'Leonel Messi' está en el conjunto: {'Leonel Messi' in conjunto}")  # True

# Método `type`
print(f"Tipo de 'conjunto': {type(conjunto)}")  # <class 'set'>

#######################################################
# 04. Diccionarios
#######################################################

# Los diccionarios almacenan datos como pares clave-valor.
# Son desordenados y mutables.
diccionario = {
    'Nombre': 'Lucas Dalto',
    'Canal': 'Soy Dalto',
    'Esta_emocionado': True,
    'Altura': 1.96
}

# Accediendo a un valor usando su clave
print(f"Nombre: {diccionario['Nombre']}")  # 'Lucas Dalto'
print(f"Canal: {diccionario['Canal']}")  # 'Soy Dalto'

# Modificando un valor en el diccionario
diccionario['Altura'] = 1.80
print(f"Diccionario modificado: {diccionario}")

# Agregando un nuevo par clave-valor
diccionario['Edad'] = 30
print(f"Diccionario con nueva clave: {diccionario}")

# Eliminando un elemento
del diccionario['Esta_emocionado']
print(f"Diccionario después de eliminar clave: {diccionario}")

# Método `type`
print(f"Tipo de 'diccionario': {type(diccionario)}")  # <class 'dict'>

#######################################################
# NOTAS GENERALES
#######################################################

# - Los índices en listas y tuplas comienzan desde 0.
# - Para modificar datos inmutables (como tuplas), necesitas crear una nueva estructura.
# - Usa conjuntos cuando no necesites un orden o valores repetidos.
# - Los diccionarios son perfectos para trabajar con datos estructurados como JSON.
