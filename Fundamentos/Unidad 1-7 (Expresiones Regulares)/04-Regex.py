
import re
text = "Este es un ejemplo de una página web: https://proyectodalto.com y también podemos visitar http://example.org"


# Explicación del patrón:
# https?://
#   - https? significa que podemos encontrar 'http' o 'https'. La "s" es opcional gracias al '?', que significa "cero o uno".
#   - :// es el separador entre el protocolo y la dirección de la página (algo como 'http://').
#
# [a-zA-Z0-9.-]+
#   - Aquí estamos buscando el dominio de la página web, que puede tener letras (mayúsculas o minúsculas), números,
#     puntos (.) o guiones (-).
#   - El '+' asegura que haya al menos uno de estos caracteres.
#
# \.
#   - El punto (.) se coloca con el carácter '\' porque en las expresiones regulares el punto tiene un significado especial:
#     coincide con cualquier carácter. Entonces, usamos '\.' para decir "quiero un punto literal aquí".
#
# [a-zA-Z]{2,}
#   - Esto valida la extensión del dominio, como .com, .org, etc.
#   - Aceptamos solo letras (mayúsculas o minúsculas) y el {2,} significa que debe haber al menos 2 letras en la extensión.
#   - Ejemplo válido: ".com", ".org", ".net".

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Usamos re.findall() para buscar todas las coincidencias que cumplan con el patrón en el texto
# re.findall() devuelve una lista con todas las coincidencias encontradas.
result = re.findall(pattern, text)

print(result)
