# 01

# A )

# - Poner en mayúsculas
# - Poner en minúsculas
# - Primer letra en mayúsculas

texto = "hola mundo"

texto_mayus = texto.upper() # A mayúscula
texto_minus = texto.lower() # A minúsculas
primera_en_mayuscula = texto.capitalize()


print("Texto en mayúscula:" , texto_mayus)
print("Texto en minúscula:" , texto_minus)
print("Primera letra en mayúscula:" , primera_en_mayuscula)


# B )

# - Contar ocurrencias
# - Reemplazar las ocurrencias
# - Reemplazar
# - Sacar los espacios

aparece = texto.count("h")
print(f"Está palabra aparece {aparece} ves")

reemplazo = "Argentina es campeona del mundo"
texto_reemplazo = reemplazo.replace("Argentina" , "River")
print("El texto reemplazado es:", texto_reemplazo)

sin_caracter = "  Texto para sacar los espacios  "
texto_sin_espacios = sin_caracter.strip()
print("El texto sin espacios quedaria asi:" , texto_sin_espacios)


# C )

# - Comprobar si es Alfanumérica
# - Verifificar si "PYTHON" está completamente mayúsculas

cadena_alfanumerica = "Python123"
es_alfanumerica = cadena_alfanumerica.isalnum()
print("Es una cadena alfanúmerica?" , es_alfanumerica)


esta_en_mayuscula = "PYTHON"
comprobado = esta_en_mayuscula.isupper()
print("Realmente está en mayúsculas?" , comprobado)


# D )

# - Buscar 
# - Dividir y unir cadenas

cadena = "Estoy aprendiendo Python"
se_encuentra = cadena.find("Python")
print("Se encuentra en la posición:" , se_encuentra)

reemplazo = cadena.replace("Python" , "Programación")
print("Texto cambiado:" , reemplazo)


# E )

# - Separar por guiones
# - Eliminar los espacios

texto1 = "Hola, este es un texto que quedara sin espacios"
texto_limpio = texto1.strip().split()
resultado = "-".join(texto_limpio)
print(resultado)