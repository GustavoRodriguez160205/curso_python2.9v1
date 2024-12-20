### Desempaquetado de variables:

### Definicíon: 

## El desempaquetado de variables en Python es una forma de asignar los valores de una tupla o lista directamente a variables, de manera simple y ordenada.
## Funciona con : Tuplas , Listas 

datos_tupla = ("Gustavo", "Rodriguez", 19)
datos_lista = ["Gustavo", "Rodriguez", 19]

# Desempaquetado
nombre, apellido, edad = datos_tupla

# Mostramos los datos con más contexto
print(f"¡Bienvenido, {nombre} {apellido}! Nos comentaste que tenés {edad} años.")
