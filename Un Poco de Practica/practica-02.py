### Practica de metodos de cadenas en python

## 01. Contar la frecuencia de una palabra en la cadena

contar = input( "Ingresa una frase por favor:" )
veces_repetidas = contar.count("a")
print(f"La palabra se repite {veces_repetidas}")


## 02. Reemplazar un texto dentro de una cadena

reemplazo = "Hola a todos como están"
texto_Cambiado = reemplazo.replace("como" , "Como")
print(f"La frase cambiada queda asi: {texto_Cambiado}.")

## 03. Comprobar si una cadena empieza o termina con una subcadena

empieza = "Javier Milei va a ser uno de los mejores presidentes de Argentina"
verificar = empieza.startswith("Javier")
print(f"Seguro ue empieza con esa?: {verificar}")

## 04. Convertir una cadena a mayúsculas 

may = input("Ingresa una cadena para poner en mayúscula: ").upper()
print(f"La cadena en mayúscula queda así: {may}")

min_ = input("Ingresa una cadena para poner en minúscula: ").lower()
print(f"La cadena en minúscula queda así: {min_}")


## 05. Eliminar espacios Extras

frase = " Hola , mundo "
frase_sin_espacios = frase.strip()
print(f"La frase sin espacios queda asi: {frase_sin_espacios}")



## 06. Buscar Subcadenas

repite = input("Ingresa una frase y te diré cuántas veces se repite 'Python': ").strip()
contar_frase = repite.lower().count("python")
print(f"La palabra 'Python' se repite: {contar_frase} veces.")
