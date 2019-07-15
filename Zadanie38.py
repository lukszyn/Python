import re

tekst = input("Podaj ciag znakow: ")
szablon = '^[\-]?[0-9]*[\.]?[0-9]*$'
try:
    dopasowanie = re.match(szablon, tekst).group()
    print("Napis pasuje do szablonu")
except (TypeError, AttributeError):
    print("Napis nie pasuje do szablonu")