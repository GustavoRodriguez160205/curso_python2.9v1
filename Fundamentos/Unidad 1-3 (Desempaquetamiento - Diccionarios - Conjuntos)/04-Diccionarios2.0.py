##########################################

## Un diccionario es una estructura de datos en programación que almacena pares de clave-valor,
## permitiendo acceder al valor asociado a una clave de manera rápida y eficiente.
## En este tipo de estructuras, cada clave es única dentro del diccionario, 
## lo que significa que no puede haber claves duplicadas. 
## Los diccionarios son también conocidos como "mapas" o "hashmaps" en algunos lenguajes.

## Características principales:

## - Claves únicas: Cada clave dentro de un diccionario debe ser única. Si se intenta insertar una clave duplicada, el valor asociado a la clave original será sobrescrito.
## - Acceso rápido: Los diccionarios permiten buscar un valor asociado a una clave en tiempo constante promedio, lo que los hace muy eficientes para este tipo de operación.
## - Mutable: Los diccionarios son estructuras mutables, es decir, se pueden modificar después de su creación (agregar, modificar o eliminar elementos).
## - No ordenados (en algunos lenguajes): En muchos lenguajes, como Python antes de la versión 3.7, los diccionarios no garantizan un orden específico de los elementos. A partir de Python 3.7, los diccionarios mantienen el orden de inserción.

############################################

### Métodos de Creación:

# Método 1: Usando dict() para crear un diccionario
diccionario = dict(nombre= "Gustavo", apellido= "Rodriguez")
print("Diccionario creado con dict():", diccionario)

# Método 2: Usando fromkeys() nos permite crear un diccionario sin valores

diccionario = dict.fromkeys(["Nombre" , "Apellido"])
print("Creando con valores none:" , diccionario["Apellido"])


# Creando diccionarios cambiando el valor por defecto a "No se"

diccionario = dict.fromkeys(["Nombre" , "Apellio"], "No se")
print("Diccionario con valores por defecto:" , diccionario)

#############################################

## Las listas no pueden ser claves de un diccionario debido a que son mutables, 
## pero podemos usar `frozenset`, que es inmutable, como clave.

# Usando frozenset como clave para almacenar un conjunto inmutable
diccionario_conjunto = {frozenset(["Dalto", "Rancio"]): "Jajaja"}
print("Diccionario con frozenset como clave:", diccionario_conjunto)

