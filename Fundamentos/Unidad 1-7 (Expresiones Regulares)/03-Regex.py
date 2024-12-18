
import re

email = "gustavorodriguez@gmail.com.c?"

# Definimos el patrón de la expresión regular para validar el correo
# Básicamente, queremos asegurarnos de que el correo tenga el formato correcto.
# El formato típico es: 'usuario@dominio.extension'

# Empezamos con la parte local (antes del @):
# [a-zA-Z0-9._%+-]+
#   - Esto dice que la parte antes del @ puede tener letras (mayúsculas o minúsculas),
#     números, puntos (.), guiones bajos (_), signos de porcentaje (%), más (+) o guiones (-).
#   - El símbolo '+' es importante porque significa que debe haber al menos uno de estos caracteres.

# Después tenemos el símbolo @:
#   - Es el separador entre la parte local y el dominio.

# Ahora vamos con el dominio:
# [a-zA-Z0-9.-]+
#   - El dominio (después del @) puede tener letras, números, puntos (.) y guiones (-).
#   - El '+' significa que debe haber al menos un carácter de estos.

# Después, el punto literal (.) que necesitamos para separar el dominio de la extensión:
# \.
#   - El carácter '\' escapa el punto porque en las expresiones regulares el punto tiene un significado especial (cualquier carácter).
#     Entonces, usamos el '\' para decir "oye, quiero un punto literal aquí".

# Finalmente, la extensión del dominio (como .com, .org, etc.):
# [a-zA-Z]{2,}
#   - Aquí validamos que la extensión tenga solo letras (mayúsculas o minúsculas) y al menos 2 caracteres. Ejemplo: ".com", ".org".

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Ahora vamos a intentar hacer coincidir el correo con este patrón usando re.match()
# re.match() revisa si el correo sigue el patrón desde el principio
result = re.match(pattern, email)

# Si re.match() devuelve algo, significa que la coincidencia fue exitosa
if result:
    # Si result no es None, el correo es válido
    print("Dirección de correo válida")
else:
    # Si result es None, entonces el correo no cumple con el patrón y es inválido
    print("Correo Inválido")
