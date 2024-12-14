## Conversión de pesos Argentinos a Dolares

def convertir_a_dolares(*montos, tipo_cambio = 1060):
    resultados = [monto / tipo_cambio for monto in montos]
    return resultados

monto_pesos = convertir_a_dolares(7000 , 14200 , 21000)
print(f"Monto en dólares: {monto_pesos}")

## Promedio de temperaturas en Provincias

def promedio_temperaturas(*temperaturas):
    if not temperaturas:
        return "No se ingresaron temperaturas."
    return sum(temperaturas) / len(temperaturas)

promedio = promedio_temperaturas(18,22,20,24,19,35)
print(f"El promedio de temperaturas es: {promedio:.2f} °C ")


## Calcular precio total en un supermercado.

def calcular_total_supermercado(*precios):
    if not precios:
        return "No se ingresaron precios."
    total = sum(precios)
    total_iva = total * 1.21
    return f"El total con IVA (21%) es: {total_iva:2f}"

total = calcular_total_supermercado(100 , 200 , 300 , 150)
print(total)

## Armar una pizza al estilo Argentino

def pizza(*ingredientes):
    if not ingredientes:
        return "No se especificaron ingredientes para la pizza."
    return f"Tu pizza tendrá: {','.join(ingredientes)}"

pizza = pizza("Muzzarella" , "Jamon" , "Queso" , "Aceitunas")
print(pizza)


## Listar Monumentos Argentinos

def listar_monumentos(*monumentos):
    if not enumerate:
        return "No se ingresaron monumentos."
    lista = "\n".join(f"{i + 1}. {monumentos}" for i, monumentos in enumerate(monumentos))
    return f"Monumentos Argentinos: \n{lista} "

monumentos = listar_monumentos("Obelisco" , "Cerro de los Siete Colores" , "Glaciar Perito Moreno")
print(monumentos)