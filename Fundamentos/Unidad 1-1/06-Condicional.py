### Condicionales en Python

## Los condicionales en Python son estructuras que te permiten ejecutar ciertos bloques de código según se cumpla o no una condición. Básicamente, es como decirle a la computadora: "Si pasa esto, hacé tal cosa; si no, hacé otra cosa". 
## Son clave para que un programa tome decisiones.

###################################################

# Ejemplo : Hay partido de la selección?
# Si hay partido, te preparás para verlo. Si no, te relajás.

hay_partido = True

if hay_partido:
    print("Hoy se para el país , a ver el partido")
else:
    print("No hay partido , dia tranquilo")

#######################################################

# Ejemplo : Te alcanza para para el boleto de colectivo?

dinero = 100
precio = 150

if dinero >= 150:
    print("Me alcanza para el colectivo.")
else:
    print("No me alcanza , toca caminar.")

##########################################################

# Ejemplo : Están ganando los pumas?

puntos_pumas = 25
puntos_rival = 30


if puntos_pumas > puntos_rival:
    print("Vamos los Pumas , estamos ganando")
else:
    print("Hay que remontar, vamos con todo.")