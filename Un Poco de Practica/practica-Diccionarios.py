# 01 ) Obtener las claves del diccionario

frutas = {
    "Manzana": 10,
    "Banana": 20,
    "Pera": 15
}

for i in frutas:
    print(i)


# 02 ) Obtener los pares clave - valor

productos = {
    "Manzana": 10,
    "Banana": 20,
    "Pera": 15
}


for clave,valor in productos.items():
    print(f"La clave es: {clave}, y el valor es: {valor}")