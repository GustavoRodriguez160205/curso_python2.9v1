### Practica de metodos de cadenas

## 01. Ordenar una lista

numeros = [5, 3, 2 , 1 , 9 , 10 , 7 , 4]
numeros.sort() # Ordenamos de forma ascendente
print("Ascendente:" , numeros)

numeros.sort(reverse = True) # Ordenamos de forma Descendente
print("Descendente:" , numeros)


## 02. Contar elementos que aparecen en una lista

numeros = [ 3 , 7 , 3 , 1 , 3 , 7 , 2 ]
conteo = numeros.count(3)
print("El número 3 aparece:" , conteo , "veces")

## 03. Extender una lista

lista1 = [1 , 2 , 3]
lista2 = [4 , 5 , 6]

## 05. Revertir una lista

cadenas = ["Python" , "Java" , "C++" , "Ruby"]
cadenas.reverse() # Revertimos el Orden
print("Lista Invertida:" , cadenas)


## 06. Búsqueda de índice

numeros= [5 , 3 , 8 , 3 , 10 , 3]
indice = numeros.index(3)
print("El índice del primer 3 es:" , indice)


## 06. Lista de Provincias argentinas. Eliminar y Agregar

provincias = ["Buenos Aires" , "Cordoba" , "Santa Fe" , "Mendoza" , "Tucumán"]
provincias.append("Salta") # Agregamos
print("Después de Agregar:" , provincias)

provincias.remove("Mendoza")
print("Después de eliminar:" , provincias)


## 07. Equipos de Fútbol de Argentina. Ordenar y Buscar la posicion

equipos = ["Boca Juniors" , "River Plate" , "Racing" , "Independiente" , "San Lorenzo"]
equipos.sort() # Ordenamos alfabeticamente
print("Equipos Ordenados:" , equipos) 

indices = equipos.index("River Plate") # Buscamos por Indice
print("Posición de River Plate:" , indices) 


## 08. Lista de comidas típicas argentinas

comidas = ["Asado" , "Empanadas" , "Milanesas" , "Locro" , "Choripán"]
comidas.insert(1 , "Alfajor") # Insertamos en la posición 1
print("Después de insertar:" , comidas)

comidas.pop() # Eliminamos el Precio
print("Lista después de eliminar el ultimo:" , comidas)


## 09. Lista de precios en pesos argentinos

precios = [1500 , 2500 , 1200 , 4500 , 3000]

precio_max = max(precios)
print("Precio más alto:" , precio_max)

precio_min = min(precios)
print("Precio más bajo:" , precio_min)


