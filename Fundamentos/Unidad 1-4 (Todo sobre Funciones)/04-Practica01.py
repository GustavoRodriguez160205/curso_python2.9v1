### 01. Falto el profe y los chicos van a dar la clase


def obtener(cant_de_compañeros):
    compañeros = [] # Creamos la lista con los compañeros

    # Hacemos un for para pedir información de cada compañero
    for i in range(cant_de_compañeros):
        nombre = input("Ingresa el nombre del compañero:")
        edad = int(input("Ingrese la edad del compañero:"))
        compañero = (nombre , edad)
        compañeros.append(compañero) # Agregamos la información a la lista
    compañeros.sort(lambda x : x[1]) # Ordenamos de menor a mayor según la edad
   
    asistente = compañeros[0][0] # compañeros [x] evuelve una tupla y despues accedemos al nombre
    profesor = compañeros[-1][0] # Para saber cual es el asistente y el profesor

    return asistente , profesor

# Desempaquetamos lo que retorna la función

asistente , profesor = obtener(5)
print(f"El asistente es: {asistente}. Y el profesor es: {profesor}")
