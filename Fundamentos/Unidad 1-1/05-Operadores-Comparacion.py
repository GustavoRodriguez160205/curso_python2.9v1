### ¿ Que son ?

## Los operadores de comparación en Python son usados para comparar dos valores y devolver un resultado booleano (True o False) 
## dependiendo de si la comparación es verdadera o no

#######################################################


# Comparación de igualdad (==)
es_igual_que = 3 == 3  # True: 3 es igual a 3
print(es_igual_que)  # Imprime: True

# Comparación de desigualdad (!=)
es_distinto_que = 2 != 5  # True: 2 es distinto de 5
print(es_distinto_que)  # Imprime: True

# Comparación mayor que (>)
mayor_que = 4 > 1  # True: 4 es mayor que 1
print(mayor_que)  # Imprime: True

# Comparación menor que (<)
menor_que = 7 < 10  # True: 7 es menor que 10
print(menor_que)  # Imprime: True

# Comparación mayor o igual que (>=)
mayor_o_igual = 6 >= 6  # True: 6 es igual a 6
print(mayor_o_igual)  # Imprime: True

# Comparación menor o igual que (<=)
menor_o_igual = 3 <= 5  # True: 3 es menor que 5
print(menor_o_igual)  # Imprime: True


################################################################

## Unos ejemplos

a = 5
b = 19
c = 20

comparacion = a + b == c
print(comparacion) # Devuelve Falso

##########################################

contraseña_guardada = 'DaltoMaestro'
contraseña_tipeada = 'DaltoMaestro'


print(contraseña_guardada == contraseña_tipeada)