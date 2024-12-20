

frutas = ["Banana", "Manzana", "Ciruela", "Pera", "Naranja", "Granada", "Durazno"]

######################################################


# Usamos `continue` para evitar comer una "Granada"

print("Evitar comer una Granada usando 'continue':")
for fruta in frutas:
    if fruta == "Granada":
        continue  # Saltar la iteración si la fruta es "Granada"
    print(f"Me voy a comer una: {fruta}")


######################################################

# Usamos `break` para detener el bucle al encontrar una "Pera"

print("\nDetener el bucle al encontrar una Pera usando 'break':")
for fruta in frutas:
    if fruta == "Pera":
        break  # Terminar el bucle si encontramos una "Pera"
    print(f"Me voy a comer una: {fruta}")

print("\nBucle Terminado")

######################################################

# Recorremos una cadena de texto

cadena = "Hola Dalto"

print("\nRecorriendo una cadena de texto:")
for letra in cadena:
    print(letra)

######################################################

# For en una sola línea de código

numeros = [2, 5, 8, 10]
numeros_duplicados = [x * 2 for x in numeros]  # Multiplicamos cada número por 2
print("\nLista de números duplicados:", numeros_duplicados)

######################################################
