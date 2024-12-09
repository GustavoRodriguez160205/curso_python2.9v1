### Metodos de Cadenas

## Son funciones que permiten manipular, modificar y consultar cadenas de texto (strings) de manera sencilla. 
## Se usan para tareas como cambiar mayúsculas 
## y minúsculas, reemplazar texto, buscar palabras o separar contenido.

cadena1 = "Hola soy dalto"
cadena2 = "Bienvenido Maquinola"

### 01. Dir (Nos va a devolver todos los metodos). Dir no es un metodo , es una función

resultado = dir(cadena1)
#print(resultado)

### 02. Upper (Convierte todo el texto a mayúsucla)

resultado = cadena1.upper()
print(f"El texto en mayúscula es: {resultado}")

### 02. Lower (Convierte a minúsculas)

resultado = cadena1.lower()
print(f"El texto en minúscula es: {resultado}")

### 03. Capitalize (Convertimos la primera letra a mayúscula)

cadena3 = "argentina"
resultado = cadena3.capitalize()
print(f"La primer letra a mayúscula quedara asi: {resultado}")

### 04. Find (Buscamos el valor de una cadena en otra cadena). (Nos devolvera la posición en la que encuentra lo que le pedimos)

busqueda_find = cadena3.find("t")
print(f"El resultado de la busqueda es: {busqueda_find}")

## Aclaración : (Los espacios también cuentan , porque son un caracter más)
## Aclaración : (Si no encuentra lo que le pedimos , nos da -1 )

### 05. Index (Es igual al metodo find)

cadena4 = 'Hola , Argentina'
busqueda_index = cadena4.index("A")
print(f"La búsqueda con index es: {busqueda_index}")

## Aclaración: (Si no las encuentra , aca nos devuelve una exepción)


### 06. Isnumeric (Nos permite ver si es una función o no). (Devuelve True o False)

es_numero = cadena1.isnumeric()
print(es_numero)

### 07. IsAlpha (Devuelve True si todos los caracteres son letras , sin espacios , números ni simbolos)

cadena5 = 'Argentina2024'
es_alfanumerico = cadena5.isalpha()
print(f"Es alfanúmerico: {es_alfanumerico}") # Devuelve False porque contiene letras y núemros

cadena6 = 'Argentina'
es_solo_letras = cadena6.isalpha()
print(f'Es alfanúmerico: {es_solo_letras}') # Develve True porque es solo texto


### 07. Count (Nos va a decir las coincidencias que hay en una cadena)

contar_coincidencias = cadena1.count("o")
print(f"Va a aparecer: {contar_coincidencias}")

## Aclaración : Si no se encuentra va a devolver 0

### 08. Len (Devuelve la cantidad de caracteres que tiene una cadena.) (Es una función , no un metodo)

contar_Caracteres = len(cadena1)
print(f"La cantidad de caracteres es: {contar_Caracteres}")


### 09. Endswith (Verificamos si una cadena empieza por sierto caracter). (Devuelve True o False)

empieza_con = cadena1.startswith("o")

print(f"Empieza con? {empieza_con}")

### 10. StartsWith (Verificamos si una cadena termina por sierto caracter). (Devuelve True o False)

termina_con = cadena1.startswith("p")
print(f"Termina con? {termina_con}")

### 11. Replace (Reemplaza un pedazo de la cadena dada , por otra que le pasemos)

cadena_nueva = cadena1.replace("Hola" , "Hole maquina")
print(f"La cadena reemplazada seria asi: {cadena_nueva}")

## Aclaración (Si encuentra una concidiencia con la cadena que le pasamos , la va a reemplazar)


### 12. Split (Separa el valor por el parametro dado). Separa todo lo que le pasemos , y nos va a devolver una lista

cadena_separada = cadena1.split(",")
print(f"La cadena separada queda asi: {cadena_separada}")