########################################
### Condicionales

### 01.
## Escribe un programa que reciba la temperatura actual en Buenos Aires e indique:
##  -"Hace frío" si está por debajo de 15°C.
##  -"Está agradable" si está entre 15°C y 25°C.
##  -"Hace calor" si supera los 25°C.

temperatura_bsas = int(input(" Por favor ingresa una temperatura: "))

if temperatura_bsas < 10:
    print("Hace frio")

elif temperatura_bsas == 15:
    print("Está Bien")
    if temperatura_bsas == 25:
        print(f"Está agradable hace {temperatura_bsas}")

elif temperatura_bsas >= 30 and temperatura_bsas <= 50:
     print(f"Hace calor, la temperatura es de: {temperatura_bsas} grados")


### 02. 
## Crea un programa que reciba una fecha (día y mes) e indique si corresponde a un feriado nacional en Argentina. Ejemplo:
## 25 de mayo: Día de la Revolución de Mayo.
## 9 de julio: Día de la Independencia.

dia = int(input("Ingresa un día por favor: "))
mes = int(input("Ingresa un número de mes por favor (1-12): "))

if dia == 25 and mes == 5:
    print("Es feriado, ¡Día de la Revolución de Mayo!")
elif dia == 9 and mes == 7:
    print("Es feriado, ¡Día de la Independencia!")
else:
    print("No es feriado. El día y mes no coinciden.")



### 03.
## Crea un programa que:
## Pida al usuario que ingrese el nombre de un equipo de fútbol argentino (por ejemplo: Boca, River, Racing, etc.).
## Imprima el estadio correspondiente.

estadios = {
    "River Plate": "Más Monumental",
    "Racing Club": "El Cilindro de Avellaneda",
    "Boca Juniors": "La Bombonera"
}

equipo = input("Por favor ingresa tu club y te diré el nombre de su estadio: ")

if equipo in estadios:
    print(f"El equipo es: {equipo} y su estadio es: {estadios[equipo]}.")
else:
    print("No hay ningún club registrado con ese nombre.")


### 04.
## Crea un programa que:
## Almacene las edades en una lista.
## - Luego, clasifique y muestre cuántas personas hay en cada grupo de edad:
## - Menores de 18 años.
## - Entre 18 y 60 años.
## - Mayores de 60 años.


edades = int(input(" Ingresa una edad por favor: "))

if edades <= 18:
    print("Sos adolescente")

elif edades == 18 and edades <= 60:
    print("Sos un Adulto")

elif edades >= 60:
    print("Sos un jubilado")



### 05.
## Ejercicio de Calificación de Estudiantes

## En Argentina, las calificaciones se dan en una escala de 1 a 10. Escribe un programa que:
##Pida al usuario que ingrese la calificación.
## - Imprima el mensaje correspondiente según la calificación:
## - Menor a 4: "Reprobado"
## - Entre 4 y 6 (inclusive): "Aprobado"
## - Entre 7 y 8 (inclusive): "Muy bueno"
## - Entre 9 y 10 (inclusive): "Excelente"

nota = int(input("Ingresa una nota por favor:"))

if nota < 4:
    print(f"Estás reprobado, tu nota es: {nota}")
elif 4 <= nota <= 6:
    print(f"Estás Regular, tu nota es: {nota}. Vas a tener que ir al final")
elif 7 <= nota <= 8:
    print(f"Estás Promocionado, tu nota es: {nota}")
elif 9 <= nota <= 10:
    print(f"Estás más que promocionado. Tu nota final es: {nota}")
else:
    print("Nota inválida")


### 06.
## Ejercicio de Elección de Comida Típica
## En Argentina, hay platos típicos de diferentes regiones. Escribe un programa que:

## Pida al usuario que ingrese una provincia.
##  Según la provincia, el programa debe sugerir una comida típica:
## - Buenos Aires: "Asado"
## - Córdoba: "Cuarto de cordero"
## - Mendoza: "Empanadas"
## - Tucumán: "Tamales"
## - Salta: "Locro"

city_ingresada = input("Ingresa una ciudad por favor: ").strip()  # strip() para eliminar espacios extra

# Convertir a minúsculas para validar sin importar las mayúsculas/minúsculas
city_ingresada = city_ingresada.lower()

# Validación para asegurar que se ingresó algo
if not city_ingresada:
    print("No ingresaste ninguna ciudad.")
elif city_ingresada == "buenos aires":
    print(f"Si es {city_ingresada.title()}, te recomiendo comer un buen Asado.")
elif city_ingresada == "cordoba":
    print(f"Si es {city_ingresada.title()}, te recomiendo comer un Cuarto de Cordero.")
elif city_ingresada == "mendoza":
    print(f"Si es {city_ingresada.title()}, te recomiendo comer unas Empanadas.")
elif city_ingresada == "tucumán":
    print(f"Si es {city_ingresada.title()}, te recomiendo comer unos Tamales.")
elif city_ingresada == "salta":
    print(f"Si es {city_ingresada.title()}, te recomiendo comer un Locro.")
else:
    print("La ciudad ingresada no está en nuestra lista de recomendaciones.")
