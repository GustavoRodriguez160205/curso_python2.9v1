

diccionario = {
    "nombre": "Lucas",
    "apellido": "Dalto",
    "subs": 10000000
}


# 01. keys() - Devuelve todas las claves del diccionario
claves = diccionario.keys()
print(f"Las claves del diccionario son: {list(claves)}")

# 02. values() - Devuelve todos los valores del diccionario
valores = diccionario.values()
print(f"Los valores del diccionario son: {list(valores)}")

# 03. items() - Devuelve los pares clave-valor como tuplas
pares = diccionario.items()
print(f"Los pares clave-valor del diccionario son: {list(pares)}")

# 04. get() - Devuelve el valor de una clave específica
subs = diccionario.get("subs")
print(f"Los suscriptores son: {subs}")

# Si la clave no existe, devuelve None o un valor por defecto
clave_inexistente = diccionario.get("edad", "No especificado")
print(f"Edad: {clave_inexistente}")

# 05. update() - Actualiza o agrega elementos al diccionario
diccionario.update({"edad": 30})
print(f"Diccionario actualizado: {diccionario}")

# 06. pop() - Elimina una clave específica y devuelve su valor
eliminado = diccionario.pop("apellido")
print(f"Elemento eliminado: {eliminado}")
print(f"Diccionario después de pop: {diccionario}")

# 07. popitem() - Elimina y devuelve el último par clave-valor
ultimo = diccionario.popitem()
print(f"Último elemento eliminado: {ultimo}")
print(f"Diccionario después de popitem: {diccionario}")

# 08. clear() - Elimina todos los elementos del diccionario
diccionario.clear()
print(f"Diccionario después de clear: {diccionario}")

# 09. copy() - Crea una copia del diccionario
diccionario_original = {"a": 1, "b": 2, "c": 3}
copia_diccionario = diccionario_original.copy()
print(f"Copia del diccionario: {copia_diccionario}")

# 10. fromkeys() - Crea un nuevo diccionario con claves específicas y un valor predeterminado
nuevas_claves = ["x", "y", "z"]
diccionario_nuevo = dict.fromkeys(nuevas_claves, 0)
print(f"Diccionario creado con fromkeys: {diccionario_nuevo}")

##############################

# Recorriendo un diccionario

data = {

    "Nombre": "Gustavo",
    "Apellido": "Dalto",
    "Edad": 19
}

claves = data.keys()

for clave in claves:
    print(f"Clave: {clave}")


#################################

# Recorriendo pares clave-valor

diccionario = {
 
    "nombre": "Lucas",
    "apellido": "Dalto",
    "subs": 10000000
}

for clave,valor in diccionario.items():
    print(f"Clave: {clave} , Valor: {valor}")


############################################

# Recorriendo los valores

diccionario = {

    "nombre": "Lucas",
    "apellido": "Dalto",
    "subs": 10000000
}

for valor in diccionario.values():
    print(f"Valor: {valor}")


##############################################

# Recorriendo solo las claves y accediendo a los valores

diccionario = {
    "nombre": "Lucas",
    "apellido": "Dalto",
    "subs": 10000000
}

for clave in diccionario:
    valor = diccionario[clave]  
    print(f"Clave: {clave}, Valor: {valor}")
