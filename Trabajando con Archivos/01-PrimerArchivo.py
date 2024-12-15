# Abrimos el archivo

archivo_sin_leer = open("Trabajando con Archivos\\texto01.txt" , encoding= "utf-8")

## Leemos el archivo completo

archivo = archivo_sin_leer.read()


######################################################


# Leer linea por linea

# \n Nos sirve para dejar espacios entre los caracteres

lineas = archivo_sin_leer.readlines()


########################################################

# Leer una sola linea

# Si no lee la linea completa.
# Lee la cantd de caracteres que le digamos
# Para archivos grandes puede consumir toda la memoria de nuestra pc

linea = archivo_sin_leer.readline(10) 


#########################################################

# Cerramos el archivo

archivo_sin_leer.close()





