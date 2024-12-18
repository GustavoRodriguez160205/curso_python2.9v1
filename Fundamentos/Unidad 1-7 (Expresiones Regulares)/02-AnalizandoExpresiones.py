import re

text = "Reemplazando todas las vocales por el asterisco"

new_Text = re.sub("[aeiou]", "*" , text)
print(new_Text)