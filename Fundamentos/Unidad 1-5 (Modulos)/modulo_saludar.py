# Importamos el módulo "modulo" y le asignamos un alias para sus funciones
# import modulo as m.saludar

# Importamos dos funciones específicas del módulo y les cambiamos el nombre:
# - La función `saluar_raro` la renombramos como `saludar_como_coscu`
from modulo import saludar, saluar_raro as saludar_como_coscu

# Creamos dos variables para almacenar los saludos generados por las funciones

# Usamos la función `saludar` para generar un saludo y lo asignamos a la variable `saludo`
saludo = saludar("Gustavo")
print(saludo)

# Usamos la función `saludar_como_coscu` (antes llamada `saluar_raro`) para generar otro saludo
# y lo asignamos a la variable `saluar_raro`
saluar_raro = saludar_como_coscu("Fran")
print(saluar_raro)
