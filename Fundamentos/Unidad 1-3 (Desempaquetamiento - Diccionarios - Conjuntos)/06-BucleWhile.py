####################################################

contador = 0 # Variable que se va a ir incrementando

# Se ejecutará mientras el contador sea menor que 10
# Vuelta tras vuelta se verifica la condición
while contador < 10:
    contador += 1  # Incrementamos el contador en 1
    print(contador)  
    

print("El bucle 'while' ha terminado")


#######################################################

## Algunos Ejercicios para entenderlos

contador = 10

while contador >= 10:
    contador -= 1
    print(contador)

print("¡Despegue!")


###########################################################

## Suma de números del 1 al 50

suma = 0 # Aqui se va a incrementar 
numero = 1 # Comenzamos desde 0


while numero <= 50:
    suma += numero # Sumamos el número actual 
    numero += 1 # Pasamos al siguiente número

print("La suma de los números del 1 al 100 es:" , suma)


############################################################

## Pedir contraseña

contraseña = ""

while contraseña != '1234': # Bucle que se ejecutara hasta que la contraseña sea 1234
    contraseña = input("Ingresa la contraseña:") # Pedimos la Contraseña

print("Acceso concedido")

##############################################################

## Números Pares

numero = 0

while numero <= 20: # Se ejecutara mientras el número sea <= a 20
    numero += 2 # Incrementamos en 2 para obtener el número par
    print(f"Los números pares son: {numero}")

###############################################################

## Suma hasta que sea suficiente

suma_total = 0
numero = 0

while numero >= 0: # Se ejecutara hasta que sea un num negativo
    numero = int(input("Ingresa un número ( negativo para salir ):"))
    if numero >= 0: # Si el número es positivo o cero, lo sumamos
        suma_total += numero

print("La suma total de los números positivos es:" , suma_total)


####################################################################

## Contar la letra "a"

texto = input("Ingresa una cadena de texto:")

contador = 0  # Recorre cada carácter
cantidad_a = 0 # Cuenta las A

while contador < len(texto):
    if texto[contador].lower() == "a": # Comprobamos el caracter actual
        cantidad_a += 1 # Si aparece una "a" aumentamos el contador
    contador += 1 # Pasamos al siguiente carácter

print(f"La letra 'a' aparece {cantidad_a} veces en la cadena")



