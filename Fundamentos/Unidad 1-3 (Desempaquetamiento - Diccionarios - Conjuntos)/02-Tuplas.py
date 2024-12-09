### Introducción a las tuplas


## Las tuplas son una estructura de datos en Python que se utilizan para almacenar una colección ordenada de elementos.
## A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación (no se pueden agregar, eliminar ni cambiar sus elementos). 
## Son muy útiles cuando necesitas asegurarte de que los datos no sean modificados accidentalmente.

## Características de las tuplas:
##   Inmutabilidad: Una vez creada una tupla, no se puede cambiar. Esto las hace más seguras en cuanto a manipulación de datos.
##   Ordenada: Los elementos dentro de una tupla mantienen su orden, es decir, el primer elemento es siempre el primero, el segundo es siempre el segundo, etc.
##   Accesible por índice: Puedes acceder a los elementos de una tupla usando índices, al igual que en las listas.
##   Permite elementos repetidos: Al igual que las listas, las tuplas pueden tener elementos duplicados.
##   Uso de paréntesis: Se define una tupla utilizando paréntesis ().


### Metodos de Creación de Tuplas

## 01. Creando una tupla usando la función Tuple
tupla_desde_funcion = tuple(["Dato1" , "Dato2"])
print(f"Tupla creada con la función tuple: {tupla_desde_funcion}")

## 02. Creando una tupla sin parentesis
tupla_sin_parentesis = "Dato1" , "Dato2"
print(f"Tupla Creada sin paréntesis: {tupla_sin_parentesis}")

###################################