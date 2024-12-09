###  Listas en Python

##  Las listas son una de las estructuras de datos más comunes en Python. Son colecciones ordenadas y mutables, 
## Lo que significa que puedes modificar su contenido después de haberlas creado. 
## Puedes agregar, eliminar o modificar los elementos de una lista.

## Características de las listas:
## - Mutabilidad: Las listas son modificables, lo que te permite cambiar, agregar o eliminar elementos después de su creación.
## - Ordenada: Al igual que las tuplas, las listas mantienen el orden de sus elementos.
## - Accesible por índice: Los elementos de las listas también se pueden acceder utilizando índices.
## - Permite elementos repetidos: Puedes tener elementos duplicados en una lista.
## - Uso de corchetes: Las listas se definen utilizando corchetes [].




## 01. List (Es un metodo , no una función. Nos sirve para crear listas)
lista = list(["Hola" , "Dalto" , 34 , True])
print(f"La lista queda: {lista}")

## 02. Len (Nos va a devolver la cantidad de elementos que tiene la lista)

largo = len(lista)
print(f"La longitud de la lista es de: {largo}")

## 03. Append (Nos permite agregar elementos a la lista)

lista.append("Holaa")
print(f"Lista después de agregado: {lista}")

## 04. Insert (También agrega un elemento pero en el orden que le digamos)

lista.insert(2, "River Plate")
print(f"Lista después de insert: {lista}")

## 05. Extend (Agrega varios elementos a la lista)

lista.extend([2024 , True])
print(f"Lista después de extend: {lista}")

## 06. Pop (Nos sirve para eliminar un elemento de la lista , por su índice)

lista.pop(2)
print(f"Lista después de POP: {lista}")

## Aclaración: -1 Nos sirve para eliminar el último elemento, -2 para el anteultimo y asi sucesivamente.


## 07. Remove (Eliminamos un elemento por su valor)

lista.remove("Holaa")
print(f"Lista después de Remove: {lista}")

## 08. Clear (Elimina todos los elementos de una lista)

#lista.clear()
#print(f"Lista despues de clear")

## 09. Sort (Nos sirve para ordenar una lista de forma ascendente)
## Aclaración: Si usamos el reverse = true la ordena en forma descendente

precios = [199.99 , 49.99 , 5.99 , 89.99 , 10.0]
precios.sort(reverse=True)
print(f"Los precios ordenados quedan asi: {precios}")


## 10. Reverse (Invierte los elementos de la lista)
## Aclaración: También se puede usar el reverse = true

colores = ["rojo", "verde", "azul", "amarillo"]
colores.reverse()
print(f"Lista con Reverse: {colores}")

## Aclaración: Busca elementos completos

## 11. Saber si se encuentra en la lista
lista_De_prueba = [10 , 20 , 30 , 40 , 55 , 66 , 77]
elemento_encontrado = lista_De_prueba.index(77)
print(f"El elemento encontrado en la lista: {elemento_encontrado}")