
frutas = ["Banana", "Manzana", "Ciruela", "Pera", "Naranja", "Granada", "Durazno"]

# Usamos continue para evitar comer una "Granada"

print("Evitar comer una Granada usando 'continue':")
for fruta in frutas:
    if fruta == "Granada":
        # Saltar la iteración si la fruta es "Granada"
        continue
    print(f"Me voy a comer una: {fruta}")

######################################################

# Usamos break para detener el bucle al encontrar una "Pera"

print("\nDetener el bucle al encontrar una Pera usando 'break':")
for fruta in frutas:
    if fruta == "Pera":
        # Terminar el bucle si encontramos una "Pera"
        break
    print(f"Me voy a comer una: {fruta}")


print("\nBucle Terminado")


#########################################################

## Recorremos una cadena de texto

cadena = "Hola Dalto"

for letra in cadena:
    print(letra)

############################################################

## For en una sola linea de codigo

numeros = [2 , 5 , 8 , 10]

numeros_dupicados = [x * 2 for x in numeros] # Aca la x toma el valor de cada elemento de la lista.
print(numeros_dupicados)