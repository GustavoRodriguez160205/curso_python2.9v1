
# Promedios de duración
otros_min = 2.5
otros_max = 7
otros_prom = 4 
dalto = 1.5

### Ejercicio A: Mostrar las diferencias

# Calculamos el Porcentaje
diferencias_min = 100 - dalto / otros_min  * 100
difernecia_max =  100 - dalto * 1000 // otros_max * 100
diferencia_prom = 100 - dalto / otros_prom * 100

## Mostramos
print("El curso de Dalto dura:")

print("------------------------")
print(f" - El curso de Dalto dura un {diferencias_min} % menos que el más rapido.")
print(f" - El curso de Dalto dura un {difernecia_max}  % menos que el más lento.")
print(f" - El curso de Dalto dura un {diferencia_prom} % menos que el promedio.")
print("--------------------------")


##########################################
##########################################
##########################################
##########################################
##########################################

### Ejercicio B y C: Mostrar la difirencia de crudo 

crudo_promedio = 5
dalto_promedio = 3.5

tiempo_vacio_promedio = 100 - otros_prom * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto // dalto_promedio / 10

## Mostramos las diferencias de tiempo eliminado
print(f" - Un curso promedio elimina: {tiempo_vacio_promedio} % de tiempo vacio.")
print(f" - Este curso elimnó: {tiempo_vacio_dalto} % de tiempo de vacio")

print("-------------------------------------------------------")
print("-----------------------------------------------------")

## Mostramos diferencias si los cursos duran 10 horas
print(f" - Ver 10hs de este curso equivale a ver:  {otros_prom * 1000 // dalto / 100} horas de otros cursos")
print(f" - Ver 10hs de otros cursos equivale a ver {dalto * 100 // otros_prom / 100}  horas de este curso ")