### Metodos de Diccionarios


## 01. Keys (Nos devuelve las claves del diccionario). (También itera el diccionario)

diccionario = {
    "nombre":" Lucas",
    "apellido": "Dalto",
    "subs": 10000000
}

claves = diccionario.keys()
print(f"Las claves del diccionario son: {claves}")


## 02. Get (Devuelve el valor de una clave). 


claves = diccionario.get("jajsjajdjs")
print("Hola papa , el programa continua ! ")


## Aclaración: (Si no encuentra nada el programa continua)


## 03. Clear (Elimina todos los elementos de la lista)

diccionario.clear()
print(f"El diccionario eliminado: {diccionario}")


## 04. Pop (Igual que en las listas)

diccionario.pop("nombre")
print(f"El diccionario sin nombre: {diccionario}")


## 05. Items (Nos sirve para recorrer el elemento)

diccionario_iterable = diccionario.items()
print(diccionario)