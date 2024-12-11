### 01.

deportistas = { 
    "Lionel Messi": "Hombre",
    "Diego Maradona": "Hombre",
    "Manu Ginóbili": "Hombre",
    "Gabriela Sabatini": "Mujer"
}

hombres = []
mujeres = []

for nombre,genero in deportistas.items():
    if genero == "Hombre":
        hombres.append(nombre)
        print(f"Es legendario, el deportista es: {nombre}")
    elif genero == "Mujer":
        mujeres.append(nombre)
        print(f"Es legendaria, la deportista es: {nombre}")

print("Hombres:" , hombres)
print("Mujeres:" , mujeres)


### 02. Calcula la producción máxima

produccion = {
    "Buenos Aires": 500000,
    "Santa Fe": 700000,
    "Córdoba": 800000,
    "Entre Ríos": 400000,
    "La Pampa": 600000
}

produc_max = 0
provinc_ton = ""

for provincia , toneladas in produccion.items():
    if toneladas > produc_max:
        produc_max = toneladas
        provinc_ton = provincia

print(f"La provincia con mayor producción es: {provinc_ton} con {produc_max} toneladas.")


### 03. Suma de números del 1 al 10

numero_sumar = [10 , 20 , 30 , 40 , 50 , 60]
resultado = 0

for numero in numero_sumar:
    resultado += numero

print("La suma total de los números es:" , resultado)


### 04. Suma de números pares

pares = [10 , 20 , 30 , 40 , 50]
suma = 0

for num in pares:
    if num % 2 == 0:
        suma += num
    
print("La suma quedaría:" , suma)


### 05. Suma de números en una lista

lista = [ 3 , 5 , 7 ]
suma = 0

for num in lista:
    suma += num

print("La suma quedaria:" , suma)


### 06. Escribe una lista donde cuente números pares e impares

lista = [ 1 , 2 , 3 , 4 , 5 , 6 ]

for num in lista:
    if num % 2 == 0:
        print(f"Este número es par. El número es: {num}")
    elif num % 2 != 0:
        print(f"Este número es impar. El número es: {num}")

### 07. Crear mi propia tabla de multiplicar


numero = int(input("Por favor ingresa un número para generar su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
