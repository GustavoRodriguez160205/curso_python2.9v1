###################################################
# CONDICIONALES EN PYTHON
###################################################

# Los condicionales permiten que un programa tome decisiones 
# basadas en condiciones específicas. En Python, los condicionales 
# principales son: `if`, `elif` y `else`.

###################################################
# Ejemplo básico: ¿Hay partido de la selección?
###################################################

# Si hay partido, mostramos un mensaje; si no, otro.
hay_partido = True

if hay_partido:
    print("Hoy se para el país, a ver el partido")
else:
    print("No hay partido, día tranquilo")

###################################################
# Ejemplo: ¿Te alcanza para el boleto de colectivo?
###################################################

dinero = 100
precio = 150

if dinero >= precio:
    print("Me alcanza para el colectivo.")
else:
    print("No me alcanza, toca caminar.")

###################################################
# Ejemplo: ¿Están ganando los Pumas?
###################################################

puntos_pumas = 25
puntos_rival = 30

if puntos_pumas > puntos_rival:
    print("Vamos los Pumas, estamos ganando")
else:
    print("Hay que remontar, vamos con todo.")

###################################################
# CONDICIONAL CON MÚLTIPLES CASOS: `if`, `elif`, `else`
###################################################

# Si queremos evaluar más de una condición, usamos `elif`.

temperatura = 15

if temperatura > 30:
    print("Hace mucho calor, mejor quedate en casa.")
elif temperatura > 20:
    print("Día agradable, salí a disfrutar.")
elif temperatura > 10:
    print("Un poco fresco, llevá abrigo.")
else:
    print("Hace frío, mejor quedarse adentro.")

###################################################
# EJEMPLOS AVANZADOS
###################################################

# Ejemplo 1: Determinar si un número es positivo, negativo o cero
numero = 0

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Ejemplo 2: Verificar si una persona puede votar
edad = 16

if edad >= 18:
    print("Podés votar.")
else:
    print("No podés votar aún.")

# Ejemplo 3: Uso combinado de condiciones
# Podés usar operadores lógicos como `and` y `or` en condicionales.
saldo = 500
precio_boleto = 150
es_estudiante = True

if saldo >= precio_boleto and es_estudiante:
    print("Podés viajar con descuento.")
elif saldo >= precio_boleto:
    print("Podés viajar pagando el precio completo.")
else:
    print("No podés viajar, recargá tu saldo.")

###################################################
# NOTAS IMPORTANTES
###################################################

# - Python usa indentación para definir bloques de código. 
#   Asegúrate de usar espacios o tabs consistentes.
# - Las condiciones se evalúan en orden. Una vez que se cumple una,
#   las demás no se evalúan.
# - Podés usar cualquier expresión que devuelva un booleano
#   como condición (`True` o `False`).

