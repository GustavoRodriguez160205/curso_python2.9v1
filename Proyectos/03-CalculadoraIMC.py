def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def obtener_categoria(imc):
    if imc < 18.5:
        return "Peso bajo"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():

    print("Calculadora de IMC")

    try:

        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))
        imc = calcular_imc(peso, altura)
        categoria = obtener_categoria(imc)  
        print(f"Tu IMC es: {imc:.2f}")
        print(f"Categoría: {categoria}")
        
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()
