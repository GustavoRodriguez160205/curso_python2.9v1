###############################################

### Que es iterar?

## En programación, iterar significa recorrer una colección de datos o un conjunto de elementos, ejecutando repetidamente una serie de instrucciones para cada uno de ellos. Este proceso se detiene cuando se han recorrido todos los elementos o se cumple una condición específica. 
## Por ejemplo, es como recorrer todos los casilleros de una grilla, realizando una acción en cada uno, utilizando estructuras como for o while.

#################################################

### ¿ Cuales son los objetos iterables ?

##   Un iterable es un objeto en Python que puede ser recorrido secuencialmente
##   obteniendo uno de sus elementos a la vez. 
##   Los objetos iterables permiten usar bucles para acceder a sus elementos de manera ordenada.
##   Algunos ejemplos comunes de iterables en Python son:

## - Listas
## - Tuplas
## - Conjuntos
## - Diccionarios
## - Cadenas de texto

#################################################

lista = ["Gato" , "Perro" , "Loro" , "Cocodrilo"]

# Recorriendo la Lista Animales
for animal in lista:
    print(f"Ahora la variable animal es igual a: {animal}")

################################################

numeros = [10 , 21 , 11 , 44 ]

# Recorriendo la lista números y multiplicando su valor
for numero in numeros:
    resultado = numero * 5
    print(f"Los números multiplicados quedan asi: {resultado}")


##################################################

## Iteramos ambas listas juntas con un zip.

for numero , animal in zip(numeros , lista):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")


## La función zip nos permite iterar 2 listas al mismo tiempo
## Se itera todo al mismo tiempo

######################################################


## Otro que también nos sirve para iterar: Range

for num in range(1 , 10):
    print(f"Los números del 1 al 10 son: {num}")


## Esto nos va a permitir iterar los números del x numero a x número
## El ultimo número no lo cuenta.


## También Funciona para las listas. (Forma no optima)

for num in range(len(numeros)):  ## No funciona en Conjuntos
    print(numeros[num])

##################################################################


## La forma correcta es con enumerate

numeros = [10, 20, 30, 40]

for indice, valor in enumerate(numeros):
    print(f"El índice es {indice} y el valor es {valor}")

######################################################################

## Usando el Else

## El bloque else en un bucle se ejecuta cuando el bucle termina normalmente, es decir, sin que se interrumpa con un break.

numeros = [1, 2, 3, 4, 5]

for numero in numeros: # Recorre el elemento de la lista y imprime el resultado
    print(f"Procesando el número: {numero}")
else: # Este bloque solo se ejecuta si el bucle termino normalmente. Si hay un break el else no se ejecuta
    print("El bucle ha terminado sin interrupciones.")

#########################################################################

## Todo esto funciona lo mismo para las tuplas y Conjuntos

###########################################################################