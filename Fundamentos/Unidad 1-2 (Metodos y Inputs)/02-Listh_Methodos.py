###  Listas en Python

##  Las listas son una de las estructuras de datos más comunes en Python. Son colecciones ordenadas y mutables, 
## ,Lo que significa que puedes modificar su contenido después de haberlas creado. 
##  Puedes agregar, eliminar o modificar los elementos de una lista.

## Características de las listas:


## - Mutabilidad: Las listas son modificables, lo que te permite cambiar, agregar o eliminar elementos después de su creación.
## - Ordenada: Al igual que las tuplas, las listas mantienen el orden de sus elementos.
## - Accesible por índice: Los elementos de las listas también se pueden acceder utilizando índices.
## - Permite elementos repetidos: Puedes tener elementos duplicados en una lista.
## - Uso de corchetes: Las listas se definen utilizando corchetes [].



# 01. list() - Crea una lista a partir de un iterable (como una tupla, conjunto, etc.)
# Es un método, no una función. Nos sirve para crear listas.
lista = list(["Hola", "Dalto", 34, True])
print(f"La lista creada es: {lista}")





# 02. len() - Devuelve la cantidad de elementos en la lista
# Nos va a devolver la cantidad de elementos que tiene la lista.
largo = len(lista)
print(f"La longitud de la lista es: {largo}")



# 03. append() - Agrega un elemento al final de la lista
# Nos permite agregar elementos a la lista.
lista.append("Nuevo Elemento")
print(f"Lista después de append: {lista}")



# 04. insert() - Agrega un elemento en una posición específica
# Agrega un elemento en el orden que le digamos.
lista.insert(2, "River Plate")
print(f"Lista después de insert: {lista}")


# 05. extend() - Agrega múltiples elementos al final de la lista
# Agrega varios elementos a la lista.
lista.extend([2024, False])
print(f"Lista después de extend: {lista}")


# 06. pop() - Elimina un elemento por su índice
# Nos sirve para eliminar un elemento de la lista por su índice.
elemento_eliminado = lista.pop(2)
print(f"Elemento eliminado: {elemento_eliminado}")
print(f"Lista después de pop: {lista}")
# Aclaración: Puedes usar índices negativos para eliminar elementos desde el final (ej. -1 para el último).


# 07. remove() - Elimina el primer elemento que coincida con el valor
# Elimina un elemento por su valor (no por su índice).
lista.remove("Nuevo Elemento")
print(f"Lista después de remove: {lista}")


# 08. clear() - Elimina todos los elementos de la lista
# Elimina todos los elementos de una lista.
lista.clear()
print(f"Lista después de clear: {lista}")



# 09. sort() - Ordena la lista de forma ascendente
# Nos sirve para ordenar una lista de forma ascendente.
precios = [199.99, 49.99, 5.99, 89.99, 10.0]
precios.sort(reverse=True)  # Si usamos reverse=True, ordena de forma descendente.
print(f"Los precios ordenados quedan así: {precios}")


# 10. reverse() - Invierte el orden de los elementos en la lista
# Invierte los elementos de la lista.
colores = ["rojo", "verde", "azul", "amarillo"]
colores.reverse()
print(f"Lista después de reverse: {colores}")


# 11. index() - Busca el primer índice de un valor en la lista
# Nos ayuda a encontrar la posición (índice) de un elemento.
lista_De_prueba = [10, 20, 30, 40, 55, 66, 77]
elemento_encontrado = lista_De_prueba.index(77)
print(f"El elemento 77 se encuentra en el índice: {elemento_encontrado}")
