### Datos compuestos en python

# Los datos compuestos en Python son tipos de datos que pueden guardar más de un valor a la vez.
# Estos valores pueden ser de diferentes tipos y se agrupan en una sola variable. 
# Cuando trabajas con datos compuestos como listas, tuplas, conjuntos o diccionarios, la numeración o índices siempre comienza desde 0. 
# Esto significa que el primer elemento de una colección se encuentra en el índice 0, el segundo en el índice 1, y así sucesivamente.

# (Aclaración en general) : El metodo type nos va a devolver que dato compuesto es


### Listas (Se pueden modificar)
lista = ['Lucas Dalto' , 'Soy Dalto' , False , 1.64]

print(lista[0]) # Accedemos a un valor de la lista.

# Está es una forma de manipular un dato de la lista.
lista[3] = 'Maquinola' 
print(lista)           
 


## Datos compuestos no modificables

####################################################

### Tuplas (No se puede modificar)
tupla = ('Lucas Dalto' , 'Soy Dalto' , True , 1.41)
print(tupla)


### (Aclaración para ambos: Para que se puedan modificar , hay que crear una nueva)

######################################################

### Creamos un conjunto (Set) (No se pueden modificar) 
## Los conjuntos no tienen un orden fijo, los valores pueden cambiar su lugar y estara todo ok
## La diferencia con las listas : No se pueden acceder con el indice , No se pueden repetir valores
## Para acceder a los datos de un conjunto hay que utilizar los bucles.
conjunto = {'Leonel Messi' , 'El goat' , True , 1.65}
print(conjunto)



######################################################
## Diccionarios (JSON en JS)
## La estructura es clave : valor y se separa con comas

diccionario = {
    # Clave    Valor
    'Nombre': 'Lucas Dalto',
    'Canal' : 'Soy Dalto',
    'Esta_emocionado' : True,
    'Altura' : 1.96
}

print(diccionario["Nombre"]) # Accedemos a los elementos.
print(diccionario["Canal"])


