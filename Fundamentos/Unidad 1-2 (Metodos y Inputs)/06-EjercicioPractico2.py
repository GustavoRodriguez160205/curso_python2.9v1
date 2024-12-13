### Enunciado:

### A) Pedirle al usuario que diga cualquer texto real y:
   # - Calcular cuanto tardaría en decir esa frace
   # - ¿Cuantas palabras dijo?

### B) Si se tarda más de un minuto:
   # - Decirle: "Para flaco tampoco te pedí un testamento." 
   # - Calcular cuanto tiempo lo haria dalto que habla un 30% más rapido


frase = input("Decime una frase y te calculo cuanto tiempo tardaria en decirla dalto:")

palabras = frase.split()
cant_palabras = len(palabras)

tiempo_normal = cant_palabras / 2
tiempo = tiempo_normal * 0.7

tiempo_norm_redond = round(tiempo_normal , 2)
tiempo_dalto_redond = round(tiempo , 2)

if tiempo_normal > 60:
    print("Para , no te pedi un testamento")
else:
    print("Frase aceptable.")
   
print(f"Dijiste {cant_palabras} palabras y tardarías aproximadamente {cant_palabras} segundos en decirlas.")
print(f"Dalto lo diría en aproximadamente {tiempo} segundos.")

## Codigo Optimizado