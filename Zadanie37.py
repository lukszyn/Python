import re

tekst = input("Podaj ciag znakow: ")
szablon = '^[abcdx\.]{1,7}$'

try:
    dopasowanie = re.match(szablon, tekst).group()
    print("Napis pasuje do szablonu")
except (TypeError, AttributeError):
    print("Napis nie pasuje do szablonu")
