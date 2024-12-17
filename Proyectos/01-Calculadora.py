def ingreso():
    """Pide dos números al usuario y los retorna."""
    numA = int(input("Ingresa un primer número: "))
    numB = int(input("Ingresa un segundo número: "))
    return numA, numB


def suma(numA, numB):
    """Realiza la suma de dos números."""
    return numA + numB


def resta(numA, numB):
    """Realiza la resta de dos números."""
    return numA - numB


def multiplicacion(numA, numB):
    """Realiza la multiplicación de dos números."""
    return numA * numB


def division(numA, numB):
    """Realiza la división de dos números, manejando división por cero."""
    try:
        return numA / numB
    except ZeroDivisionError:
        print("Error: No se puede dividir por 0.")
        return None


def interacciones():
    """Función principal para interactuar con el usuario."""
    print("\n---- Calculadora -------")

    while True:
        print("\nSelecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        try:
            opcion = int(input("Ingresa una opción del 1 al 5: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 5:
            print("Saliendo de la calculadora... ¡Adiós!")
            break

        if opcion in [1, 2, 3, 4]:
            numA, numB = ingreso()  # Pedimos los números

            if opcion == 1:
                print(f"Resultado de la suma: {suma(numA, numB)}")
            elif opcion == 2:
                print(f"Resultado de la resta: {resta(numA, numB)}")
            elif opcion == 3:
                print(f"Resultado de la multiplicación: {multiplicacion(numA, numB)}")
            elif opcion == 4:
                resultado = division(numA, numB)
                if resultado is not None:
                    print(f"Resultado de la división: {resultado}")
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")


# Llamada principal
interacciones()
