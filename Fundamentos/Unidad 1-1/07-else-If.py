### Else If

#  Es una forma de agregar condiciones adicionales después de un if. Sirve para evaluar múltiples posibilidades sin necesidad de usar varios if separados, 
#  haciendo que el código sea más claro y eficiente.


##########################################

# 01. Ejemplo If - Else y Anidados

ingreso_mensual = 100000
gasto_mensual = 89000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en déficit")  # El gasto es mayor que el ingreso.
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estás bien")  # Hay un margen positivo mayor a 3000.
    else:
        print("Estás gastando una banda")  # Margen positivo, pero menor o igual a 3000.

elif ingreso_mensual > 1000:
    print("Estás bien en Latinoamérica")  # Ingresos moderados en el contexto latinoamericano.

elif ingreso_mensual > 500:
    print("Estás bien en Argentina")  # Ingreso bajo, pero aceptable en Argentina.

elif ingreso_mensual > 200:
    print("Estás bien en Venezuela")  # Ingreso muy bajo, pero notable en Venezuela.

else:
    print("Sos pobre")  # Ingreso extremadamente bajo, en situación complicada.


###########################################


# 02. Calificación de un estudiante

notaFinal = 30


if notaFinal >= 90:
    if notaFinal == 100:
        print("Estás aprobado con la maxima calificación")
    else:
        print("Muy bien , has sacado una calificación excelente")

elif notaFinal >= 75:
    print("Bien echo , has aprobado con una nota buena")

elif notaFinal >= 70:
    print("Aprobaste , pero puedes mejorar")

elif notaFinal >= 50:
    print("Pasaste por poco , te recomiendo estudiar más")

else:
    print("No has aprobado , pero aún puedes mejorar.")

