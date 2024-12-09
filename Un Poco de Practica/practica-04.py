### Practica de Desempaquetamiento de Variables

## 01. 
numeros = (10 , 20 , 30 , 40)
a , b , c , d = numeros
print(f"a = {a} , b = {b} , c = {c} , d = {d}")

valores = [5, 15 , 25 , 35]
x , y , z , w = valores
print(f"x = {x} , y = {y} , z = {z} , w = {w}")


###################################################

## 02.

datos = (1, 2, 3, 4)

# Desempaquetamos la tupla:
# 1. `primero` captura el primer elemento (1)
# 2. `* _` captura el resto de los elementos, excepto el último (en este caso, [2, 3])
# 3. `ultimo` captura el último elemento (4)
primero, *_ , ultimo = datos


print(f"Primero: {primero}, Último: {ultimo}")


#######################################################


## 03. Desempaquetar un Bucle

pares = [(1 , "Uno") , (2 , "Dos") , (3 , "Tres")]
for numero , text in  pares:
    print(f"Número: {numero}  , Texto: {text}")


## 04. Intercambio de Variables

x = 5
y = 10
x , y = y , x
print(f" X = {x} , Y = {y}")


## 05. Multiplicación por escalares

def escalar_tupla(tupla , escalar):
    return tuple(valor * escalar for valor in tupla)

valores = (10 , 20 , 30)
resultado = escalar_tupla(valores , 2)
print(f"Resultado escalado: {resultado}")


############################################

# Ejercicios con Condicionales

## 01. Verificra Datos en una tupla

producto = ("Cuaderno" , 125.50 , 0)

nombre , precio , stock = producto

if stock == 0:
    print(f"El producto '{nombre}' está agotado. No se puede vender.")

elif precio > 1000:
    print(f"El producto '{nombre}' tiene un precio elevado: ${precio}")

else:
    print(f"El producto '{nombre}' está disponible por $'{precio}'. Stock: {stock} unidades.")

## 02. Anlisis de Ventas

accion = ("Tesla" , 750 , 800 , 2.5)

nombre , precio_actual , precio_objetivo , volatilidad = accion

if precio_actual < precio_objetivo * 0.9 and volatilidad < 3:
    print(f"La acción {nombre} es recomendable para comprar. Precio actual: ${precio_actual}")

elif precio_actual > precio_objetivo * 1.1:
    print(f"La acción {nombre} está sobrevalorada. Es recomendable vender. Precio actual: ${precio_actual}")

else:
    print(f"La acción {nombre} debe mantenerse. Precio actual: ${precio_actual} , Precio Objetivo: ${precio_objetivo}")