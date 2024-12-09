### Inputs en Python
nombre = input(" Che maestro , dame tu nombre: ")
print(f" Mostramos el nombre: {nombre} ")

######################################

numero = input(" Danos un número: ")
resultado = numero * 2  # Aquí multiplicamos el texto que ingresamos por 2
print(f"El resultado va a ser : {resultado}")

## Aclaración: Aqui no multiplicamos números estamos repitiendo cadenas de texto porque el tipo de dato es string.

######################################

## Para que funcione tiene que estár convertido el número o el input a entero

numero1 = input(" Danos un número: ")
resultado1 = int(numero1) * 2
print(f"El resultado ahora si es un número: {resultado1}")


#########################################

## Aca cambiamos el número a flotante y lo multiplicamos por 2

resultado1 = float(numero1) * 2
print(f"El número con resultado decimal quedara asi: {resultado1}")