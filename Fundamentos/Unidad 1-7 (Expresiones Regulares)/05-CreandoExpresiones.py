import re

# Detectando un número CABA y ocultándolo

texto = "Hola Pedro, mi número es: +54 11 4321-4321"

# Definimos la expresión regular para detectar un número de teléfono CABA
# Explicación detallada del patrón:
# \+ : El símbolo '+' debe ser escapado con una barra invertida (\) porque en las expresiones regulares, el '+' tiene un significado especial.
#      Así que \+ busca el símbolo '+' literalmente.
#
# \d{2} : Esto busca exactamente dos dígitos (números del 0 al 9). En este caso, corresponde al código de país (como el "54" de Argentina).
#
# \s? : El símbolo '\s' busca un espacio en blanco (como un espacio o tabulación). El '?' hace que este espacio sea opcional, es decir, puede estar presente o no.
#       Esto permite que haya o no un espacio entre el código de país y el código de área (como en el número "+54 11").
#
# \d{2} : Nuevamente, buscamos exactamente dos dígitos. Esto corresponde al código de área (como el "11" en este ejemplo).
#
# \s? : Nuevamente, se permite un espacio opcional entre el código de área y el número de teléfono.
#
# \d{4}-\d{4} : Esto busca un número de teléfono con cuatro dígitos, seguido de un guion y luego otros cuatro dígitos.
#              Es decir, coincide con la parte del número "4321-4321" en el ejemplo.
# 
# El patrón completo se ve como: 
# +<código de país> <código de área> <número de teléfono>


# Ejemplo de coincidencia: +54 11 4321-4321

patterns = r'\+\d{2}\s?\d{2}\s?\d{4}-\d{4}'
reemplazo = re.sub(patterns, "(Número oculto)", texto)
print(reemplazo)
