### Enunciado:

### A) Pedirle al usuario que diga cualquer texto real y:
   # - Calcular cuanto tardaría en decir esa frace
   # - ¿Cuantas palabras dijo?

### B) Si se tarda más de un minuto:
   # - Decirle: "Para flaco tampoco te pedí un testamento." 
   # - Calcular cuanto tiempo lo haria dalto que habla un 30% más rapido


frase = input("Decime una frase y te calculo cuanto tardarías si tuviaras que decirla:")

palabras_sep = frase.split(" ") # Separamos por espacios
cantd_palabras = len(palabras_sep) # Calculamos la longitud

# Condidional para calcular cuantas palabras escribio
if cantd_palabras > 120:
    print("Para flaco tampoco te pedi un testamento")

print(f"Dijiste: {cantd_palabras} palabras , y tardarias { cantd_palabras / 2 } segundos en decirlas")
print(f"Dalto se demoraría {cantd_palabras * 100 // 2 * 1.3 / 100} segundos en decirlo.")

