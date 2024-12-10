### 01. Contar hasta 10

for numero in range(1,11):
    print(f"Los números son: {numero}")


### 02. Saluar a tus amigos

nombre = ["Ana" , "Luis" , "María" , "Juan"]
print("!Saludos a todos¡")

for amigo in nombre:
    print(f"Hola, {amigo}! ¿Cómo estás?")



### 03. Multiplicar por 2

numeros = [ 1 , 2 , 3 , 4 , 5]

print("Los números multiplicados serían:")
for num in numeros:
    resultado = num * 2
    print(resultado)


### 03. Contar letras en una palabra

palabra = input("Ingresa una oración por favor:")

contador = 0

for carac in palabra:
    if carac == "e":
        contador += 1

print(f"La letra 'e' se repite {contador} veces en la palabra.")



### 04. Nombre de Provincias

prov = ["Buenos Aires" , "CABA" , "Mendoza" , "Córdoba" , "Santa Fe"]


for provin in prov:
    en_min = provin.lower()
    print("Las provincias en minúsculas son:" , en_min)

### 05. Ordenar las provincias de forma ascendente

prov = ["Buenos Aires", "CABA", "Mendoza", "Córdoba", "Santa Fe"]

prov.sort()

print("Las provincias ordenadas quedan así:")
for pro in prov:
    print(pro)


### 06. Contar cuantas provinias tienen más de 10 caracteres


prov = ["Buenos Aires", "CABA", "Mendoza", "Córdoba", "Santa Fe"]

cont = 0

for pro in prov:
    if len(pro.replace(" " , "")) > 10:
        cont += 1

print(f"Hay {contador} provincia con más de 10 caracteres.")


### 07. Contar si una provincia tiene la letra "o"


prov = ["Buenos Aires", "CABA", "Mendoza", "Córdoba", "Santa Fe"]

for pro in prov:
    if "o" in pro.lower():
        print(f"La provincia '{pro}' contiene la letra 'o'.")
    else:
        print(f"La provincia '{pro}' no ontiene la letra 'o'.")