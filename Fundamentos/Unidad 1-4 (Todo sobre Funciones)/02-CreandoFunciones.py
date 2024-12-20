# Introducción: Creando mis propias funciones

#######################################################

# Ejemplo 1: Función sin parámetros
def saludar():
    print("Hola Lucas, mi maestro. ¿Cómo andas?")

# Llamamos a la función para ver el saludo
saludar()

#######################################################

# Ejemplo 2: Función con parámetros
def saludar_personalizado(nombre, sexo):
    adjetivos = {
        "Mujer": "muchacha",
        "Hombre": "titán",
    }
    # Utilizamos get para manejar valores no contemplados
    adjetivo = adjetivos.get(sexo, "persona no binaria")
    print(f"Hola {nombre}, mi {adjetivo}. ¿Cómo andas?")

# Llamamos a la función con diferentes parámetros
saludar_personalizado("Camila", "Mujer")
saludar_personalizado("Lucas", "Hombre")
saludar_personalizado("Alex", "Otro")

#######################################################

# Ejemplo 3: Función que retorna múltiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    primer_digito = int(str(num)[0])  # Obtenemos el primer dígito
    c1 = primer_digito - 2
    c2 = primer_digito
    c3 = primer_digito - 5
    # Generamos la contraseña utilizando caracteres y cálculos
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{primer_digito * 2}"
    return contraseña, primer_digito

# Uso de la función
password, primer_num = crear_contraseña_random(394)
print(f"Tu contraseña nueva es: {password}")
print(f"El número utilizado para crearla fue: {primer_num}")

#######################################################

# Ejemplo 4: Funciones con *args (parámetros variables)
def suma(nombre, *numeros):
    # Usamos sum para calcular la suma de los números
    return f"{nombre}, la suma de tus números es: {sum(numeros)}"

# Llamada con múltiples argumentos
resultado = suma("Lucas", 555, 777, 333, 444)
print(resultado)

#######################################################

# Ejemplo 5: Optimización de la suma total
def suma_total(numeros):
    # sum ya funciona directamente con iterables
    return sum([*numeros])

# Llamada a la función con una lista de números
resultado2 = suma_total([5, 31, 41, 11, 22, 44, 55])
print(f"La suma total es: {resultado2}")

#######################################################

# Ejemplo 6: Creando una función con varios parámetros y argumentos por clave
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

# Usando keyword arguments (no tienen orden)
frase_resultante = frase(adjetivo="capo", nombre="Gustavo", apellido="Rodriguez")
print(frase_resultante)

#######################################################

# Ejemplo 7: Funciones con parámetros opcionales y valores por defecto
def frase1(nombre, apellido, adjetivo="Pelotudo"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

# Cambiando el parámetro por defecto
frase_final = frase1("Lucas", "Dalto", "Muy Inteligente")
print(frase_final)

##############################################

