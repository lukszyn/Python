import re

tekst = input("Podaj ciag znakow: ")
szablon = '^[az034789]{1,4}$'

try:
    dopasowanie = re.match(szablon, tekst).group()
    print("Napis pasuje do szablonu")
except (TypeError, AttributeError):
    print("Napis nie pasuje do szablonu")
