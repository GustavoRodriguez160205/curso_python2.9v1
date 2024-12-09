### Variables en python

## Son un espacio que se almacenan en la memoria de nuestro programa.
## Los datos se pueden reutilizar a lo largo del programa.
## Las variables son modificables y reutilizarse

## Ejemplo con texto. Mostramos por consola un nombre
# Declaro | Definimos
nombre = 'Javier'
print(nombre)

## Ejemplo con números. Realizamos una suma de variables

a = 4
b = 12
c = a + b
print(c) # Con un print podemos ver el codigo por consola

## Otro ejemplo
numero = 10
numero += 5 # El + funciona como un incremento
numero += 5
numero -= 3
print(numero)


### Concatenación de variable
## Es la unión de dos strings
## El espacio cuenta como cada caracter
## Este formato no es muy optimo , porque no nos permite trabajar con números

nombre = 'Lucas'
bienvenida = ' Hola ' + nombre + ' como estás? '
print(bienvenida)

## El formato recomendado es el f-strings
## Con f-strings es la mejor forma de integrar un número con python
nombre = 'Pedro'
bienvenida = f"Hola {nombre} como estás?"
print(bienvenida)

## El operador DEL es un operador que nos sirve para borrar datos.

nombre = True
bienvenida = f'Hola {nombre} como estás?' # Si lo ponemos arriba de bienvenida da error
del nombre  # Pero si lo ponemos abajo no
print(bienvenida)



### Operadores de pertenencia y identidad
## Estos operadores nos van a dar true o false
nombre = True
bienvenida = f' Hola {nombre} ¿Como estás? '

print("ola" in bienvenida) # Da true porque ola si está en bienvenida
print("pedro" not in bienvenida) # Da true porque es verdad que no está. Not in es como decir : no está 

nombre = 'Lucas'
bienvenida = f' Hola {nombre} ¿Como estás? '
print('Mario' in bienvenida)



### Escritura de variables : 

# camel-case
nombreCompleto = 'Lucas Dalto'

# snake-case (Está es la recomendada por python)
nombre_completo = 'Leonel Andres Messi'
