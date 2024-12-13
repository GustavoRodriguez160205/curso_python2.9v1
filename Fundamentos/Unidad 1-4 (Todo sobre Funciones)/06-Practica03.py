## Crea una función que muestre la serie de fibonacci entre el 0 y el número dado



#############################

## Otra forma

def fibonacci(num):
    a, b = 0, 1
    # Creamos una lista vacía donde guardaremos los números de la secuencia
    fibonacci_list = []
    
    # Mientras a sea menor o igual al número límite (num)
    while a <= num:
        # Añadimos el valor de a a la lista
        fibonacci_list.append(a)
        # Actualizamos a y b: 
        # a toma el valor de b (el siguiente número en la secuencia)
        # b toma el valor de a + b (la suma de los dos números anteriores en la secuencia)
        a, b = b, a + b
    
    # Devolvemos la lista con los números de Fibonacci hasta el número límite
    return fibonacci_list

resultado = fibonacci(34)
print(f"El resultado de forma sencilla es: {resultado}")


#################################

## Forma Original

def fibonacci(num):
    a,b = 0,1
    fibonacci_list = [0]
    for i in range(num):
        if b > num: return fibonacci_list
        else:
            fibonacci_list.append(b)
            a,b = b, a + b

resultado = fibonacci(34)
print(f"El resultado de forma original es: {resultado}")

