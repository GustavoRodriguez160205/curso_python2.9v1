## Creando una función que nos devuelva los números primos entre 0 y el que le pasemos
    

# Función que verifica si un número es primo
def es_primo(num):
    # Verificamos que el número pasado no pueda dividirse
    # por ningún n° entero entre 2 y ese mismo -1
    for i in range(2 , num - 1):
        # Si es divisible retornamos false y termina el bucle
        if num % i == 0: return False
    return True # Si termina el bucle siginifca que no fue divisible entonces es primo


# Función que retorna una lista con todos los números primos
def primos_hasta(num):
    # Creamos la lista
    primos = []
    for i in range(3, num + 1):
        # Verificamos si es primo
        resultado = es_primo(i)
        # Eb casi de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    return primos # Devolvemos la lista

resultado = primos_hasta(14)
print(f"Los números primos son: {resultado}")
